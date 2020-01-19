from django.urls import resolve, reverse
from django.test import TestCase

class TestUrls:

    def test_add_movie(self):
        path = reverse('add',  args=[1])
        assert resolve(path).view_name == "add"

    def test_delete_movie(self):
        path = reverse('delete',  args=[1])
        assert resolve(path).view_name == "delete"