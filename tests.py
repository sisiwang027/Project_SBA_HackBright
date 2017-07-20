# from selenium import webdriver
import unittest
from unittest import TestCase
from model import connect_to_db, db
from server import app
from flask import session
import server
from example_data import example_data


class FlaskTestsInSession(TestCase):

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'WANGSS'

        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_id'] = 1
                sess['first_name'] = 'sisi'

    def test_login(self):
        """Test login home page."""

        result = self.client.get("/")
        self.assertIn("Hi sisi!", result.data)

    def test_upload(self):
        """Test upload page."""

        result = self.client.get("/upload_product")
        self.assertIn("Select CSV file to upload:", result.data)


class FlaskTestsDatabase(TestCase):
    """Flask tests that use the database."""

    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()
        app.config['TESTING'] = True

        # Connect to test database
        connect_to_db(app, "postgresql:///testdb")

        # Create tables and add sample data
        db.create_all()
        example_data()

    def tearDown(self):
        """Do at end of every test."""

        db.session.close()
        db.drop_all()

    def test_login(self):
        """Test login page."""

        result = self.client.post("/login",
                                  data={"email": "wangss.wuhan@gmail.com", "password": "1111"},
                                  follow_redirects=True)
        self.assertIn("You have successfully logged in.", result.data)

    def test_notlogin(self):
        """Test wrong login page."""

        result = self.client.post("/login",
                                  data={"email": "wangss.wuhan@gmail.com", "password": "111"},
                                  follow_redirects=True)
        self.assertIn("Your information is incorrect.", result.data)

    def test_register(self):
        """Test registe successfully page."""

        result = self.client.post("/register",
                                  data={"email": "test_wangss.wuhan@gmail.com",
                                        "psw": "1111", "firstname": "testsisi",
                                        "lastname": "testwang"},
                                  follow_redirects=True)
        self.assertIn("You have successfully registered.", result.data)

    def test_duplicate_register(self):
        """Test registe unsuccessfully page."""

        result = self.client.post("/register",
                                  data={"email": "wangss.wuhan@gmail.com",
                                        "psw": "1111", "firstname": "testsisi",
                                        "lastname": "testwang"},
                                  follow_redirects=True)
        self.assertIn("Your email was already registered!", result.data)


class FlaskTestsNoSession(TestCase):
    """Test log in and log out."""

    def setUp(self):
        """Before every test"""

        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'WANGSS'
        self.client = app.test_client()

    def test_logout(self):
        """Test logout route."""

        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_id'] = 1

            result = self.client.get('/logout', follow_redirects=True)

            self.assertNotIn('user_id', session)
            self.assertIn('You have successfully logged out.', result.data)

    def test_register(self):
        """Test registe page."""

        result = self.client.get("/register", follow_redirects=True)
        self.assertIn("<h1>Register</h1>", result.data)

# class MyAppUnitTestCase(unittest.TestCase):

#     def test_adder(self):
#         assert arithmetic.adder(2, 3) == 5

if __name__ == "__main__":
    unittest.main()
