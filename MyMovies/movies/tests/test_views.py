from django.test import RequestFactory
from django.urls import resolve, reverse
from mixer.backend.django import mixer
from movies.models import Movie
from datetime import datetime
from movies.views import add, delete
import pytest

@pytest.mark.django_db
class TestViews:

    def test_add_view(self):
        mixer.blend('movies.MyFavoriteMovies')
        path = reverse('add',  args=[1])
        request = RequestFactory().get(path)
        response = add(request, 1)
        assert 'movies' in response.url and response.status_code == 302

    def test_delete_view(self):
        mixer.blend('movies.MyFavoriteMovies')
        path = reverse('delete',  args=[1])
        request = RequestFactory().get(path)
        response = add(request, 1)
        print(response.url)
        assert 'movies' in response.url and response.status_code == 302
    