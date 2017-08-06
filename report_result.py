"""Get the result of reports and return json"""

from flask import (Flask, render_template, redirect, request, flash,
                   session, jsonify, url_for, send_from_directory)
from model import (Gender, User, Customer, Category, CategoryAttribute, CategoryDetail,
                   Product, CategoryDetailValue, ProductDetail,  Sale, Purchase)
from model import connect_to_db, db, app
from datetime import datetime
from sqlalchemy.sql.functions import coalesce
from dateutil.relativedelta import relativedelta


def sql_to_linechartejson(sqlalchemy_list, chart_title):
    """Change the result of sqlalchemy to linecharte json"""

    data_dict = {}
    data_dict["labels"] = []
    data_dict["datasets"] = []
    cg_qty_dic = {}
    color_list = ["#ffb366", "rgba(102,204,255,1)", "#66ff66", "#99b3e6"]
    clor_choose = 0

    for time_at, cg_name, qty in sqlalchemy_list:
        time_at = str(int(time_at))
        cg_name = str(cg_name)

        if time_at not in data_dict["labels"]:
            data_dict["labels"].append(time_at)

        cg_qty_dic.setdefault(cg_name, []).append(qty)

    for cg_name in cg_qty_dic:

        data_set = {"fill": True,
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
                "spanGaps": False}

        data_set["label"] = cg_name
        data_set["data"] = cg_qty_dic[cg_name]
        data_set["borderColor"] = color_list[clor_choose]
        clor_choose += 1

        data_dict["datasets"].append(data_set)

    options = {"title": {"display": True, "text": chart_title}, "responsive": True}
    data_chart = {"type": "line", "options": options, "data": data_dict}

    return data_chart


def show_sal_qtychart_json(user_id, month_num, attr_list):
    """show sale quantities chart data as a json"""

    firstday_month = "01{}{}".format(str(datetime.now().month), str(datetime.now().year))

    set_date = datetime.strptime(firstday_month, "%d%m%Y").date() - relativedelta(months=month_num-1)

    sale = db.session.query(db.func.date_part('year', Sale.transc_at).label("year_at"), db.func.date_part('month', Sale.transc_at).label("month_at"), Sale.prd_id, db.func.sum(Sale.transc_price * Sale.quantities).label("revenue"), db.func.sum(Sale.quantities).label("sale_qty")).filter(Sale.transc_at >= set_date).group_by(db.func.date_part('year', Sale.transc_at).label("year_at"), db.func.date_part('month', Sale.transc_at).label("month_at"), Sale.prd_id).subquery()

    purch_cost = db.session.query(Purchase.prd_id, (db.func.sum(Purchase.purchase_price * Purchase.quantities) / db.func.sum(Purchase.quantities)).label("avg_purch_cost")).group_by(Purchase.prd_id).subquery()

    prod = db.session.query(Product.prd_id, Product.cg_id, Category.cg_name).join(Category).join(Product.prddetail).filter(CategoryDetailValue.attr_val.in_(attr_list), Product.user_id == user_id).group_by(Product.prd_id, Product.cg_id, Category.cg_name).subquery()

    sale_qty_sum = db.session.query((sale.c.year_at * 100 + sale.c.month_at).label("sale_at"),\
                                    prod.c.cg_name,\
                                    db.func.sum(db.func.round(sale.c.sale_qty)).label("sale_qty"))\
                   .join(purch_cost, sale.c.prd_id == purch_cost.c.prd_id)\
                   .join(prod, sale.c.prd_id == prod.c.prd_id)\
                   .group_by((sale.c.year_at * 100 + sale.c.month_at).label("sale_at"),\
                             prod.c.cg_name).order_by((sale.c.year_at * 100 + sale.c.month_at).label("sale_at"), prod.c.cg_name)\
                   .all()

    return sql_to_linechartejson(sale_qty_sum, "Qty Chart")


