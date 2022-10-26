import unittest
from urllib import response
from app import app 
from app import fib

class flasktest(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/")
        statuscode = response.status_code
        self.assertEqual(statuscode,200)
    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get("/")
        self.assertEqual(response.content_type,"text/html; charset=utf-8")
    def test_index_data(self):
        tester = app.test_client(self)
        response = tester.get("/")
        print(response)
        self.assertTrue(b'Hello World' in response.data)

class Testfib(unittest.TestCase):
    def test_fib(self):
        self.assertEqual(fib(1),1)

if __name__ == "__main__":
   unittest.main()