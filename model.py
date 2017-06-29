"""Models and database functions for Ratings project."""
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, flash, redirect, session

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

#from collections import defaultdict

# This is the connection to the PostgreSQL database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Model definitions

class Gender(db.Model):
    """Gender type."""

    __tablename__ = "gender"

    gender_code = db.Column(db.String(8), primary_key=True)
    gender_name = db.Column(db.String(8))

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Gender gender_code={} gender_name={}>".format(self.gender_code, self.gender_name)


class User(db.Model):
    """User on ratings website."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<User user_id={} first_name={} last_name={}>".format(self.user_id, self.first_name, self.last_name)


class Customer(db.Model):
    """Customer infomation"""

    __tablename__ = "customers"

    cust_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    gender_code = db.Column(db.String(8), db.ForeignKey('gender.gender_code'), nullable=False)
    phone_number = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    birth_date = db.Column(db.Date)
    address = db.Column(db.String(256), nullable=False)
    city = db.Column(db.String(30), nullable=False)
    state = db.Column(db.String(8), nullable=False)
    zipcode = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Customer cust_id={} first_name={} last_name={}>".format(self.cust_id, self.first_name, self.last_name)


class Category(db.Model):
    """Categories of products."""

    __tablename__ = "categories"

    cg_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    cg_name = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Category category_id={} name={}>".format(self.cg_id, self.cg_name)


class Purchase(db.Model):
    """Purchases that users purchased and sale."""

    __tablename__ = "purchases"

    p_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    cg_id = db.Column(db.Integer, db.ForeignKey('categories.cg_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    purchase_at = db.Column(db.DateTime(), nullable=False)
    purchase_price = db.Column(db.Decimal(10, 2), nullable=False)
    sale_price = db.Column(db.Decimal(10, 2), nullable=False)
    quantities = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Purchase p_id={} user_id={}>".format(self.p_id, self.user_id)


class Sale(db.Model):
    """Purchases that users purchased and sale."""

    __tablename__ = "sales"

    s_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    cg_id = db.Column(db.Integer, db.ForeignKey('categories.cg_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    cust_id = db.Column(db.Integer, db.ForeignKey('customers.cust_id'), nullable=False)
    returned_flag = db.Column(db.Boolean, nullable=False)
    transc_at = db.Column(db.DateTime(), nullable=False)
    transc_price = db.Column(db.Decimal(10, 2), nullable=False)
    quantities = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Sale s_id={} user_id={} cust_id={}>".format(self.s_id, self.user_id, self.cust_id)


class CategoryDetailName(db.Model):
    """Description of product details."""

    __tablename__ = "category_detailname"

    cg_detailname_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    detailname = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<CategoryDetailName detail_name={}>".format(self.detailname)


class CategoryDetail(db.Model):
    """Products details."""

    __tablename__ = "category_details"

    cg_detail_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    cg_id = db.Column(db.Integer, db.ForeignKey('categories.cg_id'), nullable=False)
    cg_detailname_id = db.Column(db.Integer, db.ForeignKey('category_detailname.cg_detailname_id'), nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<CategoryDetail cg_id={} cg_detailname_id={}>".format(self.cg_id, self.cg_detailname_id)


class CategoryDetailValue(db.Model):
    """ The values of details of each categeory."""

    __tablename__ = "category_detail_values"

    cg_detailvalue_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    cg_detailname_id = db.Column(db.Integer, db.ForeignKey('category_detailname.cg_detailname_id'))
    detail_value = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<CategoryDetailValue cg_detailname_id={} detail_value={}>".format(self.cg_detailname_id, self.detail_value)


class TranscType(db.Model):
    """Transaction type name."""

    __tablename__ = 'transaction_type'

    transc_type = db.Column(db.String(8), autoincrement=True, primary_key=True)
    type_name = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<TranscType transc_type={} type_name={}>".format(self.transc_type, self.type_name)


class ProductDetail(db.Model):
    """Detail infomation of each prodect."""

    __tablename__ = "purchase_details"

    detail_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    transc_type = db.Column(db.String(8), db.ForeignKey("transaction_type.transc_type"), nullable=False)
    id = db.Column(db.Integer, db.ForeignKey("products.p_id"), autoincrement=True)
    cg_detailvalue_id = db.Column(db.Integer, db.ForeignKey("category_detail_values.cg_detailvalue_id"), autoincrement=True)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<ProductDetail p_id={} cg_detailvalue_id={}>".format(self.p_id, self.cg_detailvalue_id)




##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///sba'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app

    connect_to_db(app)
    print "Connected to DB."
