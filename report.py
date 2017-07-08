import pandas as pd
from model import (Gender, User, Customer, Category, CategoryAttribute, CategoryDetail,
                   Product, CategoryDetailValue, ProductDetail)
from model import connect_to_db, db, app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import UniqueConstraint
from flask import Flask, session


app.secret_key = "WANGSS"



#cg = Category.query.filter_by(cg_id=2).all()

# d = [{'two' : 1,'one':1},{'two' : 2,'one' : 2},{'two' : 3,'one' : 3},{'two' : 4}]
# df = pd.DataFrame(d,index=['a','b','c','d'], columns=['one','two'])
# df.index.name='index'
# df
def show_table():
    sql = "select c.prd_name, max(c.total_num) total_num,  sum(coalesce(d.quantities,0)) sale_num  from (select a.prd_id, a.prd_name, sum(coalesce(b.quantities,0)) total_num from products a left join purchases b on a.prd_id=b.prd_id group by a.prd_id, a.prd_name) c left join sales d on c.prd_id = d.prd_id group by c.prd_name order by 2 desc"
    cursor = db.session.execute(sql)
    df = pd.DataFrame(cursor.fetchall(), columns=["Product", "Inventory", "Sale Volume"])
    # query = db.session.query(Category).filter(Category.cg_id == 1)
    # df = pd.read_sql(query.statement, session.bind)
    
    return df.to_html()


def show_pie():
    sql = "select c.attr_val, sum(s.quantities) from sales s, products p, product_details pd, category_detail_values c where s.prd_id=p.prd_id and p.prd_id=pd.prd_id  and pd.cg_detailvalue_id=c.cg_detailvalue_id and c.cg_attr_id=4 and p.cg_id=1 group by c.attr_val"
    cursor = db.session.execute(sql)
    df = pd.DataFrame(cursor.fetchall(), columns=["Color", "Sale Volume"])
    # query = db.session.query(Category).filter(Category.cg_id == 1)
    # df = pd.read_sql(query.statement, session.bind)
    
    return df.to_html()

if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    #from server import app
    connect_to_db(app)
    print "Connected to DB."




# # dataframe with all fields in the table
# df = data_frame(query, [c.name for c in Member.__table__.columns])