"""Load CSV file to talbes."""

# from sqlalchemy.orm.exc import NoResultFound
# from model import (Gender, User, Customer, Category, CategoryAttribute, CategoryDetail,
#                    Product, CategoryDetailValue, ProductDetail,  Sale, Purchase)
# from model import connect_to_db, db, app
# from flask import (Flask, render_template, redirect, request, flash,
#                    session, jsonify, url_for, send_from_directory)

from add_datato_db import add_attr_to_table, add_file_to_db


def return_result(upload_result):
    """Return a massage of the result of the upload."""

    failed_records = upload_result.count("fail")
    done_records = upload_result.count("Submit successfully!")
    fail_row = ""

    for index, val in enumerate(upload_result):
        #add all failed row number to a string.
        if val == "fail":
            fail_row = fail_row + str(index + 1) + " "

    if failed_records == 0:
        # return result massage.
        return "Upload {} rows successfully!".format(done_records)
    else:
        return "{} rows uploaded successfully, {} rows unsuccessfully! These row numbers failed: {}!".format(done_records, failed_records, fail_row)


def load_csv(load_file):
    """Load data from product file to five tables.

    products, category_detail_values,
    product_details, category_attributes, category_details."""

    upload_result = []

    if not load_file:
        return "No Selected File!" + "\n" + "Please choose a file."
    elif load_file.content_type != "text/csv":
        return "Please upload a CSV file."
    elif "purchase" in load_file.filename or "sale" in load_file.filename:
        row_idx = 0
        for line in load_file:
            if row_idx != 0:
                row = line.rstrip().split(",")

                upload_result.append(add_file_to_db(row, load_file.filename))

            row_idx += 1

        return return_result(upload_result)

    elif "product" in load_file.filename:
        i = 0
        for line in load_file:
            row = line.rstrip().split(",")
            for colum in row:
                colum = colum.strip()
            if i == 0:
                # read the head of a CSV file.
                category_attr = row[4:]

                # read attributes of category
                add_attr_to_table(category_attr)

                i += 1
            else:
                #record each row's result of the upload.
                upload_result.append(add_file_to_db(row, load_file.filename, category_attr))

        return return_result(upload_result)


if __name__ == "__main__":

    print "Don't run this file directly."
