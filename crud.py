"""CRUD operations."""

from model import db, User, Movie, Rating, connect_to_db

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user


def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie. releas_date must be of type DateTime."""

    movie = Movie(title=title, overview=overview, release_date=release_date, poster_path=poster_path)

    db.session.add(movie)
    db.session.commit()

    return movie

def show_all_movies():
    """Returns all movies from database. """

    movies = Movie.query.all()

    return movies

def show_all_users():
    """Returns alll users. """
    
    return User.query.all()

def get_user_by_id(user_id):
    """Returns the movie with corresponding movie id. """

    return User.query.get(user_id)

def get_user_by_email(user_email):
    """Return the user with the email addres user_email."""
    return User.query.filter(User.email == user_email).first()

def create_rating(user, movie, score):
    """Create and return a rating. score: int, user and movie are objects."""

    rating = Rating(user=user, movie=movie, score=score)

    db.session.add(rating)
    db.session.commit()

    return rating


def get_movie_by_id(movie_id):
    """Returns the movie with corresponding movie id. """

    movie = Movie.query.get(movie_id)

    return movie


if __name__ == '__main__':
    from server import app
    connect_to_db(app)