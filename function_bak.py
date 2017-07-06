"""Load CSV file to talbes."""

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
                cg = Category.query.filter_by(cg_name=row[1].lower()).first()

                product = Product(user_id=session["user_id"],
                                  prd_name=row[0],
                                  cg_id=cg.cg_id,
                                  sale_price=row[2],
                                  description=row[3])
                db.session.add(product)
                # db.session.commit()

                attr_val = row[4:]
                val_list = []

                # read values of attributes.
                for i in range(0, len(attr_val)):

                    attr = CategoryAttribute.query.filter_by(attr_name=category_attr[i]).first()

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

        return "Upload successfully!"


if __name__ == "__main__":

    load_csv_product(file)
