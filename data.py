"""Utility file to seed sba database from MovieLens data in seed_data/"""

from model import User, Customer, connect_to_db, db, app
from faker import Faker
import random

fake = Faker()


def load_customer():
    """Load customer from faker into database."""

    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    gender_code VARCHAR(8) REFERENCES gender,
    phone_number VARCHAR(30) NOT NULL,
    email VARCHAR(50) NOT NULL,
    birth_date DATE NOT NULL, 
    address VARCHAR(256) NOT NULL,
    city VARCHAR(30) NOT NULL,
    state VARCHAR(8) NOT NULL,
    zipcode INTEGER NOT NULL,
    user_id INTEGER REFERENCES users

    first_name = fake.first
    last_name = fake.last_name()
    phone_number = fake.phone_number()
    address = fake.street_address()
    city = fake.city()
    zip = fake.zipcode()

    email_company = ['@gmail.com','@hotmail.com']

        user = User(first_name=first_name,
                    last_name=last_name,
                    gender_code='M',
                    phone_number=phone_number
                    email=first + last_name + random.choice(email_company)
                    bith_date=
            )

        # We need to add to the session or it won't ever be stored
        db.session.add(user)

        # provide some sense of progress
        if i % 100 == 0:
            print i

    # Once we're done, we should commit our work
    db.session.commit()


def set_val_user_id():
    """Set value for the next user_id after seeding database"""

    # Get the Max user_id in the database
    result = db.session.query(func.max(User.user_id)).one()
    max_id = int(result[0])

    # Set the value for the next user_id to be max_id + 1
    query = "SELECT setval('users_user_id_seq', :new_id)"
    db.session.execute(query, {'new_id': max_id + 1})
    db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()

    load_users()
    load_movies()
    load_ratings()
    set_val_user_id()

   
    r = Rating(user_id=jessica.user_id, movie_id=314, score=1)
    db.session.add(r)

    # Aladdin
    r = Rating(user_id=jessica.user_id, movie_id=95, score=5)
    db.session.add(r)

    # The Lion King
    r = Rating(user_id=jessica.user_id, movie_id=71, score=5)
    db.session.add(r)

    db.session.commit()
