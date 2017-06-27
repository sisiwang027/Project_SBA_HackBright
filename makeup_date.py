from faker


for i in range(0,10):
    print fake.zipcode()

for i in range(0,43):
    print fake.first_name_male()

for i in range(0,43):
    print fake.last_name()

for i in range(0,43):
    print fake.street_address()

for i in range(0,43):
    print fake.city()

for i in range(0,43):
    print fake.zipcode()

fake.date(pattern="%Y-%m-%d")
fake.date(pattern="%Y %m %d"),


for i in range(0,57):
    print fake.first_name_female()

for i in range(0,57):
    print fake.last_name()

for i in range(0,57):
    print fake.street_address()

for i in range(0,57):
    print fake.city()

for i in range(0,57):
    print fake.zipcode()

   
class Rating(db.Model):
    """Rating of a movie by a user."""

    __tablename__ = "ratings"

    rating_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.movie_id'), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), index=True)
    score = db.Column(db.Integer)

    # Define relationship to user
    user = db.relationship("User",
                           backref=db.backref("ratings", order_by=rating_id))

    # Define relationship to movie
    movie = db.relationship("Movie",
                            backref=db.bacAkref("ratings", order_by=rating_id))

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Rating rating_id=%s movie_id=%s user_id=%s score=%s>" % (
            self.rating_id, self.movie_id, self.user_id, self.score)