"""Load data to database."""

from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import IntegrityError
from model import (Gender, User, Customer, Category, CategoryAttribute, CategoryDetail,
                   Product, CategoryDetailValue, ProductDetail,  Sale, Purchase)
from model import connect_to_db, db, app
from flask import session


def add_file_to_db(row, filename, title=[]):
    """Add CSV file to database.

    According to different filename, call different function to store data to different target tables."""

    if "product" in filename:
        return add_product_to_table(row, title)

    elif "sale" in filename or "purchase" in filename:
        return add_transc_to_table(row, filename)


def add_transc_to_table(row, filename):
    """Add one row of purchases or sales transctions in CSV file to data base."""

    if "purchase" in filename:
        #load purchase transaction file

        prd = Product.query.filter_by(prd_name=row[0].lower()).first()

        add_row = Purchase(prd_id=prd.prd_id,
                           purchase_at=row[1],
                           purchase_price=row[2],
                           quantities=row[3])

    elif "sale" in filename:
        #load sale transaction file

        cust = Customer.query.filter_by(email=row[0]).first()
        prd = Product.query.filter_by(prd_name=row[1].lower()).first()

        add_row = Sale(cust_id=cust.cust_id,
                       prd_id=prd.prd_id,
                       returned_flag=row[2],
                       transc_at=row[3],
                       transc_price=row[4],
                       quantities=row[5]
                       )
    else:
        return "Please upload purchases and sales transcations CSV file."

    try:
        db.session.rollback()
        db.session.add(add_row)
        db.session.commit()
        return "Submit successfully!"
    except IntegrityError:
        db.session.rollback()
        return "fail"


def add_attr_to_table(attr_list):
    """add attributes to  table category_attributes."""

    for attr in attr_list:
        # add attributes into category_attributes.
        attr = attr.lower()
        if CategoryAttribute.query.filter_by(attr_name=attr).first():
            continue
        else:
            attrs = CategoryAttribute(attr_name=attr)
            db.session.add(attrs)

    return True


def add_product_to_table(row_list, attr_list):
    """Add one row of product CSV file to five talbes.

    products, category_detail_values,
    product_details, category_attributes, category_details."""

    cg = Category.query.filter_by(cg_name=row_list[1].lower()).first()

    product = Product(user_id=1,  # session["user_id"],
                      prd_name=row_list[0],
                      cg_id=cg.cg_id,
                      sale_price=row_list[2],
                      description=row_list[3])

    try:
        db.session.add(product)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return "fail"

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
