"""Load CSV file to talbes."""

from sqlalchemy.orm.exc import NoResultFound
from model import (Gender, User, Customer, Category, CategoryAttribute, CategoryDetail,
                   Product, CategoryDetailValue, ProductDetail)
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
                for attr in category_attr:
                    # add attributes into category_attributes.
                    attr = attr.lower()
                    if CategoryAttribute.query.filter_by(attr_name=attr).first():
                        continue
                    else:
                        attrs = CategoryAttribute(attr_name=attr)
                        db.session.add(attrs)
            else:
                add_product_to_table(row, category_attr)

        return "Upload successfully!"


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
