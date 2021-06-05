"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

# Replace this with routes and view functions!

@app.route("/")
def homepage():
    """Show's Homepage """

    return render_template('homepage.html')

@app.route("/movies")
def show_movies():
    """List all movies: title and link to their page."""

    # movies is a list of movie objects
    movies = crud.show_all_movies()

    return render_template('all_movies.html', movies=movies)


@app.route("/movies/<int:movie_id>")
def show_movie(movie_id):
    """Show details on a particular movie."""

    movie = crud.get_movie_by_id(movie_id)

    return render_template("movie_details.html", movie=movie)

@app.route("/users/<int:user_id>")
def show_user(user_id):
    """Show details on a particular movie."""

    user = crud.get_user_by_id(user_id)

    return render_template("user_details.html", user=user)


@app.route("/users")
def show_users():
    """List all users: email and link to their page."""

    # users is a list of user objects
    users = crud.show_all_users()

    
    return render_template('all_users.html', users=users)


@app.route("/create_account", methods=['POST'])
def create_account():
    """Checks if email is available and creates a user."""

    email = request.form.get('email')
    password = request.form.get('password')
    user = crud.get_user_by_email(email)
    print(user)
    print(user==True)

    if user:
        flash("There's already a user with that email. Please try again.")
       
    else:
        crud.create_user(email,password)
        flash("Account created. You can now log in!")

    return redirect('/')

@app.route("/login", methods=['POST'])
def login():
    """Logs in a user. """

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)

    if user.password == password:
        session['current_user'] = user.user_id
        flash("Logged in!")
        return redirect("/")
    else:
        flash("Password incorrect.")
        return redirect("/login")
        




if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
