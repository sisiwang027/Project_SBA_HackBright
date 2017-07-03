"""Small Business Assistant."""

from jinja2 import StrictUndefined
from flask_debugtoolbar import DebugToolbarExtension
from flask import (Flask, render_template, redirect, request, flash,
                   session, jsonify, url_for, send_from_directory)
from model import (Gender, User, Customer, Category, CategoryAttribute, CategoryDetail,
                   Product, CategoryDetailValue, ProductDetail)
from model import connect_to_db, db, app

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
def upload_file():
    """Show upload page."""

    return render_template("upload_file.html")


@app.route("/upload_product", methods=["POST"])
def upload_purchase():
    """Upload purchase transactions."""

    file = request.files.get("fileToUpload")

    if not file:
        return "No Selected File!" + "\n" + "Please choose a file."
    elif file.content_type != "text/csv":
        return "Please upload a CSV file."
    else:
        i = 0
        for line in file:
            row = line.rstrip().split(",")
            for colum in row:
                colum = colum.strip()
            if i == 0:
                # read the title of CSV file.
                i += 1
                category_attr = row[4:]
                # read attributes of category
                for attr in category_attr:
                    # add attributes into category_attributes.
                    attr = attr.lower()
                    if CategoryAttribute.query.filter_by(attr_name=attr).first():
                        continue
                    else:
                        attrs = CategoryAttribute(attr_name=attr)
                        db.session.add(attrs)
            else:
                load_products(row, category_attr)

        return "Upload successfully!"


@app.route("/upload_sale", methods=["POST"])
def upload_sale():
    """Upload sale transactions."""

    pass


@app.route("/upload_category", methods=["POST"])
def upload_category():
    """Upload category information."""

    pass

###########################################################################
#useful functon


def load_products(rowlist, attr_list):
    """Load product file to five tables: products, category_detail_values,
    product_details, category_attributes, category_details."""

    cg = Category.query.filter_by(cg_name=rowlist[1].lower()).first()

    product = Product(user_id=session["user_id"],
                      prd_name=rowlist[0],
                      cg_id=cg.cg_id,
                      sale_price=rowlist[2],
                      description=rowlist[3])
    db.session.add(product)
    db.session.commit

    attr_val = rowlist[4:]
    val_list = []

    # read values of attributes.
    for i in range(0, len(attr_val)):

        attr = CategoryAttribute.query.filter_by(attr_name=attr_list[i]).first()

        attr_val[i] = attr_val[i].lower()

        # adding attribute-value pairs into category_attributes.
        val = CategoryDetailValue.query.filter_by(cg_attr_id=attr.cg_attr_id, attr_val=attr_val[i]).first()
        if val and attr_val[i] != '':
            val_list.append(val)

        elif val and attr_val[i] == '':
            continue

        elif not val and attr_val[i] != '':
            new_val = CategoryDetailValue(cg_attr_id=attr.cg_attr_id, attr_val=attr_val[i])
            db.session.add(new_val)
            val_list.append(new_val)

        # adding category-attribute pairs into category_attributes.
        if CategoryDetail.query.filter_by(cg_id=cg.cg_id, cg_attr_id=attr.cg_attr_id).first() or attr_val[i] == '':
            continue
        else:
            cg.cgattribute.append(attr)

    product.prddetail.extend(val_list)
    db.session.commit()


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    app.jinja_env.auto_reload = app.debug  # make sure templates, etc. are not cached in debug mode

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')
