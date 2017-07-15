
from jinja2 import StrictUndefined
from flask_debugtoolbar import DebugToolbarExtension
from flask import (Flask, render_template, redirect, request, flash,
                   session, jsonify, url_for, send_from_directory)
from model import (Gender, User, Customer, Category, CategoryAttribute, CategoryDetail,
                   Product, CategoryDetailValue, ProductDetail, Sale, Purchase)
from model import connect_to_db, db, app
from loadCSVfile import load_csv_product, add_category, add_product_to_table, add_attr_to_table
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


def display_salesum_json (month_num, attr_list, user_id):
    """Show sale sumarizing data as jason"""

    result = {}

    set_date = datetime.now().date() - relativedelta(months=month_num)
    sale = db.session.query(db.func.date_part('year', Sale.transc_at).label("year_at"), db.func.date_part('month', Sale.transc_at).label("month_at"), Sale.prd_id, db.func.sum(Sale.transc_price * Sale.quantities).label("revenue"), db.func.sum(Sale.quantities).label("sale_qty")).filter(Sale.transc_at >= set_date).group_by(db.func.date_part('year', Sale.transc_at).label("year_at"), db.func.date_part('month', Sale.transc_at).label("month_at"), Sale.prd_id).subquery()

    purch_cost = db.session.query(Purchase.prd_id, db.func.round((db.func.sum(Purchase.purchase_price * Purchase.quantities) / db.func.sum(Purchase.quantities)), 2).label("avg_purch_cost")).group_by(Purchase.prd_id).subquery()

    prod = db.session.query(Product.prd_id, Product.cg_id, Category.cg_name).join(Category).join(Product.prddetail).filter(CategoryDetailValue.attr_val.in_(attr_list), Product.user_id == user_id).group_by(Product.prd_id, Product.cg_id, Category.cg_name).subquery()

    sale_sum = db.session.query((sale.c.year_at * 100 + sale.c.month_at).label("sale_at"), prod.c.cg_name, db.func.sum(db.func.round(sale.c.sale_qty)).label("sale_qty"), db.func.sum(sale.c.revenue).label("revenue"), db.func.sum(sale.c.revenue - purch_cost.c.avg_purch_cost * sale.c.sale_qty).label("profit")).join(purch_cost, sale.c.prd_id == purch_cost.c.prd_id).join(prod, sale.c.prd_id == prod.c.prd_id).group_by((sale.c.year_at * 100 + sale.c.month_at).label("sale_at"), prod.c.cg_name).order_by((sale.c.year_at * 100 + sale.c.month_at).label("sale_at"), prod.c.cg_name)

    column_name = [column["name"] for column in sale_sum.column_descriptions]

    result["result"] = [dict(zip(column_name, data)) for data in sale_sum]

    return jsonify(result)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    app.jinja_env.auto_reload = app.debug  # make sure templates, etc. are not cached in debug mode

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    display_salesum_json(12, ['gap', 'nike'], 1)