def show_sal_revenuechart_json(user_id, month_num, attr_list):
    """show sale revenue chart data as a json"""

    firstday_month = "01{}{}".format(str(datetime.now().month), str(datetime.now().year))

    set_date = datetime.strptime(firstday_month, "%d%m%Y").date() - relativedelta(months=month_num-1)

    sale = db.session.query(db.func.date_part('year', Sale.transc_at).label("year_at"),\
                            db.func.date_part('month', Sale.transc_at).label("month_at"), Sale.prd_id,\
                            db.func.sum(Sale.transc_price * Sale.quantities).label("revenue"),\
                            db.func.sum(Sale.quantities).label("sale_qty")).filter(Sale.transc_at >= set_date)\
                        .group_by(db.func.date_part('year', Sale.transc_at).label("year_at"), db.func.date_part('month', Sale.transc_at).label("month_at"), Sale.prd_id).subquery()

    purch_cost = db.session.query(Purchase.prd_id,\
                                  (db.func.sum(Purchase.purchase_price * Purchase.quantities) / db.func.sum(Purchase.quantities)).label("avg_purch_cost"))\
                           .group_by(Purchase.prd_id).subquery()

    prod = db.session.query(Product.prd_id, Product.cg_id, Category.cg_name)\
                     .join(Category).join(Product.prddetail)\
                     .filter(CategoryDetailValue.attr_val.in_(attr_list), Product.user_id == user_id)\
                     .group_by(Product.prd_id, Product.cg_id, Category.cg_name).subquery()

    sale_revenue_sum = db.session.query((sale.c.year_at * 100 + sale.c.month_at).label("sale_at"),\
                                    prod.c.cg_name,\
                                    db.func.sum(sale.c.revenue).label("revenue"))\
                   .join(purch_cost, sale.c.prd_id == purch_cost.c.prd_id)\
                   .join(prod, sale.c.prd_id == prod.c.prd_id)\
                   .group_by((sale.c.year_at * 100 + sale.c.month_at).label("sale_at"),\
                             prod.c.cg_name).order_by((sale.c.year_at * 100 + sale.c.month_at).label("sale_at"), prod.c.cg_name)\
                   .all()

    return sql_to_linechartejson(sale_revenue_sum, "Revenue Chart")


def show_sal_profitchart_json(user_id, month_num, attr_list):
    """show sale profit chart data as a json"""

    firstday_month = "01{}{}".format(str(datetime.now().month), str(datetime.now().year))

    set_date = datetime.strptime(firstday_month, "%d%m%Y").date() - relativedelta(months=month_num-1)

    sale = db.session.query(db.func.date_part('year', Sale.transc_at).label("year_at"),\
                            db.func.date_part('month', Sale.transc_at).label("month_at"), Sale.prd_id,\
                            db.func.sum(Sale.transc_price * Sale.quantities).label("revenue"),\
                            db.func.sum(Sale.quantities).label("sale_qty")).filter(Sale.transc_at >= set_date)\
                        .group_by(db.func.date_part('year', Sale.transc_at).label("year_at"), db.func.date_part('month', Sale.transc_at).label("month_at"), Sale.prd_id).subquery()

    purch_cost = db.session.query(Purchase.prd_id,\
                                  (db.func.sum(Purchase.purchase_price * Purchase.quantities) / db.func.sum(Purchase.quantities)).label("avg_purch_cost"))\
                           .group_by(Purchase.prd_id).subquery()

    prod = db.session.query(Product.prd_id, Product.cg_id, Category.cg_name)\
                     .join(Category).join(Product.prddetail)\
                     .filter(CategoryDetailValue.attr_val.in_(attr_list), Product.user_id == user_id)\
                     .group_by(Product.prd_id, Product.cg_id, Category.cg_name).subquery()

    sale_profit_sum = db.session.query((sale.c.year_at * 100 + sale.c.month_at).label("sale_at"),\
                                    prod.c.cg_name,\
                                    db.func.sum(sale.c.revenue - purch_cost.c.avg_purch_cost * sale.c.sale_qty).label("profit"))\
                   .join(purch_cost, sale.c.prd_id == purch_cost.c.prd_id)\
                   .join(prod, sale.c.prd_id == prod.c.prd_id)\
                   .group_by((sale.c.year_at * 100 + sale.c.month_at).label("sale_at"),\
                             prod.c.cg_name).order_by((sale.c.year_at * 100 + sale.c.month_at).label("sale_at"), prod.c.cg_name)\
                   .all()

    return sql_to_linechartejson(sale_profit_sum, "Profit Chart")


