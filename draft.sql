from datetime import date

start = date(year=2016,month=11,day=1)
end = date(year=2016,month=11,day=30)

posts = Post.query.filter(Post.post_time <= end).filter(Post.post_time >= start)

posts = Post.query.filter(Post.post_time <= year_month+'-30').filter(Post.post_time >= year_month+'-01')


select p.prd_id, pur.qty, s.qty from products p 
left join (select prd_id, sum(quantities) qty from purchases group by prd_id) pur on  p.prd_id = pur.prd_id
left join (select prd_id, sum(quantities) qty from sales group by prd_id) s on p.prd_id = s.prd_id



sqlalchemy.sql.expression.subquery(alias, *args, **kwargs)



coalesce(Purchase.quantities * Purchase.purchase_price, 0)).label("purch_price_sum"))




db.session.query(
    Sale.prd_id, 
    db.func.sum(coalesce(Sale.quantities, 0)).label("sale_qty"), 
    db.func.sum(coalesce(Sale.quantities * Sale.transc_price, 0)).label("sale_price_sum"))
.group_by(Sale.prd_id).subquery()

db.session.query(db.func.date_part('month', Sale.transc_at).label("year_at")).all()

db.session.query(db.func.round(Sale.transc_price).label("year_at")).all()


select EXTRACT(YEAR FROM transc_at) year_at, EXTRACT(Month FROM transc_at) month_at, prd_id, 
sum(transc_price * quantities) sale_price, sum(quantities) sale_qty 
from sales group by EXTRACT(YEAR FROM transc_at), EXTRACT(Month FROM transc_at), prd_id order by prd_id;

db.session.query(db.func.date_part('year', Sale.transc_at).label("year_at"), 
    db.func.date_part('month', Sale.transc_at).label("month_at"), 
    Sale.prd_id, db.func.sum(Sale.transc_price * Sale.quantities).label("revenue"),
    db.func.sum(Sale.quantities).label("sale_qty"))
.group_by(db.func.date_part('year', Sale.transc_at).label("year_at"), db.func.date_part('month', Sale.transc_at).label("month_at"), Sale.prd_id).all()


-- select product with filter attributes
attr_list = ['gap','nike']
db.session.query(Product.prd_id, Product.cg_id, Category.cg_name).join(Category).join(Product.prddetail).filter(CategoryDetailValue.attr_val.in_(attr_list), Product.user_id == 1).group_by(Product.prd_id, Product.cg_id, Category.cg_name).all()


month_num = 12
set_date = datetime.now().date() - relativedelta(months = month_num)
sale = db.session.query(db.func.date_part('year', Sale.transc_at).label("year_at"), db.func.date_part('month', Sale.transc_at).label("month_at"), Sale.prd_id, db.func.sum(Sale.transc_price * Sale.quantities).label("revenue"),db.func.sum(Sale.quantities).label("sale_qty")).filter(Sale.transc_at >= set_date).group_by(db.func.date_part('year', Sale.transc_at).label("year_at"), db.func.date_part('month', Sale.transc_at).label("month_at"), Sale.prd_id).subquery()

set_date = datetime.now().date() - relativedelta(months = month_num)
sale = db.session.query(db.func.date_part('year', Sale.transc_at).label("year_at"), db.func.date_part('month', Sale.transc_at).label("month_at"), Sale.prd_id, db.func.sum(Sale.transc_price * Sale.quantities).label("revenue"),db.func.sum(Sale.quantities).label("sale_qty")).filter(Sale.transc_at >= set_date).group_by(db.func.date_part('year', Sale.transc_at).label("year_at"), db.func.date_part('month', Sale.transc_at).label("month_at"), Sale.prd_id).subquery()

attr_list = ['gap','nike']
purch_cost = db.session.query(Purchase.prd_id, db.func.round(db.func.sum(Purchase.purchase_price * Purchase.quantities) / db.func.sum(Purchase.quantities), 2).label("avg_purch_cost")).group_by(Purchase.prd_id).subquery()

user_id = 1
prod = db.session.query(Product.prd_id, Product.cg_id, Category.cg_name).join(Category).join(Product.prddetail).filter(CategoryDetailValue.attr_val.in_(attr_list), Product.user_id == user_id).group_by(Product.prd_id, Product.cg_id, Category.cg_name).subquery()

sale_sum = db.session.query(sale.c.year_at, sale.c.month_at, prod.c.cg_name, db.func.sum(sale.c.sale_qty).label("sale_qty"), db.func.sum(sale.c.revenue).label("revenue"), db.func.sum(sale.c.revenue - purch_cost.c.avg_purch_cost * sale.c.sale_qty).label("profit")).join(purch_cost, sale.c.prd_id == purch_cost.c.prd_id).join(prod, sale.c.prd_id == prod.c.prd_id).group_by(sale.c.year_at, sale.c.month_at, prod.c.cg_name).order_by(sale.c.year_at, sale.c.month_at, prod.c.cg_name).all()




