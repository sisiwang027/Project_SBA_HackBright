"""Load CSV file to talbes."""

from sqlalchemy.orm.exc import NoResultFound
from model import (Gender, User, Customer, Category, CategoryAttribute, CategoryDetail,
                   Product, CategoryDetailValue, ProductDetail,  Sale, Purchase)
from model import connect_to_db, db, app
from flask import (Flask, render_template, redirect, request, flash,
                   session, jsonify, url_for, send_from_directory)

def load_csv_product(file):
    """Load data from product file to five tables.

    products, category_detail_values,
    product_details, category_attributes, category_details."""

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
                add_attr_to_table(category_attr)
            else:
                add_product_to_table(row, category_attr)

        return "Upload successfully!"


def add_attr_to_table(attr_list):
    """add attributes to  table, category_attributes."""

    for attr in attr_list:
                    # add attributes into category_attributes.
                    attr = attr.lower()
                    if CategoryAttribute.query.filter_by(attr_name=attr).first():
                        continue
                    else:
                        attrs = CategoryAttribute(attr_name=attr)
                        db.session.add(attrs)


def add_product_to_table(row_list, attr_list):
    """Add file to five talbes.

    products, category_detail_values,
    product_details, category_attributes, category_details."""

    cg = Category.query.filter_by(cg_name=row_list[1].lower()).first()

    product = Product(user_id=session["user_id"],
                      prd_name=row_list[0],
                      cg_id=cg.cg_id,
                      sale_price=row_list[2],
                      description=row_list[3])
    db.session.add(product)

    attr_val = row_list[4:]
    val_list = []

    # read values of attributes.
    for i, val in enumerate(attr_val):

        attr = CategoryAttribute.query.filter_by(attr_name=attr_list[i]).first()

        val = val.lower()

        # adding attribute-value pairs into category_attributes.
        is_attr = CategoryDetailValue.query.filter_by(cg_attr_id=attr.cg_attr_id, attr_val=val).first()
        if is_attr and val != '':
            val_list.append(is_attr)

        elif is_attr and val == '':
            continue

        elif not is_attr and val != '':
            new_val = CategoryDetailValue(cg_attr_id=attr.cg_attr_id, attr_val=val)
            db.session.add(new_val)
            val_list.append(new_val)

        # adding category-attribute pairs into category_attributes.
        if CategoryDetail.query.filter_by(cg_id=cg.cg_id, cg_attr_id=attr.cg_attr_id).first() or val == '':
            continue
        else:
            cg.cgattribute.append(attr)

    product.prddetail.extend(val_list)
    db.session.commit()

    return "Submit successfully!"


def add_category(new_category):
    """Add new category from form of web site."""
    new_category = new_category.strip().lower()

    if new_category == '':
        return "Please enter a category name."
    else:
        try:
            Category.query.filter_by(cg_name=new_category).one()
            return "The category has existed. Please add a new one."

        except NoResultFound:
            db.session.add(Category(cg_name=new_category))
            db.session.commit()
            return "The category has been successfully added."

if __name__ == "__main__":

    print "Don't run this file directly."


# def display_salesum_json(month_num, attr_list, user_id):
#     """Show sale sumarizing data as jason"""

#     result = {}

#     set_date = datetime.now().date() - relativedelta(months=month_num)
#     sale = db.session.query(db.func.date_part('year', Sale.transc_at).label("year_at"), db.func.date_part('month', Sale.transc_at).label("month_at"), Sale.prd_id, db.func.sum(Sale.transc_price * Sale.quantities).label("revenue"), db.func.sum(Sale.quantities).label("sale_qty")).filter(Sale.transc_at >= set_date).group_by(db.func.date_part('year', Sale.transc_at).label("year_at"), db.func.date_part('month', Sale.transc_at).label("month_at"), Sale.prd_id).subquery()

#     purch_cost = db.session.query(Purchase.prd_id, (db.func.sum(Purchase.purchase_price * Purchase.quantities) / db.func.sum(Purchase.quantities)).label("avg_purch_cost")).group_by(Purchase.prd_id).subquery()

#     prod = db.session.query(Product.prd_id, Product.cg_id, Category.cg_name).join(Category).join(Product.prddetail).filter(CategoryDetailValue.attr_val.in_(attr_list), Product.user_id == user_id).group_by(Product.prd_id, Product.cg_id, Category.cg_name).subquery()

#     sale_sum = db.session.query((sale.c.year_at * 100 + sale.c.month_at).label("sale_at"), prod.c.cg_name, db.func.sum(sale.c.sale_qty).label("sale_qty"), db.func.sum(sale.c.revenue).label("revenue"), db.func.sum(sale.c.revenue - purch_cost.c.avg_purch_cost * sale.c.sale_qty).label("profit")).join(purch_cost, sale.c.prd_id == purch_cost.c.prd_id).join(prod, sale.c.prd_id == prod.c.prd_id).group_by((sale.c.year_at * 100 + sale.c.month_at).label("sale_at"), prod.c.cg_name).order_by((sale.c.year_at * 100 + sale.c.month_at).label("sale_at"), prod.c.cg_name)

#     column_name = [column["name"] for column in sale_sum.column_descriptions]

#     result["result"] = [dict(zip(column_name, data)) for data in sale_sum]

#     return sale_sum.all()

#     # return jsonify(result)
