# TODO: Feature 2

from src.models.movie import Movie
from src.repositories import movie_repository
from src.repositories.movie_repository import get_movie_repository
import pytest
from app import app

get_movie_repository = get_movie_repository()

def test_adding_movie():
    test_app = app.test_client()
    # Gets the size of the movie repo
    size1 = len(movie_repository.get_movie_repository()._db)
    # makes sure size is 0, as no movies have been made
    assert size1 == 0
    # create a movie
    get_movie_repository.create_movie("Movie1", "Director1", 5)
    # makes sure the movie repo is of correct length
    size2 = len(movie_repository.get_movie_repository()._db)
    assert size1 == size2 - 1
    assert size2 == 1

def test_adding_movie():
    test_app = app.test_client()

    repo = movie_repository.get_movie_repository()._db
    
    # Creates a movie, and tests that the values are correct
    get_movie_repository.create_movie("Movie1", "Director1", 5)
    repo = movie_repository.get_movie_repository()._db
    
    assert repo[len(repo) - 1].director == "Director1"
    assert not repo[len(repo) - 1].director == "DirectorThatDoesNotExist"

    assert repo[len(repo) - 1].title == "Movie1"
    assert not repo[len(repo) - 1].title == "MovieThatDoesNotExist"

    assert repo[len(repo) - 1].rating == 5
    assert not repo[len(repo) - 1].rating == 3