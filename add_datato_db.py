"""Load data to database."""

from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import IntegrityError
from model import (Gender, User, Customer, Category, CategoryAttribute, CategoryDetail,
                   Product, CategoryDetailValue, ProductDetail,  Sale, Purchase)
from model import connect_to_db, db, app
from flask import session


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

    try:
        db.session.add(product)
        db.session.commit()
    except IntegrityError:
        return "Product has existed, please input a new product! (Product is unique!)"

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
