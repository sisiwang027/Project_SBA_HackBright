"""Utility file to seed sba database from MovieLens data in seed_data/"""
# insert into gender values ('M', 'Male'), ('FM','Female');
# insert into users (first_name, last_name, email, password) values ('sisi', 'wang', 'wangss.wuhan@gmail.com', '1111');

from model import Gender, User, Customer, Category, Product, CategoryDetail, CategoryDetailName, CategoryDetailValue, ProductDetail
from model import connect_to_db, db, app
from faker import Faker
from datetime import datetime, timedelta
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


def load_products():
    """Load products infomation."""

    for i in range(0, 123):
        purchase_price = random.randint(15, 100)
        purchase_at = fake.date_time_between(start_date="-1y", end_date="now", tzinfo=None)

        product = Product(cg_id=random.randint(1, 2),
                          user_id=1,
                          purchase_at=purchase_at,
                          purchase_price=purchase_price,
                          cust_id=random.randint(1, 100),
                          sale_price=purchase_price + random.randint(30, 100),
                          sold_at=purchase_at + timedelta(days=random.randint(1, 61))
                          )

        db.session.add(product)

    for i in range(0, 50):

        product = Product(cg_id=random.randint(1, 2),
                          user_id=1,
                          purchase_at=fake.date_time_between(start_date="-1y", end_date="now", tzinfo=None),
                          purchase_price=random.randint(15, 100),
                          cust_id=random.randint(1, 100)
                          )

        db.session.add(product)

    db.session.commit()


def load_category_detailname():
    """Load category detail names."""

    size = CategoryDetailName(detailname='size')
    color = CategoryDetailName(detailname='color')
    brand = CategoryDetailName(detailname='brand')
    material = CategoryDetailName(detailname='material')
    sub_category = CategoryDetailName(detailname='sub_category')

    db.session.add(size)
    db.session.add(color)
    db.session.add(brand)
    db.session.add(material)
    db.session.add(sub_category)

    db.session.commit()


def load_category_details():
    """Load category details."""

    cloth_d1 = CategoryDetail(cg_id=1, cg_detailname_id=1)
    cloth_d2 = CategoryDetail(cg_id=1, cg_detailname_id=2)
    cloth_d3 = CategoryDetail(cg_id=1, cg_detailname_id=3)
    cloth_d4 = CategoryDetail(cg_id=1, cg_detailname_id=4)
    cloth_d5 = CategoryDetail(cg_id=1, cg_detailname_id=5)

    shoe_d1 = CategoryDetail(cg_id=2, cg_detailname_id=1)
    shoe_d2 = CategoryDetail(cg_id=2, cg_detailname_id=2)
    shoe_d3 = CategoryDetail(cg_id=2, cg_detailname_id=3)
    shoe_d4 = CategoryDetail(cg_id=2, cg_detailname_id=5)

    db.session.add(cloth_d1)
    db.session.add(cloth_d2)
    db.session.add(cloth_d3)
    db.session.add(cloth_d4)
    db.session.add(cloth_d5)

    db.session.add(shoe_d1)
    db.session.add(shoe_d2)
    db.session.add(shoe_d3)
    db.session.add(shoe_d4)

    db.session.commit()


def load_category_detail_values():
    """Load values of category details."""

    d_value1 = CategoryDetailValue(cg_detailname_id=1, detail_value='0')
    d_value2 = CategoryDetailValue(cg_detailname_id=1, detail_value='2')
    d_value3 = CategoryDetailValue(cg_detailname_id=1, detail_value='4')
    d_value4 = CategoryDetailValue(cg_detailname_id=1, detail_value='6')
    d_value5 = CategoryDetailValue(cg_detailname_id=1, detail_value='8')
    d_value6 = CategoryDetailValue(cg_detailname_id=1, detail_value='10')

    d_value7 = CategoryDetailValue(cg_detailname_id=2, detail_value='Midnight')
    d_value8 = CategoryDetailValue(cg_detailname_id=2, detail_value='Pink Polish')
    d_value9 = CategoryDetailValue(cg_detailname_id=2, detail_value='Purple Dark')
    d_value10 = CategoryDetailValue(cg_detailname_id=2, detail_value='Red Lipstick')
    d_value11 = CategoryDetailValue(cg_detailname_id=2, detail_value='Black')

    d_value12 = CategoryDetailValue(cg_detailname_id=3, detail_value='gap')

    d_value13 = CategoryDetailValue(cg_detailname_id=4, detail_value='silk')

    d_value14 = CategoryDetailValue(cg_detailname_id=5, detail_value='dress')

    d_shoe1 = CategoryDetailValue(cg_detailname_id=1, detail_value='5')
    d_shoe2 = CategoryDetailValue(cg_detailname_id=1, detail_value='5.5')
    d_shoe3 = CategoryDetailValue(cg_detailname_id=1, detail_value='6')
    d_shoe4 = CategoryDetailValue(cg_detailname_id=1, detail_value='6.5')
    d_shoe5 = CategoryDetailValue(cg_detailname_id=1, detail_value='7')
    d_shoe6 = CategoryDetailValue(cg_detailname_id=1, detail_value='7.5')
    d_shoe7 = CategoryDetailValue(cg_detailname_id=1, detail_value='8')

    d_shoe8 = CategoryDetailValue(cg_detailname_id=2, detail_value='Black/Matte')
    d_shoe9 = CategoryDetailValue(cg_detailname_id=2, detail_value='White/Pure')

    d_shoe10 = CategoryDetailValue(cg_detailname_id=3, detail_value='Nike')

    d_shoe11 = CategoryDetailValue(cg_detailname_id=5, detail_value='AIR JORDAN 4 RETRO')

    db.session.add(d_value1)
    db.session.add(d_value2)
    db.session.add(d_value3)
    db.session.add(d_value4)
    db.session.add(d_value5)
    db.session.add(d_value6)
    db.session.add(d_value7)
    db.session.add(d_value8)
    db.session.add(d_value9)
    db.session.add(d_value10)
    db.session.add(d_value11)
    db.session.add(d_value12)
    db.session.add(d_value13)
    db.session.add(d_value14)

    db.session.add(d_shoe1)
    db.session.add(d_shoe2)
    db.session.add(d_shoe3)
    db.session.add(d_shoe4)
    db.session.add(d_shoe5)
    db.session.add(d_shoe6)
    db.session.add(d_shoe7)
    db.session.add(d_shoe8)
    db.session.add(d_shoe9)
    db.session.add(d_shoe10)
    db.session.add(d_shoe11)

    db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)
    #db.drop_all()
    #db.create_all()

    # load_users()
    # load_gendertype()
    # load_customers()
    # load_categories()
    # load_products()

    # load_category_detailname()
    # load_category_details()

    load_category_detail_values()







