from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/(?P<movie_id>[0-9]+)$', views.add,name='add'),
    url(r'^delete/(?P<movie_id>[0-9]+)$', views.delete,name='delete'),
    url('mycollection/', views.mycollection, name='mycollection'),
]

