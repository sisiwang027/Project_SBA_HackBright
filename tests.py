from selenium import webdriver
import unittest
from unittest import TestCase
from model import Employee, Department, connect_to_db, db, example_data
from server import app
import server

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://localhost:5000/')
        self.assertEqual(self.browser.title, 'UberCalc')

    def test_math(self):
        self.browser.get('http://localhost:5000/')

        x = self.browser.find_element_by_id('x-field')
        x.send_keys("3")
        y = self.browser.find_element_by_id('y-field')
        y.send_keys("4")

        btn = self.browser.find_element_by_id('calc-button')
        btn.click()

        result = self.browser.find_element_by_id('result')
        self.assertEqual(result.text, "7")





class FlaskTests(TestCase):
    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()

        # Show Flask errors that happen during tests
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

    def test_find_employee(self):
        """Can we find an employee in the sample data?"""

        leonard = Employee.query.filter(Employee.name == "Leonard").first()
        self.assertEqual(leonard.name, "Leonard")

    def test_emps_by_state(self):
        """Find employees in a state."""

        result = self.client.get("/emps-by-state?state=California")

        self.assertIn("Nadine", result.data)


class MockFlaskTests(TestCase):
    """Flask tests that show off mocking."""

    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True

        # Connect to test database
        connect_to_db(app, "postgresql:///testdb")

        # Create tables and add sample data
        db.create_all()
        example_data()

        # Make mock
        def _mock_state_to_code(state_name):
            return "CA"

        server.state_to_code = _mock_state_to_code

    def tearDown(self):
        """Do at end of every test."""

        db.session.close()
        db.drop_all()

    def test_emps_by_state_with_mock(self):
        """Find employees in a state."""

        result = self.client.get('/emps-by-state?state=California')
        self.assertIn("Nadine", result.data)


if __name__ == "__main__":
    unittest.main()
