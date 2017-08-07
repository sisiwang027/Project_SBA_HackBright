"""Make up exmaple data."""


from model import (Gender, User, Customer, Category, CategoryAttribute, CategoryDetail,
                   Product, CategoryDetailValue, ProductDetail, Purchase, Sale)
from model import connect_to_db, db, app
from faker import Faker
from datetime import timedelta
import random

fake = Faker()


def example_data():
    """Create some sample data."""
    #add one user for testing.
    user = User(first_name='sisi', last_name='wang', email='wangss.wuhan@gmail.com', password='1111')

    db.session.add(user)

    db.session.commit()

    #dd gender type
    male = Gender(gender_code='M', gender_name='Male')
    female = Gender(gender_code='FM', gender_name='Female')

    db.session.add(male)
    db.session.add(female)

    db.session.commit()

    #Load customer from faker into database
    email_company = ['@gmail.com', '@hotmail.com']

    for i in range(0, 1):

        first_name = fake.first_name_male()
        last_name = fake.last_name()
        #email = first_name + last_name + random.choice(email_company)
        email = 'ww@gmail.com'

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

    for i in range(0, 10):
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

    #Load categories infomation.
    clothing = Category(cg_name='clothing')
    shoes = Category(cg_name='shoes')

    db.session.add(clothing)
    db.session.add(shoes)

    db.session.commit()

    #Add products
    product1 = Product(user_id=1, prd_name='nikeshoes', cg_id=2, sale_price=180.99, description='test')
    product2 = Product(user_id=1, prd_name='gapclothing', cg_id=1, sale_price=180.99, description='test')

    db.session.add(product1)
    db.session.add(product2)

    cg_attr1 = CategoryAttribute(attr_name="brand")
    cg_attr2 = CategoryAttribute(attr_name="size")

    db.session.add(cg_attr1)
    db.session.add(cg_attr2)

    db.session.commit()

    cg_dval1 = CategoryDetailValue(cg_attr_id=1, attr_val="nike")
    cg_dval2 = CategoryDetailValue(cg_attr_id=2, attr_val="6")
    cg_dval3 = CategoryDetailValue(cg_attr_id=1, attr_val="gap")
    cg_dval4 = CategoryDetailValue(cg_attr_id=2, attr_val="4")

    db.session.add(cg_dval1)
    db.session.add(cg_dval2)
    db.session.add(cg_dval3)
    db.session.add(cg_dval4)

    db.session.commit()

    cg_d1 = CategoryDetail(cg_id=1, cg_attr_id=1)
    cg_d2 = CategoryDetail(cg_id=1, cg_attr_id=2)
    cg_d3 = CategoryDetail(cg_id=2, cg_attr_id=1)
    cg_d4 = CategoryDetail(cg_id=2, cg_attr_id=2)

    db.session.add(cg_d1)
    db.session.add(cg_d2)
    db.session.add(cg_d3)
    db.session.add(cg_d4)

    prd_d1 = ProductDetail(prd_id=1, cg_detailvalue_id=1)
    prd_d2 = ProductDetail(prd_id=1, cg_detailvalue_id=2)
    prd_d3 = ProductDetail(prd_id=2, cg_detailvalue_id=3)
    prd_d4 = ProductDetail(prd_id=2, cg_detailvalue_id=4)

    db.session.add(prd_d1)
    db.session.add(prd_d2)
    db.session.add(prd_d3)
    db.session.add(prd_d4)

    db.session.commit()

    #Load product sale infomation
    for i in range(0, 20):
        sale = Sale(cust_id=random.randint(1, 11),
                    prd_id=1,
                    returned_flag=False,
                    transc_at=fake.date_time_between(start_date="-1y", end_date="now", tzinfo=None),
                    transc_price=random.randint(65, 80),
                    quantities=random.randint(1, 5)
                    )

        db.session.add(sale)

    for i in range(0, 20):
        sale = Sale(cust_id=random.randint(1, 11),
                    prd_id=2,
                    returned_flag=False,
                    transc_at=fake.date_time_between(start_date="-1y", end_date="now", tzinfo=None),
                    transc_price=random.randint(160, 180),
                    quantities=random.randint(1, 5)
                    )
        db.session.add(sale)

    db.session.commit()

    # Load purchases infomation
    for i in range(0, 10):

        purchase_price = random.randint(40, 50) * 0.99

        purchase = Purchase(prd_id=1,
                            purchase_at=fake.date_time_between(start_date="-1y", end_date="now", tzinfo=None),
                            purchase_price=purchase_price,
                            quantities=random.randint(20, 88)
                            )

        db.session.add(purchase)

    for i in range(0, 10):

        purchase_price = random.randint(100, 110) *0.99

        purchase = Purchase(prd_id=2,
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

    load_users()
    load_gendertype()
    load_customers()
    load_categories()
    load_products()
    load_purchases()
    load_sales()

   
