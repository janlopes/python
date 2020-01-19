from mixer.backend.django import mixer
from movies.models import Movie
from datetime import datetime
import pytest

@pytest.mark.django_db
class TestModels:

    def test_register_new_movie(self):
        movie = mixer.blend('movies.Movie', title = 'Fight Club')
        assert movie.title == 'Fight Club'

    def test_movie_description(self):
        movie = mixer.blend('movies.Movie', title = 'Fight Club')
        
        assert 'Fight Club' in movie.__str__()
    
    def test_register_new_favorite(self):
        movie = mixer.blend('movies.Movie', title = 'Harry Potter')
        fav = mixer.blend('movies.MyFavoriteMovies', movie = movie)
        assert fav.movie.title == 'Harry Potter'