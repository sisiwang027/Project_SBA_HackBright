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

def set_val_user_id():
    """Set value for the next user_id after seeding database"""

    # Get the Max user_id in the database
    result = db.session.query(func.max(User.user_id)).one()
    max_id = int(result[0])

    # Set the value for the next user_id to be max_id + 1
    query = "SELECT setval('users_user_id_seq', :new_id)"
    db.session.execute(query, {'new_id': max_id + 1})
    db.session.commit()


from flask_debugtoolbar import DebugToolbarExtension


@app.route("/users")
def users():
    """Show list of users."""

    users = User.query.all()
    return render_template("user_list.html", users=users)

@app.route("/register", methods=["GET"])
def register_form():
    """Show registration form."""

    return render_template("register_form.html")


@app.route("/register", methods=["POST"])
def register_process():
    """Submit registration form."""

    email = request.form.get("email")
    password = request.form.get("password")
    age = request.form.get("age")
    zipcode = request.form.get("zipcode")

    if User.query.filter_by(email=email).count() == 0:

        new_user = User(email=email, password=password, age=age, zipcode=zipcode)
        db.session.add(new_user)
        db.session.commit()
        flash('You have successfully registered')

        return redirect("/")

    else:
        flash('Your email was already registered!')

        return redirect("/register")





@app.route("/logout")
def logout_process():
    """User log out."""

    session.pop('user_id', None)
    flash('You have successfully logged out')
    return redirect("/")


base_file:

 Ratings
  <hr>
  <p><a href="/">Home</a></p>
  <p><a href="/register">Register</a></p>

  {% if not session.get("user_id") %}
    <a href="/login">Log In</a>
  {% else %}
    <a href="/logout">Log Out</a>
  {% endif %}
  
  {% with messages = get_flashed_messages() %}
    {% if messages %}
      <ul class=flashes>
      {% for message in messages %}
        <li>{{ message }}</li>
      {% endfor %}
      </ul>
    {% endif %}
  {% endwith %}


cars = Category(cg_name="cars")

In [2]: db.session.add(cars)

In [3]: style = CategoryDetailName(detailname="style")

In [4]: sunroof = CategoryDetaiName(detailname="sunroof")

  ----> 1 sunroof = CategoryDetaiName(detailname="sunroof")

NameError: name 'CategoryDetaiName' is not defined

In [5]: sunroof = CategoryDetailName(detailname="sunroof")

In [6]: cars.category_details.extend([style, sunroof])

# association table
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


    cg_id, purchase_at, purchase_price=, sale_price=, quantities=, style, brand, size, material, color


    In [9]: vals = ['red', 'blue', 'crayon']

In [10]: for i, value in enumerate(vals):
    ...:     print i, value


    for p in prod:
   ...:     print p.prd_name
   ...:     for d in p.prddetail:
   ...:         print '\t', d.attr_val
   ...:         


csvreader.line_num

###################
#bootstramp
###################

import flask_admin as admin
from flask_admin.contrib import sqla
from flask_admin.contrib.sqla import filters

# Customized User model admin
class UserAdmin(sqla.ModelView):
    inline_models = (UserInfo,)


# Customized Post model admin
class PostAdmin(sqla.ModelView):
    # Visible columns in the list view
    column_exclude_list = ['text']

    # List of columns that can be sorted. For 'user' column, use User.username as
    # a column.
    column_sortable_list = ('title', ('user', 'user.username'), 'date')

    # Rename 'title' columns to 'Post Title' in list view
    column_labels = dict(title='Post Title')

    column_searchable_list = ('title', User.username)

    column_filters = ('user',
                      'title',
                      'date',
                      filters.FilterLike(Post.title, 'Fixed Title', options=(('test1', 'Test 1'), ('test2', 'Test 2'))))

    # Pass arguments to WTForms. In this case, change label for text field to
    # be 'Big Text' and add required() validator.
    form_args = dict(
                    text=dict(label='Big Text', validators=[validators.required()])
                )

    form_ajax_refs = {
        'user': {
            'fields': (User.username, User.email)
        },
        'tags': {
            'fields': (Tag.name,)
        }
    }

    def __init__(self, session):
        # Just call parent class with predefined model.
        super(PostAdmin, self).__init__(Post, session)


class TreeView(sqla.ModelView):
    form_excluded_columns = ['children', ]


# Create admin
admin = admin.Admin(app, name='Example: SQLAlchemy', template_mode='bootstrap3')

# Add views
admin.add_view(UserAdmin(User, db.session))
admin.add_view(sqla.ModelView(Tag, db.session))
admin.add_view(PostAdmin(db.session))
admin.add_view(TreeView(Tree, db.session))

