"""Load CSV file to talbes."""

# from sqlalchemy.orm.exc import NoResultFound
# from model import (Gender, User, Customer, Category, CategoryAttribute, CategoryDetail,
#                    Product, CategoryDetailValue, ProductDetail,  Sale, Purchase)
# from model import connect_to_db, db, app
# from flask import (Flask, render_template, redirect, request, flash,
#                    session, jsonify, url_for, send_from_directory)

from add_datato_db import add_attr_to_table, add_product_to_table


def load_csv_product(load_file):
    """Load data from product file to five tables.

    products, category_detail_values,
    product_details, category_attributes, category_details."""

    prd_result = []
    fail_row = ''

    if not load_file:
        return "No Selected File!" + "\n" + "Please choose a file."
    elif load_file.content_type != "text/csv":
        return "Please upload a CSV file."
    else:
        i = 0
        for line in load_file:
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
                result = add_product_to_table(row, category_attr)
                prd_result.append(result)

        failed_records = prd_result.count("Product has existed, please input a new product! (Product is unique!)")
        done_records = prd_result.count("Submit successfully!")

        for index, val in enumerate(prd_result):
            if val == "Product has existed, please input a new product! (Product is unique!)":
                fail_row = fail_row + str(index + 1) + " "

        if failed_records == 0:
            return "Upload {} rows successfully!".format(done_records)
        else:
            return "Upload {} rows successfully, {} failed! Failed rows' number: {}".format(done_records, failed_records, fail_row)


if __name__ == "__main__":

    print "Don't run this file directly."
