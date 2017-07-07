import pandas as pd
from model import (Gender, User, Customer, Category, CategoryAttribute, CategoryDetail,
                   Product, CategoryDetailValue, ProductDetail)
from model import connect_to_db, db, app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import UniqueConstraint
from flask import Flask, render_template, request, flash, redirect, session


#cg = Category.query.filter_by(cg_id=2).all()

d = [{'two' : 1,'one':1},{'two' : 2,'one' : 2},{'two' : 3,'one' : 3},{'two' : 4}]
df = pd.DataFrame(d,index=['a','b','c','d'], columns=['one','two'])
df.index.name='index'
df


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    #from server import app

    connect_to_db(app)
    print "Connected to DB."
    print df



# # dataframe with all fields in the table
# df = data_frame(query, [c.name for c in Member.__table__.columns])