
sale_sum = db.session.query(db.func.round(sale.c.year_at).label("year_at"), db.func.round(sale.c.month_at).label("month_at"), prod.c.cg_name, db.func.sum(sale.c.sale_qty).label("sale_qty"), db.func.sum(sale.c.revenue).label("revenue"), db.func.sum(sale.c.revenue - purch_cost.c.avg_purch_cost * sale.c.sale_qty).label("profit")).join(purch_cost, sale.c.prd_id == purch_cost.c.prd_id).join(prod, sale.c.prd_id == prod.c.prd_id).group_by(db.func.round(sale.c.year_at).label("year_at"), db.func.round(sale.c.month_at).label("month_at"), prod.c.cg_name).order_by(db.func.round(sale.c.year_at).label("year_at"), db.func.round(sale.c.month_at).label("month_at"), prod.c.cg_name)

result["result"] = [dict(zip(colum_name, data)) for data in enumerate(sale_sum)]

colum_name = [column["name"] for column in sale_sum.column_descriptions]
