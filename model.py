"""Models and database functions for Ratings project."""
from flask_sqlalchemy import SQLAlchemy

from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session
#from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined

#from collections import defaultdict

# This is the connection to the PostgreSQL database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Model definitions

class Customer(db.Model):
    """Customer infomation"""

    __tablename__ = "customers"

    cust_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    gender_code = db.Column(db.String(8), db.ForeignKey('gender.gender_code'), nullable=False)
    phone_number = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    address = db.Column(db.String(256), nullable=False)
    city = db.Column(db.String(30), nullable=False)
    state = db.Column(db.String(8), nullable=False)
    zipcode = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Customer cust_id={} first_name={} last_name={}>".formate(self.cust_id, self.first_name, self.last_name)


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

        return "<User user_id={} first_name={} last_name={}>".formate(self.user_id, self.first_name, self.last_name)


class Gender(db.Model):
    """Gender type."""

    __tablename__ = "gender"

    gender_code = db.Column(db.String(8), primary_key=True)
    gender_name = db.Column(db.String(8))

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Gender gender_code={} gender_name={}>".formate(self.gender_code, self.gender_name)

    # # Define relationship to user
    # user = db.relationship("User",
    #                        backref=db.backref("ratings", order_by=rating_id))

    # # Define relationship to movie
    # movie = db.relationship("Movie",
    #                         backref=db.bacAkref("ratings", order_by=rating_id))

    # def __repr__(self):
    #     """Provide helpful representation when printed."""

    #     return "<Rating rating_id=%s movie_id=%s user_id=%s score=%s>" % (
    #         self.rating_id, self.movie_id, self.user_id, self.score)


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

 #   from server import app

    connect_to_db(app)
    print "Connected to DB."
