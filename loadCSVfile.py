"""Load CSV file to talbes."""

from sqlalchemy.orm.exc import NoResultFound
from model import (Gender, User, Customer, Category, CategoryAttribute, CategoryDetail,
                   Product, CategoryDetailValue, ProductDetail,  Sale, Purchase)
from model import connect_to_db, db, app
from flask import (Flask, render_template, redirect, request, flash,
                   session, jsonify, url_for, send_from_directory)

from add_datato_db import add_attr_to_table, add_product_to_table, add_category

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


if __name__ == "__main__":

    print "Don't run this file directly."
