# Testing script for optional exam in CPSC113.
# Trying only to use the Python standard library
# here so that class members needn't install anything.
#
# Run this as follows:
# python ./test.py YOUR_URL_HERE

import urllib
import urllib2
import urlparse
import sys
import uuid
import logging
logging.root.setLevel(logging.INFO)

class NoRedirects(urllib2.HTTPErrorProcessor):
    def http_response(self, request, response):
        return response
    https_response = http_response

# Override the urllib2 openener so that it does not
# follow redirects by default.
urllib2.install_opener(urllib2.build_opener(NoRedirects))

def false_if_exception(f):
    """ Used as a decorator on functions. If the call to
        `urlopen` raises an exception, False is returned
        instead of the exception being raised.
    """
    def wrapped_f(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except urllib2.HTTPError as e:
            logging.error(e)
            return False
        except urllib2.URLError as e:
            logging.error(e)
            return False
    return wrapped_f


def fetch(base_url, path, data=None):
    """ Fetches a URL and returns a response object
    """
    url = urlparse.urljoin(base_url, path)
    if data:
        data = urllib.urlencode(data)
    response = urllib2.urlopen(url, data)
    return response

def log_comment(f):
    def wrapped_f(*args, **kwargs):
        result = f(*args, **kwargs)
        print ' --- '.join(['PASS' if result else 'FAIL', args[0]])
        return result
    return wrapped_f

@log_comment
def test_response(comment, base_url, path, data=None, expected_code=None, expected_headers=None, expected_content=None):
    """ Place a get request. Optionally, test the response for
        certain response codes, headers, and content. The
        expected_content parameter can be either a string
        or a function.
    """
    response = fetch(base_url, path, data=data)
    if expected_code:
        if isinstance(expected_code, int):
            if response.code != expected_code:
                return False
        elif response.code not in expected_code:
            return False
    if expected_headers:
        for header_key, header_value in expected_headers.iteritems():
            if response.info().getheader(header_key) != header_value:
                return False
    if expected_content:
        content = response.read()
        if callable(expected_content):
            if not expected_content(content):
                return False
        else:
            if expected_content not in content:
                print 'did not see expected content'
                print content
                return False
    return True

def random_content(length=1):
    return ' '.join(str(uuid.uuid4()) for i in range(length))

def main(base_url):
    posts = [random_content() for i in range(5)]
    results = [
        test_response(
            "The app should be running and return an HTTP 200 response at '/'",
            base_url, '', expected_code=200
        ),
        test_response(
            "The app should respond with text at /robots.txt",
            base_url,
            '/robots.txt',
            expected_code=200,
            expected_headers={'Content-Type': 'text/plain; charset=utf-8'}
        ),
        test_response(
            "The app should redirect '/mrw/class-is-done.gif' to the reaction gif of your choice",
            base_url,
            '/mrw/class-is-done.gif',
            expected_code=[301, 302]
        ),
        #
        test_response(
            "Calling the delete URL should delete all existing posts",
            base_url,
            '/posts/delete',
            expected_code=200
        ),
        test_response(
            "There should be no posts at first (1 of 2)",
            base_url,
            '/posts/0',
            expected_code=404
        ),
        test_response(
            "There should be no posts at first (2 of 2)",
            base_url,
            '/posts/1',
            expected_code=404
        ),
        test_response(
            "We should be able to add a post",
            base_url,
            '/posts/new',
            data={'text': posts[0]},
            expected_code=[301,302]
        ),
        test_response(
            "That post should exist now",
            base_url,
            '/posts/0',
            expected_code=200,
            expected_content=posts[0]
        ),
        test_response(
            "We should be able to create another",
            base_url,
            '/posts/new',
            data={'text': posts[1]},
            expected_code=[301,302]
        ),
        test_response(
            "And it should exist now",
            base_url,
            '/posts/1',
            expected_code=200,
            expected_content=posts[1]
        ),

    ]
    print '{0}/{1}'.format(sum(1 for result in results if result), len(results))


if __name__ == '__main__':
    main(sys.argv[1])