def sale_sum_report(user_id, attr_list, month_num):
    """Return data of Sale Sum Report."""
    result = {}

    firstday_month = "01{}{}".format(str(datetime.now().month), str(datetime.now().year))

    set_date = datetime.strptime(firstday_month, "%d%m%Y").date() - relativedelta(months=month_num-1)

    sale = db.session.query(db.func.date_part('year', Sale.transc_at).label("year_at"), db.func.date_part('month', Sale.transc_at).label("month_at"), Sale.prd_id, db.func.sum(Sale.transc_price * Sale.quantities).label("revenue"), db.func.sum(Sale.quantities).label("sale_qty")).filter(Sale.transc_at >= set_date).group_by(db.func.date_part('year', Sale.transc_at).label("year_at"), db.func.date_part('month', Sale.transc_at).label("month_at"), Sale.prd_id).subquery()

    purch_cost = db.session.query(Purchase.prd_id, (db.func.sum(Purchase.purchase_price * Purchase.quantities) / db.func.sum(Purchase.quantities)).label("avg_purch_cost")).group_by(Purchase.prd_id).subquery()

    prod = db.session.query(Product.prd_id, Product.cg_id, Category.cg_name).join(Category).join(Product.prddetail).filter(CategoryDetailValue.attr_val.in_(attr_list), Product.user_id == user_id).group_by(Product.prd_id, Product.cg_id, Category.cg_name).subquery()

    sale_sum = db.session.query((sale.c.year_at * 100 + sale.c.month_at).label("sale_at"), prod.c.cg_name, db.func.sum(db.func.round(sale.c.sale_qty)).label("sale_qty"), db.func.sum(sale.c.revenue).label("revenue"), db.func.sum(sale.c.revenue - purch_cost.c.avg_purch_cost * sale.c.sale_qty).label("profit")).join(purch_cost, sale.c.prd_id == purch_cost.c.prd_id).join(prod, sale.c.prd_id == prod.c.prd_id).group_by((sale.c.year_at * 100 + sale.c.month_at).label("sale_at"), prod.c.cg_name).order_by((sale.c.year_at * 100 + sale.c.month_at).label("sale_at"), prod.c.cg_name)

    column_name = [column["name"] for column in sale_sum.column_descriptions]

    result["result"] = [dict(zip(column_name, data)) for data in sale_sum]

    return result


def prod_sum_report(user_id, attr_list, month_num):
    """Return data of Product Sum."""
    result = {}

    firstday_month = month_num.replace('-', '') + "01"

    set_date = datetime.strptime(firstday_month, "%Y%m%d").date() + relativedelta(months=1)

    purch = db.session.query(Purchase.prd_id,
                             db.func.round(db.func.sum(coalesce(Purchase.quantities, 0))).label("purch_qty"),
                             db.func.sum(coalesce(db.func.round(Purchase.quantities) * Purchase.purchase_price, 0)).label("purch_price_sum"))\
                      .filter(Purchase.purchase_at < set_date)\
                      .group_by(Purchase.prd_id).subquery()

    sale = db.session.query(Sale.prd_id,
                            db.func.round(db.func.sum(coalesce(Sale.quantities, 0))).label("sale_qty"),
                            db.func.sum(coalesce(db.func.round(Sale.quantities) * Sale.transc_price, 0)).label("sale_price_sum"))\
                     .filter(Sale.transc_at < set_date)\
                     .group_by(Sale.prd_id).subquery()

    prod = db.session.query(Product.prd_id,
                            Product.cg_id, Category.cg_name)\
                     .join(Category).join(Product.prddetail)\
                     .filter(CategoryDetailValue.attr_val.in_(attr_list), Product.user_id == user_id)\
                     .group_by(Product.prd_id, Product.cg_id, Category.cg_name).subquery()

    product_sum = db.session.query(prod.c.cg_name,
                                   db.func.count(prod.c.prd_id).label("prod_num"),
                                   db.func.sum(purch.c.purch_qty).label("purch_qty_sum"),
                                   db.func.sum(purch.c.purch_price_sum).label("purch_price_sum"),
                                   db.func.sum(purch.c.purch_qty - sale.c.sale_qty).label("purch_onhand_qty"),
                                   db.func.sum(purch.c.purch_price_sum / purch.c.purch_qty * (purch.c.purch_qty - sale.c.sale_qty)).label("purch_onhand_cost"),
                                   db.func.sum(sale.c.sale_qty).label("sale_qty"),
                                   db.func.sum(sale.c.sale_price_sum).label("sale_price_sum"))\
                            .outerjoin(purch, prod.c.prd_id == purch.c.prd_id)\
                            .outerjoin(sale, prod.c.prd_id == sale.c.prd_id)\
                            .group_by(prod.c.cg_name)

    column_name = [column["name"] for column in product_sum.column_descriptions]

    result["result"] = [dict(zip(column_name, data)) for data in product_sum]

    return result


def sql_to_pichartejson(sqlalchemy_list, chart_title):
    """Change the result of sqlalchemy to linecharte json"""

    qty_date = list(sqlalchemy_list[0])

    data_dict = {"labels": ["Sale Qty", "On-hand Qty"],
                 "datasets": [{"data": qty_date,
                               "backgroundColor": ["#FF6384", "#36A2EB"],
                               "hoverBackgroundColor": ["#FF6384", "#36A2EB"]}]}

    options = {"title": {"display": True, "text": chart_title}, "responsive": True}
    data_chart = {"type": "doughnut", "options": options, "data": data_dict}

    return data_chart


