"""Make up fake data."""


from model import (Gender, User, Customer, Category, CategoryAttribute, CategoryDetail,
                   Product, CategoryDetailValue, ProductDetail, Purchase, Sale)
from model import connect_to_db, db, app
from faker import Faker
from datetime import timedelta
import random

fake = Faker()


def load_users():
    """add one user for testing."""
    user = User(first_name='sisi', last_name='wang', email='wangss.wuhan@gmail.com', password='1111')

    db.session.add(user)

    db.session.commit()


def load_gendertype():
    """add gender type."""
    male = Gender(gender_code='M', gender_name='Male')
    female = Gender(gender_code='FM', gender_name='Female')

    db.session.add(male)
    db.session.add(female)

    db.session.commit()


def load_customers():
    """Load customer from faker into database."""

    email_company = ['@gmail.com', '@hotmail.com']

    for i in range(0, 43):

        first_name = fake.first_name_male()
        last_name = fake.last_name()
        email = first_name + last_name + random.choice(email_company)

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            gender_code='M',
                            phone_number=str(fake.phone_number()),
                            email=email,
                            birth_date=fake.date(pattern="%Y %m %d"),
                            address=fake.street_address(),
                            city=fake.city(),
                            state='CA',
                            zipcode=int(fake.zipcode()),
                            user_id=1)

        db.session.add(customer)

    for i in range(0, 57):
        first_name = fake.first_name_male()
        last_name = fake.last_name()
        email = first_name + last_name + random.choice(email_company)

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            gender_code='FM',
                            phone_number=str(fake.phone_number()),
                            email=email,
                            birth_date=fake.date(pattern="%Y %m %d"),
                            address=fake.street_address(),
                            city=fake.city(),
                            state='CA',
                            zipcode=int(fake.zipcode()),
                            user_id=1)

        db.session.add(customer)

    db.session.commit()


def load_categories():
    """Load categories infomation."""

    clothing = Category(cg_name='clothing')
    shoes = Category(cg_name='shoes')

    db.session.add(clothing)
    db.session.add(shoes)

    db.session.commit()


def load_sales():
    """Load product sale infomation."""

    for i in range(0, 60):
        sale = Sale(cust_id=random.randint(1, 100),
                    prd_id=random.randint(1, 30),
                    returned_flag=False,
                    transc_at=fake.date_time_between(start_date="-1y", end_date="now", tzinfo=None),
                    transc_price=random.randint(65, 80),
                    quantities=random.randint(1, 5)
                    )

        db.session.add(sale)

    for i in range(0, 60):
        sale = Sale(cust_id=random.randint(1, 100),
                    prd_id=random.randint(31, 44),
                    returned_flag=False,
                    transc_at=fake.date_time_between(start_date="-1y", end_date="now", tzinfo=None),
                    transc_price=random.randint(160, 180),
                    quantities=random.randint(1, 5)
                    )
        db.session.add(sale)

    db.session.commit()


def load_purchases():
    """Load purchases infomation."""

    for i in range(0, 66):

        purchase_price = random.randint(40, 50) * 0.99

        purchase = Purchase(prd_id=random.randint(1, 30),
                            purchase_at=fake.date_time_between(start_date="-1y", end_date="now", tzinfo=None),
                            purchase_price=purchase_price,
                            quantities=random.randint(20, 88)
                            )

        db.session.add(purchase)

    for i in range(0, 66):

        purchase_price = random.randint(100, 110) *0.99

        purchase = Purchase(prd_id=random.randint(31, 44),
                            purchase_at=fake.date_time_between(start_date="-1y", end_date="now", tzinfo=None),
                            purchase_price=purchase_price,
                            quantities=random.randint(20, 40)
                            )

        db.session.add(purchase)

    db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)
    # db.drop_all()

    db.create_all()

    # load_users()
    # load_gendertype()
    # load_customers()
    # load_categories()
    load_purchases()
    load_sales()

    # load_category_detailname()
    # load_category_detail_values()

    # load_purchase_cg_details()
    # load_sale_cg_details()



#################
#save for later
#################

# CREATE VIEW product_sum AS
#   SELECT p.prd_id, p.user_id, p.prd_name, p.cg_id, c.cg_name, p.sale_price,
#   p.description, coalesce(purc.purc_qty, 0) purc_qty, coalesce(purc.purc_cost, 0) purc_cost,
#          coalesce(s.sale_qty, 0) sale_qty, coalesce(s.revenue, 0) revennue
#     FROM products AS p
#        LEFT JOIN (select prd_id, SUM(quantities) purc_qty, SUM(purchase_price * quantities) purc_cost FROM purchases GROUP BY prd_id) AS purc ON  p.prd_id = purc.prd_id
#        LEFT JOIN (SELECT prd_id, SUM(quantities) sale_qty, SUM(quantities * transc_price) revenue FROM sales GROUP BY prd_id) AS s ON p.prd_id = s.prd_id
#        LEFT JOIN categories c ON p.cg_id=c.cg_id;

# def load_products():
#     """Load products infomation."""

#     pass


# def load_category_attributes():
#     """Load category detail names."""

#     size = CategoryAttribute(detailname='size')
#     color = CategoryAttribute(detailname='color')
#     brand = CategoryAttribute(detailname='brand')
#     material = CategoryAttribute(detailname='material')
#     sub_category = CategoryAttribute(detailname='style')

#     db.session.add(size)
#     db.session.add(color)
#     db.session.add(brand)
#     db.session.add(material)
#     db.session.add(sub_category)

#     db.session.commit()


# def load_transc_type():
#     """Load transaction types."""

#     sold = TranscType(transc_type='s', type_name='sold')
#     returned = TranscType(transc_type='r', type_name='returned')

