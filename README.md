CPSC 113: Optional Final Exam
A Small Web Application

For the final exam, we'd like you to write a small web application that passes a series of tests. There are three parts to the exam:

Write a web app that passes the tests
Deploy that to Heroku
Push your code to GitHub or git.yale.edu
Nothing should be too much of a surprise.

In order to receive any credit you must have a running Heroku app and a repo on GitHub or git.yale.edu with your code, so we suggest that this is one of the first things you do when starting the exam. Once you download the test code, you should be able to run it as described below.

Running the Testing Suite

Tests on the system can be run via a python script. It tests all the behaviors described in the next section. You can run the script by typing

python ./test.py YOUR_URL_HERE

into your terminal.

When you are developing your app, YOUR_APP_URL will likely point to localhost or to your Cloud9 app (make sure to put http before localhost or the test script will fail). Once you deploy your app to Heroku, you can test with your Heroku app's URL. The testing code does not have any external dependencies, so you can run it wherever there is an installation of Python 2.7 or above, including Cloud9.

The Tests

The tests shown in test.py are ordered from easiest to hardest for the most part. They are all worth equal points. Again, you must submit your code and a working Heroku app to receive any credit. That is so 1) we know you wrote code and 2) we can run the tests for your app. So, start with pushing to GitHub/git.yale.edu first and then pushing a "Hello World!" app to Heroku. Everything else descends from there.

Basic Functionality

The first three tests are simple in nature, and test your ability to write basic endpoint functionality.

A GET request to '/' produces an HTTP 200 response with content 'Hello World!' somewhere
A GET request to ''/robots.txt' produces a HTTP 200 response with Content-Type 'text/plain; charset=utf-8'"
A GET request to '/mrw/class-is-done.gif' 301 or 302 redirects to the reaction gif of your choice
Blog Post Functionality

Next, we want to mimic some functionality of a very minimal blog. We'll have you develop a few functions for creating a post, displaying a post, and deleting posts. Note that there is no need to have user accounts!

The way that users can view posts is by visiting /posts/:id, where :id starts at 0 and increments as a new post is created. So the first post created can be accessed via /posts/0 and the second can be accessed via /posts/1. If a post does not exist yet, visiting this page should return a 404 error.

New posts can be created from a form on the homepage.

The test script first checks to make sure that no posts exist. It then tests to make sure that new posts can be created and that the content can be rendered. Finally it tries to delete the created posts and tests that functionality.

The specific tests for the blog are as follows:

There should be no posts at first (checking '/posts/0' returns 404 status)
There should be no posts at first (checking '/posts/1' returns 404 status)
A POST request to '/posts/new' with form data containing a 'text' field creates a new post with id 0 and redirects to '/posts/0'
A GET request to /posts/0 contains the post content that was submitted and status code 200
A POST request to '/posts/new' with form data containing a 'text' field creates a new post with id 1 and redirects to '/posts/1
A GET request to /posts/1 contains the post content that was submitted and status code 200
A DELETE request to '/posts/delete' deletes all existing posts and responses w/ 200 status code
There should be no more posts (checking '/posts/0' returns 404 status)
Submitting the Exam

An assignment has been created on the course Web site. When you are done, please submit to https://cpsc113.som.yale.edu/assignments/optional-exam.

GOOD LUCK!