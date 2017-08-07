# from selenium import webdriver
import unittest
from unittest import TestCase
from model import connect_to_db, db
from server import app
from flask import session
from example_data import example_data
from loadCSVfile import return_result, load_csv
from add_datato_db import add_file_to_db, add_transc_to_table, add_attr_to_table, add_product_to_table, add_category
from report_result import (sql_to_linechartejson, show_sal_qtychart_json,
                           show_sal_revenuechart_json, show_sal_profitchart_json,
                           sale_sum_report, prod_sum_report, sql_to_pichartejson,
                           show_prodchart_json, sql_to_barchartejson, show_top10_prod_json,
                           sql_to_cust_barchartejson, show_cust_age_json)


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

        result = self.client.get("/upload_csvfile")
        self.assertIn("Select CSV file to upload:", result.data)

    def test_category(self):
        """Test adding category to table categories."""

        result = self.client.get("/add_category")
        self.assertIn("Add a New Category:", result.data)


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

    def test_product_list(self):
        """Test adding category to table categories."""

        result = self.client.get("/product")
        self.assertIn("Product List", result.data)

    def test_product(self):
        """Test adding product to five different table."""

        result = self.client.get("/add_product")
        self.assertIn("Attribute Name:", result.data)

    def test_product_sum(self):
        """Test adding product to five different table."""

        self.client = app.test_client()
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'WANGSS'

        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_id'] = 1
                sess['first_name'] = 'sisi'

        result = self.client.get("/product_sum")
        self.assertIn("Product Sumary Report", result.data)

    def test_product_detail(self):
        """Test show details of each product."""

        self.client = app.test_client()
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'WANGSS'

        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_id'] = 1
                sess['first_name'] = 'sisi'

        result = self.client.get("/product_detail/1")
        self.assertIn("nikeshoes", result.data)

    def test_purchase_detail(self):
        """Test show details of purchases transcations of one product."""

        self.client = app.test_client()
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'WANGSS'

        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_id'] = 1
                sess['first_name'] = 'sisi'

        result = self.client.get("/purchase/1")
        self.assertIn("nikeshoes", result.data)

    def test_sale_detail(self):
        """Test show details of sales transcations of one product."""

        self.client = app.test_client()
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'WANGSS'

        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_id'] = 1
                sess['first_name'] = 'sisi'

        result = self.client.get("/sale/1")
        self.assertIn("nikeshoes", result.data)

    def test_sale_sum(self):
        """Test show details of purchases transcations of one product."""

        self.client = app.test_client()
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'WANGSS'

        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_id'] = 1
                sess['first_name'] = 'sisi'

        result = self.client.get("/sale_sum")
        self.assertIn("Show Data in the Past", result.data)

    def test_category(self):
        """Test adding category to table categories."""

        self.client = app.test_client()
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'WANGSS'

        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_id'] = 1
                sess['first_name'] = 'sisi'

        result = self.client.post("/add_category",
                                  data={"cg": "bags"},
                                  follow_redirects=True)
        self.assertIn("successfully", result.data)

    def test_add_product(self):
        """Test adding category to table categories."""

        self.client = app.test_client()
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'WANGSS'

        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_id'] = 1
                sess['first_name'] = 'sisi'

        result = self.client.post("/add_product",
                                  data={"cg": "shoes",
                                        "pname": "nikeshoestest",
                                        "sprice": 180.99,
                                        "pdescription": "test",
                                        "attr_num": 1,
                                        "attrname1": "brand",
                                        "attrvalue1": "nike"},
                                  follow_redirects=True)
        self.assertIn("successfully", result.data)

    def test_add_file_to_db(self):
        """Test function add_file_to_db."""

        assert add_file_to_db(["ww@gmail.com", "nikeshoes", "f", "2017-07-01", "180", "1"], "s") is None

    def test_add_transc_to_table(self):
        """Test add_transc_to_table function."""

        assert add_transc_to_table(["ww@gmail.com", "nikeshoes", "f", "2017-01-01", 180.00, 1], "sales") == "Submit successfully!"

    def test_add_attr_to_table(self):
        """Test function add_attr_to_table."""

        assert add_attr_to_table(["brand"]) is True

    def test_add_product_to_table(self):
        """Test function add_product_to_table."""

        self.client = app.test_client()
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'WANGSS'

        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_id'] = 1

        assert add_product_to_table(["nikeshoes_test", "shoes", 78.99, "test", "nike"], ["brand"]) == "Submit successfully!"

    def test_add_category(self):
        """Test function add_category."""

        assert add_category("bags") == "The category has been successfully added."


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


class MyAppUnitTestCase(unittest.TestCase):
    """Test functions."""

    def test_return_result(self):
        """Test function return_result."""

        assert return_result(["fail", "Submit successfully!", "Submit successfully!"]) == "2 rows uploaded successfully, 1 rows unsuccessfully! These row numbers failed: 1 !"

    def test_load_csv(self):
        """Test function load_csv."""

        assert "No Selected File!" in load_csv(None)

    def test_sql_to_linechartejson(self):
        """Test function sql_to_linechartejson."""

        options = {"title": {"display": True, "text": "Sales Chart"}, "responsive": True}

        data_set1 = {"fill": True,
                "lineTension": 0.5,
                "backgroundColor": "rgba(220,220,220,0.2)",
                "borderCapStyle": 'butt',
                "borderDash": [],
                "borderDashOffset": 0.0,
                "borderJoinStyle": 'miter',
                "pointBorderColor": "rgba(220,220,220,1)",
                "pointBackgroundColor": "#fff",
                "pointBorderWidth": 1,
                "pointHoverRadius": 5,
                "pointHoverBackgroundColor": "#fff",
                "pointHoverBorderColor": "rgba(220,220,220,1)",
                "pointHoverBorderWidth": 2,
                "pointRadius": 3,
                "pointHitRadius": 10,
                "spanGaps": False,
                "label": "shoes",
                "data": [100, 100],
                "borderColor": "#ffb366"}

        data_dict = {"labels": ["201707", "201706"], "datasets": [data_set1]}

        assert sql_to_linechartejson([("201707", "shoes", 100), ("201706", "shoes", 100)], "Sales Chart") == {"type": "line", "options": options, "data": data_dict}

    # def test_(self):
    #     """Test function ."""

    #     assert () ==

    # def test_(self):
    #     """Test function ."""

    #     assert () ==


if __name__ == "__main__":
    unittest.main()
