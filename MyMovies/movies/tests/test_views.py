from django.test import RequestFactory
from django.urls import resolve, reverse
from mixer.backend.django import mixer
from movies.models import Movie
from datetime import datetime
from movies.views import add, delete, index, mycollection
from django.test import TestCase
import pytest

@pytest.mark.django_db
class TestViews(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestViews, cls).setUpClass()
        mixer.blend('movies.MyFavoriteMovies')
        cls.factory = RequestFactory()

    def test_add_view(self):
        path = reverse('add',  args=[1])
        request = self.factory.get(path)
        response = add(request, 1)
        assert 'movies' in response.url and response.status_code == 302

    def test_delete_view(self):
        path = reverse('delete',  args=[1])
        request = self.factory.get(path)
        response = delete(request, 1)
        assert 'movies' in response.url and response.status_code == 302
    
    def test_index_view(self):
        path = reverse('index')
        request = self.factory.get(path)
        response = index(request)
        assert response.status_code == 200

    def test_mycollection_view(self):
        path = reverse('mycollection')
        request = self.factory.get(path)
        response = mycollection(request)
        assert response.status_code == 200