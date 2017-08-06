"""Make up fake data."""

from model import (Gender, User, Customer, Category, CategoryAttribute, CategoryDetail,
                   Product, CategoryDetailValue, ProductDetail, Purchase, Sale)
from model import connect_to_db, db, app
from faker import Faker
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

    for i in range(0, 80):
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

    for i in range(0, 30):

        purchase_price = random.randint(40, 50) * 0.99

        purchase = Purchase(prd_id=random.randint(1, 30),
                            purchase_at=fake.date_time_between(start_date="-1y", end_date="now", tzinfo=None),
                            purchase_price=purchase_price,
                            quantities=random.randint(10, 20)
                            )

        db.session.add(purchase)

    for i in range(0, 20):

        purchase_price = random.randint(100, 110) * 0.99

        purchase = Purchase(prd_id=random.randint(31, 44),
                            purchase_at=fake.date_time_between(start_date="-1y", end_date="now", tzinfo=None),
                            purchase_price=purchase_price,
                            quantities=random.randint(5, 11)
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
