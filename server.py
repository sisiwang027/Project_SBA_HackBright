"""Small Business Assistant."""

from jinja2 import StrictUndefined
from flask_debugtoolbar import DebugToolbarExtension
from flask import (Flask, render_template, redirect, request, flash,
                   session, jsonify, url_for, send_from_directory)
from model import (Gender, User, Customer, Category, CategoryAttribute, CategoryDetail,
                   Product, CategoryDetailValue, ProductDetail, Sale, Purchase)
from model import connect_to_db, db, app
from loadCSVfile import load_csv_product
from add_datato_db import add_category, add_product_to_table, add_attr_to_table
from report_result import show_sal_qtychart_json, sale_sum_report, prod_sum_report, show_sal_revenuechart_json, show_sal_profitchart_json, show_prodchart_json, prod_sum_report, show_top10_prod_json
from report import show_table, show_test_table
from sqlalchemy.sql.functions import coalesce
from dateutil.relativedelta import relativedelta
from datetime import datetime
import json

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


@app.route("/add_product", methods=["POST"])
def add_product_process():
    """adding category to table categories."""

    attr_val = []
    attr_name = []

    category = request.form.get("cg")
    productname = request.form.get("pname")
    saleprice = request.form.get("sprice")
    description = request.form.get("pdescription")
    attr_num = request.form.get("attr_num")

    for i in range(1, int(attr_num) + 1):
        if request.form.get("attrname" + str(i)):
            attr_name.append(request.form.get("attrname" + str(i)))
            attr_val.append(request.form.get("attrvalue" + str(i)))

    one_product = [productname, category, float(saleprice), description] + attr_val

    print one_product, attr_name

    add_attr_to_table(attr_name)

    return add_product_to_table(one_product, attr_name)


@app.route("/show_report")
def show_report():
    """show reports"""

    table = show_table()

    return render_template("report.html", table=table)


@app.route("/product")
def show_product():
    """show products"""

    user_id = session.get("user_id")

    purch = db.session.query(Product.prd_id, Product.user_id, Product.prd_name, Product.cg_id, Category.cg_name, Product.sale_price, Product.description, db.func.sum(coalesce(Purchase.quantities, 0)).label("purch_qty"), db.func.sum(coalesce(Purchase.quantities * Purchase.purchase_price, 0)).label("purch_price_sum")).outerjoin(Purchase).outerjoin(Category).filter(Product.user_id == user_id).group_by(Product.prd_id, Product.user_id, Product.prd_name, Product.cg_id, Category.cg_name, Product.sale_price, Product.description).order_by(Product.prd_id).subquery()

    products = db.session.query(purch.c.prd_id, purch.c.user_id, purch.c.prd_name, purch.c.cg_id, purch.c.cg_name, purch.c.sale_price, purch.c.description, purch.c.purch_qty, purch.c.purch_price_sum, db.func.sum(coalesce(Sale.quantities, 0)).label("sale_qty"), db.func.sum(coalesce(Sale.quantities * Sale.transc_price, 0)).label("sale_price_sum")).outerjoin(Sale, purch.c.prd_id == Sale.prd_id).group_by(purch.c.prd_id, purch.c.user_id, purch.c.prd_name, purch.c.cg_id, purch.c.cg_name, purch.c.sale_price, purch.c.description, purch.c.purch_qty, purch.c.purch_price_sum).order_by(purch.c.prd_id).all()

    return render_template("product.html", products=products)


@app.route("/product_detail/<int:prd_id>", methods=['GET'])
def show_product_detail(prd_id):
    """Show details of movie."""

    product = Product.query.get(prd_id)

    prd_details = product.prddetail

    return render_template("product_detail.html", prd_details=prd_details, product=product)


@app.route("/purchase/<int:prd_id>", methods=['GET'])
def show_purchase(prd_id):
    """Show details of movie."""

    product = Product.query.get(prd_id)

    purchases = product.purchases

    total_pur_price = db.session.query(db.func.sum(Purchase.purchase_price).label("total"))\
                                .filter(Product.prd_id == 1).one()

    return render_template("purchase.html", purchases=purchases, product=product, total_pur_price=total_pur_price)


@app.route("/sale/<int:prd_id>", methods=['GET'])
def show_sale(prd_id):
    """Show details of movie."""

    product = Product.query.get(prd_id)

    sales = product.sales

    return render_template("sale.html", sales=sales, product=product)


@app.route("/product_sum")
def show_product_sum():
    """Show sumarizing information of products."""

    user_id = session.get("user_id")

    return render_template("product_sum.html")


@app.route("/product_sum.json", methods=['GET'])
def sent_product_sum():
    """Show sumarizing information of sales."""

    user_id = session.get("user_id")

    month_num = request.args.get("months")

    attr_list = ['gap', 'nike']

    result = prod_sum_report(user_id, attr_list, month_num)

    return jsonify(result)


@app.route('/prod_pichart.json')
def show_product_chart():
    """Return sale quantities data as json."""

    user_id = session.get("user_id")

    month_num = request.args.get("months")

    attr_list = ['gap', 'nike']

    data_dict = show_prodchart_json(user_id, month_num, attr_list)

    return jsonify(data_dict)


@app.route('/top_prod_barchart.json')
def show_topproduct_chart():
    """Return sale quantities data as json."""

    user_id = session.get("user_id")

    month_num = request.args.get("months")

    attr_list = ['gap', 'nike']

    data_dict = show_top10_prod_json(user_id, month_num, attr_list)

    return jsonify(data_dict)


@app.route("/sale_sum")
def show_sale_sum():
    """Show sumarizing information of sales."""

    user_id = session.get("user_id")

    return render_template("sale_sum.html")


@app.route("/sale_sum.json", methods=['GET'])
def sent_sale_sum():
    """Show sumarizing information of sales."""

    user_id = session.get("user_id")

    month_num = int(request.args.get("months"))

    attr_list = ['gap', 'nike']

    result = sale_sum_report(user_id, attr_list, month_num)

    return jsonify(result)


@app.route('/sale-qty-linechart.json')
def show_sale_qty_chart():
    """Return sale quantities data as json."""

    user_id = session.get("user_id")

    month_num = int(request.args.get("months"))

    attr_list = ['gap', 'nike']

    data_dict = show_sal_qtychart_json(user_id, month_num, attr_list)

    return jsonify(data_dict)


@app.route('/sale-revenue-linechart.json')
def show_sale_revenue_chart():
    """Return sale revenue data as json."""

    user_id = session.get("user_id")

    month_num = int(request.args.get("months"))

    attr_list = ['gap', 'nike']

    data_dict = show_sal_revenuechart_json(user_id, month_num, attr_list)

    return jsonify(data_dict)


@app.route('/sale-profit-linechart.json')
def show_sale_profit_chart():
    """Return sale profit data as json."""

    user_id = session.get("user_id")

    month_num = int(request.args.get("months"))

    attr_list = ['gap', 'nike']

    data_dict = show_sal_profitchart_json(user_id, month_num, attr_list)

    return jsonify(data_dict)



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