#     db.session.add(sold)
#     db.session.add(returned)

#     db.session.commit()


# def load_purchase_cg_details():
#     """Load purchase cagegory dtails."""

#     purchase_cg1 = db.session.query(Purchase).filter(Purchase.cg_id == 1).all()
#     purchase_cg2 = db.session.query(Purchase).filter(Purchase.cg_id == 2).all()
#     detail_values = db.session.query(CategoryDetailValue).filter(CategoryDetailValue.cg_detailvalue_id <= 14).all()
#     detail_values2 = db.session.query(CategoryDetailValue).filter(CategoryDetailValue.cg_detailvalue_id > 14).all()

#     for cg in purchase_cg1:
#         for detail_value in detail_values:
#             p_detail = PurchaseCgDetail(p_id=cg.p_id, cg_detailvalue_id=detail_value.cg_detailvalue_id)
#             db.session.add(p_detail)

#     for cg in purchase_cg2:
#         for detail_value in detail_values2:
#             p_detail = PurchaseCgDetail(p_id=cg.p_id, cg_detailvalue_id=detail_value.cg_detailvalue_id)
#             db.session.add(p_detail)

#     db.session.commit()




# def load_sale_cg_details():
#     """Load sale cagegory dtails."""

#     sale_cg1 = db.session.query(Sale).filter(Sale.cg_id == 1).all()
#     sale_cg2 = db.session.query(Sale).filter(Sale.cg_id == 2).all()
#     detail_values = db.session.query(CategoryDetailValue).filter(CategoryDetailValue.cg_detailvalue_id <= 14).all()
#     detail_values2 = db.session.query(CategoryDetailValue).filter(CategoryDetailValue.cg_detailvalue_id > 14).all()

#     for cg in sale_cg1:
#         for detail_value in detail_values:
#             p_detail = SaleCgDetail(s_id=cg.s_id, cg_detailvalue_id=detail_value.cg_detailvalue_id)
#             db.session.add(p_detail)

#     for cg in sale_cg2:
#         for detail_value in detail_values2:
#             p_detail = SaleCgDetail(s_id=cg.s_id, cg_detailvalue_id=detail_value.cg_detailvalue_id)
#             db.session.add(p_detail)

#     db.session.commit()

# def load_category_detail_values():
#     """Load values of category details."""

#     d_value1 = CategoryDetailValue(cg_attribute_id=1, detail_value='0')
#     d_value2 = CategoryDetailValue(cg_attribute_id=1, detail_value='2')
#     d_value3 = CategoryDetailValue(cg_attribute_id=1, detail_value='4')
#     d_value4 = CategoryDetailValue(cg_attribute_id=1, detail_value='6')
#     d_value5 = CategoryDetailValue(cg_attribute_id=1, detail_value='8')
#     d_value6 = CategoryDetailValue(cg_attribute_id=1, detail_value='10')

#     d_value7 = CategoryDetailValue(cg_attribute_id=2, detail_value='Midnight')
#     d_value8 = CategoryDetailValue(cg_attribute_id=2, detail_value='Pink Polish')
#     d_value9 = CategoryDetailValue(cg_attribute_id=2, detail_value='Purple Dark')
#     d_value10 = CategoryDetailValue(cg_attribute_id=2, detail_value='Red Lipstick')
#     d_value11 = CategoryDetailValue(cg_attribute_id=2, detail_value='Black')

#     d_value12 = CategoryDetailValue(cg_attribute_id=3, detail_value='Gap')

#     d_value13 = CategoryDetailValue(cg_attribute_id=4, detail_value='Silk')

#     d_value14 = CategoryDetailValue(cg_attribute_id=5, detail_value='Dress')

#     d_shoe1 = CategoryDetailValue(cg_attribute_id=1, detail_value='5')
#     d_shoe2 = CategoryDetailValue(cg_attribute_id=1, detail_value='5.5')
#     d_shoe3 = CategoryDetailValue(cg_attribute_id=1, detail_value='6')
#     d_shoe4 = CategoryDetailValue(cg_attribute_id=1, detail_value='6.5')
#     d_shoe5 = CategoryDetailValue(cg_attribute_id=1, detail_value='7')
#     d_shoe6 = CategoryDetailValue(cg_attribute_id=1, detail_value='7.5')
#     d_shoe7 = CategoryDetailValue(cg_attribute_id=1, detail_value='8')

#     d_shoe8 = CategoryDetailValue(cg_attribute_id=2, detail_value='Black/Matte')
#     d_shoe9 = CategoryDetailValue(cg_attribute_id=2, detail_value='White/Pure')

#     d_shoe10 = CategoryDetailValue(cg_attribute_id=3, detail_value='Nike')

#     d_shoe11 = CategoryDetailValue(cg_attribute_id=5, detail_value='AIR JORDAN 4 RETRO')

#     db.session.add(d_value1)
#     db.session.add(d_value2)
#     db.session.add(d_value3)
#     db.session.add(d_value4)
#     db.session.add(d_value5)
#     db.session.add(d_value6)
#     db.session.add(d_value7)
#     db.session.add(d_value8)
#     db.session.add(d_value9)
#     db.session.add(d_value10)
#     db.session.add(d_value11)
#     db.session.add(d_value12)
#     db.session.add(d_value13)
#     db.session.add(d_value14)

#     db.session.add(d_shoe1)
#     db.session.add(d_shoe2)
#     db.session.add(d_shoe3)
#     db.session.add(d_shoe4)
#     db.session.add(d_shoe5)
#     db.session.add(d_shoe6)
#     db.session.add(d_shoe7)
#     db.session.add(d_shoe8)
#     db.session.add(d_shoe9)
#     db.session.add(d_shoe10)
#     db.session.add(d_shoe11)

#     db.session.commit()