db.session.query(db.func.round(sale.c.year_at)).join(purch_cost, sale.c.prd_id == purch_cost.c.prd_id).all()





sale_sum = db.session.query(db.func.round(sale.c.year_at).label("year_at"), db.func.round(sale.c.month_at).label("month_at"), prod.c.cg_name, db.func.sum(sale.c.sale_qty).label("sale_qty"), db.func.sum(sale.c.revenue).label("revenue"), db.func.sum(sale.c.revenue - purch_cost.c.avg_purch_cost * sale.c.sale_qty).label("profit")).join(purch_cost, sale.c.prd_id == purch_cost.c.prd_id).join(prod, sale.c.prd_id == prod.c.prd_id).group_by(db.func.round(sale.c.year_at).label("year_at"), db.func.round(sale.c.month_at).label("month_at"), prod.c.cg_name).order_by(db.func.round(sale.c.year_at).label("year_at"), db.func.round(sale.c.month_at).label("month_at"), prod.c.cg_name)





    

sale_sum.column_descriptions[0]["name"]
Out[39]: 'year_at'


db.session.query(db.func.date_part('year', Sale.transc_at).label("year_at"), 
    db.func.date_part('month', Sale.transc_at).label("month_at"), 
    Sale.prd_id, db.func.sum(Sale.transc_price * Sale.quantities).label("revenue"), 
    db.func.sum(Sale.quantities).label("sale_qty")).filter(Sale.transc_at >= set_date)
.group_by(db.func.date_part('year', Sale.transc_at).label("year_at"), db.func.date_part('month', Sale.transc_at).label("month_at"), Sale.prd_id).subquery()




db.session.query(Purchase.prd_id, db.func.round((db.func.sum(Purchase.purchase_price * Purchase.quantities) / db.func.sum(Purchase.quantities)), 2).label("avg_purch_cost")).group_by(Purchase.prd_id).subquery()





'%0.2f' % profit|float


db.session.query(Purchase.prd_id, 
                 (db.func.sum(Purchase.purchase_price * Purchase.quantities) / db.func.sum(Purchase.quantities))
       .label("avg_purch_cost")).group_by(Purchase.prd_id).subquery()




var fen_yuan = function(val){
    //toFixed来确定保留两位小数  因为除以100 所以都会整除
    var str = (val/100).toFixed(2) + '';
    var intSum = str.substring(0,str.indexOf(".")).replace( /\B(?=(?:\d{3})+$)/g, ',' );
    //取到整数部分
    var dot = str.substring(str.length,str.indexOf("."))
    //取到小数部分
    var ret = intSum + dot;
    return ret;
}


sale_sum_timelabel = db.session.query((sale.c.year_at * 100 + sale.c.month_at).label("sale_at"), prod.c.cg_name,\
    db.func.sum(sale.c.sale_qty).label("sale_qty"),\
    db.func.sum(sale.c.revenue).label("revenue"),\
    db.func.sum(sale.c.revenue - purch_cost.c.avg_purch_cost * sale.c.sale_qty).label("profit"))\
.join(purch_cost, sale.c.prd_id == purch_cost.c.prd_id)\
.join(prod, sale.c.prd_id == prod.c.prd_id)\
.group_by((sale.c.year_at * 100 + sale.c.month_at).label("sale_at"))\
.order_by((sale.c.year_at * 100 + sale.c.month_at).label("sale_at"), prod.c.cg_name)



sale_sum_label = db.session.query((sale.c.year_at * 100 + sale.c.month_at).label("sale_at"), prod.c.cg_name)\
.join(purch_cost, sale.c.prd_id == purch_cost.c.prd_id)\
.join(prod, sale.c.prd_id == prod.c.prd_id)\
.group_by((sale.c.year_at * 100 + sale.c.month_at).label("sale_at"), prod.c.cg_name).all()



time_list, cg_list = zip(*sale_sum_label)

time_list = list(set(time_list))

time_list = [str(int(item)) for item in time_list]

cg_list = list(set(cg_list))

cg_list = [str(item) for item in cg_list]



sale_sum_timelabel = db.session.query((sale.c.year_at * 100 + sale.c.month_at).label("sale_at"))\
.join(purch_cost, sale.c.prd_id == purch_cost.c.prd_id)\
.join(prod, sale.c.prd_id == prod.c.prd_id)\
.group_by((sale.c.year_at * 100 + sale.c.month_at).label("sale_at")).all()





https://stackoverflow.com/questions/26643503/handlebars-loading-external-template-files
$.get('static/sale_sum_report.hbs', function (data) {
    var template=Handlebars.compile(data);
    $(target).html(template(jsonData));
}, 'html')


















