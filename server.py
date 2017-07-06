"""Small Business Assistant."""

from jinja2 import StrictUndefined
from flask_debugtoolbar import DebugToolbarExtension
from flask import (Flask, render_template, redirect, request, flash,
                   session, jsonify, url_for, send_from_directory)
from model import (Gender, User, Customer, Category, CategoryAttribute, CategoryDetail,
                   Product, CategoryDetailValue, ProductDetail)
from model import connect_to_db, db, app
from loadCSVfile import load_csv_product, add_category

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "WANGSS"


# Normally, if you use an undefined variable in Jinja2, it fails
# silently. This is horrible. Fix this so that, instead, it raises an
# error.
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage."""

    return render_template("home.html")


@app.route("/register", methods=["GET"])
def register_form():
    """Show registration form."""

    return render_template("register.html")


@app.route("/register", methods=["POST"])
def register_process():
    """Submit registration form."""

    email = request.form.get("email")
    password = request.form.get("psw")
    lastname = request.form.get("lastname")
    firstname = request.form.get("firstname")

    if User.query.filter_by(email=email).count() == 0:

        new_user = User(email=email, password=password, first_name=firstname, last_name=lastname)
        db.session.add(new_user)
        db.session.commit()
        flash('You have successfully registered')

        return redirect("/")

    else:
        flash('Your email was already registered!')

        return redirect("/register")


@app.route("/login", methods=["GET"])
def login():
    """Show login form."""

    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login_process():
    """User log in."""

    email = request.form.get("email")
    password = request.form.get("password")

    u_login = User.query.filter_by(email=email).first()

    if u_login.password == password:

        session["user_id"] = u_login.user_id
        session["first_name"] = u_login.first_name

        flash('You have successfully logged in.')

        return redirect("/")  # if user login, show user's data. url_for(".class", user_id=u_login.user_id)

    else:
        flash('Your information is incorrect')

        return redirect("/login")


@app.route("/logout", methods=["GET"])
def logout_process():
    """User logs out."""

    session.pop('user_id', None)
    flash('You have successfully logged out.')
    return redirect("/")


@app.route("/upload_product")
def upload_product():
    """Show upload page."""

    return render_template("upload_file.html")


@app.route("/upload_product", methods=["POST"])
def upload_product_process():
    """Upload purchase transactions."""

    file = request.files.get("fileToUpload")

    return load_csv_product(file)


@app.route("/add_category")
def add_category_form():
    """Show form of adding categories."""

    return render_template("add_category.html")


@app.route("/add_category", methods=["POST"])
def add_category_process():
    """adding category to table categories."""

    cg_name = request.form.get("cg")

    return add_category(cg_name)


@app.route("/add_product")
def add_product_form():
    """Show form of adding products."""

    categories = Category.query.all()

    return render_template("add_product.html", categories=categories)
    # render_template("add_product.html", categories)


@app.route("/add_product", methods=["POST"])
def add_product_process():
    """adding category to table categories."""

    category = request.form.get("category")
    productname = request.form.get("productname")
    saleprice = request.form.get("saleprice")
    description == request.form.get("description")

    pass

    # return add_product_to_table()


# @app.route("/upload_sale", methods=["POST"])
# def upload_sale():
#     """Upload sale transactions."""

#     pass


# @app.route("/upload_category", methods=["POST"])
# def upload_category():
#     """Upload category information."""

#     pass

###########################################################################
#useful functon





if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    app.jinja_env.auto_reload = app.debug  # make sure templates, etc. are not cached in debug mode

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')
