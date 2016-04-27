# Testing script for optional exam in CPSC113.
# Trying only to use the Python standard library
# here so that class members needn't install anything.
#
import urllib2
import urlparse
import sys
import logging
logging.root.setLevel(logging.INFO)

def false_if_exception(f):
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

@false_if_exception
def test_200_response(base_url):
    url = urlparse.urljoin(base_url, "/")
    response = urllib2.urlopen(url)
    return (response.code == 200)


def main(base_url):
    results = [
        test_200_response(base_url)
    ]
    print results


if __name__ == '__main__':
    main(sys.argv[1])
