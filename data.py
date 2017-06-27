"""Utility file to seed sba database from MovieLens data in seed_data/"""
# insert into gender values ('M', 'Male'), ('FM','Female');
# insert into users (first_name, last_name, email, password) values ('sisi', 'wang', 'wangss.wuhan@gmail.com', '1111');

from model import User, Customer, connect_to_db, db, app
from faker import Faker
import random

fake = Faker()


def load_customer():
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



# def set_val_user_id():
#     """Set value for the next user_id after seeding database"""

#     # Get the Max user_id in the database
#     result = db.session.query(func.max(User.user_id)).one()
#     max_id = int(result[0])

#     # Set the value for the next user_id to be max_id + 1
#     query = "SELECT setval('users_user_id_seq', :new_id)"
#     db.session.execute(query, {'new_id': max_id + 1})
#     db.session.commit()

if __name__ == "__main__":
    connect_to_db(app)
   # db.create_all()

    load_customer()
