"""Models and database functions for Ratings project."""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import UniqueConstraint
from flask import Flask

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "WANGSS"

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
    gender_name = db.Column(db.String(8), unique=True)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Gender gender_code={} gender_name={}>".format(self.gender_code, self.gender_name)


class User(db.Model):
    """User on ratings website."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
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
    cg_name = db.Column(db.String(30), unique=True, nullable=False)

    cgattribute = db.relationship("CategoryAttribute",
                                  secondary="category_details",
                                  backref="categories")

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Category category_id={} name={}>".format(self.cg_id, self.cg_name)


class CategoryAttribute(db.Model):
    """Description of product details."""

    __tablename__ = "category_attributes"

    cg_attr_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    attr_name = db.Column(db.String(30), nullable=False, unique=True)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<CategoryAttribute attribute_name={}>".format(self.attr_name)


class CategoryDetail(db.Model):
    """Assossiation table bteween cagegories and category_attributes."""

    __tablename__ = "category_details"

    cg_detail_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    cg_id = db.Column(db.Integer, db.ForeignKey('categories.cg_id'), nullable=False)
    cg_attr_id = db.Column(db.Integer, db.ForeignKey('category_attributes.cg_attr_id'), nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<CategoryDetail cg_id={} cg_attr_id={}>".format(self.cg_id, self.cg_attr_id)


class Product(db.Model):
    """Products infomation."""

    __tablename__ = "products"

    prd_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    prd_name = db.Column(db.String(80))
    cg_id = db.Column(db.Integer, db.ForeignKey('categories.cg_id'), nullable=False)
    sale_price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(256))

    __table_args__ = (UniqueConstraint('user_id', 'prd_name', name='_user_product'),)

    prddetail = db.relationship("CategoryDetailValue",
                                secondary="product_details",
                                backref="products")

    prdcg = db.relationship("Category",
                            backref="products")

    def __reper__(self):
        """Provide helpful representation when printed."""

        return "<Product prd_id={} prd_name={}>".format(self.prd_id, self.prd_name)


class CategoryDetailValue(db.Model):
    """ The values of details of each categeory."""

    __tablename__ = "category_detail_values"

    cg_detailvalue_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    cg_attr_id = db.Column(db.Integer, db.ForeignKey('category_attributes.cg_attr_id'))
    attr_val = db.Column(db.String(80), nullable=False)

    attributeval = db.relationship("CategoryAttribute",
                                   backref="category_detail_values")

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<CategoryDetailValue cg_attr_id={} detail_value={}>".format(self.cg_attr_id, self.attr_val)


class ProductDetail(db.Model):
    """Detail infomation of each prodect, it's an assosiation table connecting products and category_detail_values."""

    __tablename__ = "product_details"

    detail_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    prd_id = db.Column(db.Integer, db.ForeignKey("products.prd_id"), nullable=False)
    cg_detailvalue_id = db.Column(db.Integer, db.ForeignKey("category_detail_values.cg_detailvalue_id"), nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<PurchaseCgDetail p_id={} cg_detailvalue_id={}>".format(self.p_id, self.cg_detailvalue_id)


class Purchase(db.Model):
    """Purchases that users purchased and sale."""

    __tablename__ = "purchases"

    purch_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    prd_id = db.Column(db.Integer, db.ForeignKey('products.prd_id'), nullable=False)
    purchase_at = db.Column(db.DateTime(), nullable=False)
    purchase_price = db.Column(db.Float, nullable=False)
    quantities = db.Column(db.Integer, nullable=False)

    purchasePrd = db.relationship("Product",
                                  backref="purchases")

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Purchase purch_id={} prd_id={}>".format(self.purch_id, self.prd_id)


class Sale(db.Model):
    """Purchases that users purchased and sale."""

    __tablename__ = "sales"

    transc_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    cust_id = db.Column(db.Integer, db.ForeignKey('customers.cust_id'), nullable=False)
    prd_id = db.Column(db.Integer, db.ForeignKey('products.prd_id'), nullable=False)
    returned_flag = db.Column(db.Boolean, nullable=False)
    transc_at = db.Column(db.DateTime(), nullable=False)
    transc_price = db.Column(db.Float, nullable=False)
    quantities = db.Column(db.Integer, nullable=False)

    salePrd = db.relationship("Product",
                              backref="sales")

    custs = db.relationship("Customer",
                            backref="sales")

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Sale transc_id={} cust_id={} prd_id={}>".format(self.transc_id, self.cust_id, self.prd_id)


def connect_to_db(app, db_uri='postgresql:///sba'):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    #from server import app

    connect_to_db(app)
    print "Connected to DB."
