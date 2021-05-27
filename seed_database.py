"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()

# Load movie data from JSON file
with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

# Create movies, store them in list so we can use them
# to create fake ratings later
movies_in_db = []
for movie in movie_data:

    title = movie['title']
    overview = movie['overview']
    poster_path = movie['poster_path']

    release_date = datetime.strptime(movie["release_date"], "%Y-%m-%d") 

    # TODO: get the title, overview, and poster_path from the movie
    # dictionary. Then, get the release_date and convert it to a
    # datetime object with datetime.strptime

    # TODO: create a movie here and append it to movies_in_db
    new_movie = crud.create_movie(title, overview, release_date, poster_path)
    movies_in_db.append(new_movie)

# -------------------------------------------------------------
# Create 10 fake users
for n in range(10):
    email = f'user{n}@test.com'  # Voila! A unique email!
    password = 'test'

    user = crud.create_user(email, password)
    
    for i in range(10):
        crud.create_rating(user, choice(movies_in_db), randint(1, 5))

with open('data/movies.json') as f:
    movie_data = json.loads(f.read())