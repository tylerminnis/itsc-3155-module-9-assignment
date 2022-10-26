from src.models.movie import Movie
from src.repositories.movie_repository import get_movie_repository
import pytest
from app import app

movie_repository = get_movie_repository()

#correct way of using it
def test_get_all_movies():
    test_app = app.test_client()

    movie_repository.create_movie('The Nightmare Before Christmas', 'Tim Burton', 5)
    response = test_app.get('/movies')
    assert b'<td>The Nightmare Before Christmas</td>' in response.data
    assert b'<td>Tim Burton</td>' in response.data
    assert b'<td>5</td>' in response.data

#bad case (still figuring out)
def test_get_all_movies_wrong():
    test_app = app.test_client()

    movie_repository.create_movie('Morbius', "Daniel Espinosa", 1)
    response = test_app.get('/movies')
    assert not b'<td>Morbo</td>' in response.data
    assert not b'<td>Daniel Spouse</td>' in response.data
    assert not b'<td>4</td>' in response.data