def show_prodchart_json(user_id, month_num, attr_list):
    """show sale profit chart data as a json"""

    firstday_month = month_num.replace('-', '') + "01"

    set_date = datetime.strptime(firstday_month, "%Y%m%d").date() + relativedelta(months=1)

    purch = db.session.query(Purchase.prd_id,
                             db.func.round(db.func.sum(coalesce(Purchase.quantities, 0))).label("purch_qty"),
                             db.func.sum(coalesce(db.func.round(Purchase.quantities) * Purchase.purchase_price, 0)).label("purch_price_sum"))\
                      .filter(Purchase.purchase_at < set_date)\
                      .group_by(Purchase.prd_id).subquery()

    sale = db.session.query(Sale.prd_id,
                            db.func.round(db.func.sum(coalesce(Sale.quantities, 0))).label("sale_qty"),
                            db.func.sum(coalesce(db.func.round(Sale.quantities) * Sale.transc_price, 0)).label("sale_price_sum"))\
                     .filter(Sale.transc_at < set_date)\
                     .group_by(Sale.prd_id).subquery()

    # prod = db.session.query(Product.prd_id,
    #                         Product.cg_id, Category.cg_name)\
    #                  .join(Category).join(Product.prddetail)\
    #                  .filter(CategoryDetailValue.attr_val.in_(attr_list), Product.user_id == user_id)\
    #                  .group_by(Product.prd_id, Product.cg_id, Category.cg_name).subquery()

    product_sum = db.session.query(db.func.sum(sale.c.sale_qty).label("sale_qty_sum"),
                                   db.func.sum(purch.c.purch_qty - sale.c.sale_qty).label("purch_onhand_qty"))\
                            .join(purch, sale.c.prd_id == purch.c.prd_id).all()

    return sql_to_pichartejson(product_sum, "Sales Chart")


def sql_to_barchartejson(sqlalchemy_list, chart_title):
    """Change the result of sqlalchemy to linecharte json"""

    prod_list = []
    sale_list = []

    for prod_name, sale_qty in sqlalchemy_list:
        prod_list.append(prod_name)
        sale_list.append(sale_qty)

    data_dict = {"labels": prod_list,
                 "datasets": [{"data": sale_list,
                               "backgroundColor": ["#FF6384", "#36A2EB", "#36A2EB", "#36A2EB", "#36A2EB",
                                                   "#36A2EB", "#36A2EB", "#36A2EB", "#36A2EB", "#36A2EB"]}]}

    options = {"title": {"display": True, "text": chart_title}, "legend": {"display": False}}
    data_chart = {"type": "bar", "options": options, "data": data_dict}

    return data_chart


def show_top10_prod_json(user_id, month_num, attr_list):
    """Show Top 10 products chart."""

    firstday_month = month_num.replace('-', '') + "01"

    set_date = datetime.strptime(firstday_month, "%Y%m%d").date() + relativedelta(months=1)
    top10_prod = db.session.query(Product.prd_name,
                                  db.func.sum(db.func.round(Sale.quantities)).label("sale_qty"))\
                           .filter(Sale.transc_at < set_date)\
                           .join(Sale).group_by(Product.prd_name)\
                           .order_by(db.func.sum(db.func.round(Sale.quantities)).label("sale_qty").desc())\
                           .limit(10).all()

    return sql_to_barchartejson(top10_prod, "Top Ten Products")


def sql_to_cust_barchartejson(sqlalchemy_list, chart_title):
    """Change the result of sqlalchemy to barcharte json"""

    distrib_name = []
    cust_num = []

    for distri_name, num in sqlalchemy_list:
        distrib_name.append(distri_name)
        cust_num.append(num)

    data_dict = {"labels": distrib_name,
                 "datasets": [{"data": cust_num,
                               "backgroundColor": ["#36A2EB", "#FF6384", "#36A2EB", "#36A2EB"]}]}

    options = {"title": {"display": True, "text": chart_title}, "legend": {"display": False}}
    data_chart = {"type": "bar", "options": options, "data": data_dict}

    return data_chart


def show_cust_age_json(user_id):
    """Show customer age distribution chart."""

    sql = "select birth, count(*) num from ( select case when date_part('year',age(birth_date)) < 20 then 'age:0-20' when date_part('year',age(birth_date)) between 20 and 30 then 'age:21-30' when date_part('year',age(birth_date)) between 30 and 40 then 'age:31-40' when date_part('year',age(birth_date)) > 40 then 'age:41 and up' end birth from customers where user_id = 1 ) a group by birth order by 1"

    cursor = db.session.execute(sql)

    result = cursor.fetchall()

    return sql_to_cust_barchartejson(result, "Customers Age Distribution")


if __name__ == "__main__":

    print "Don't run this file directly."



