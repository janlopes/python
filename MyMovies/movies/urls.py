from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<movie_id>[0-9]+)/add$', views.add,name='add'),
    url(r'^(?P<movie_id>[0-9]+)/delete$', views.delete,name='delete'),
    url('mycollection/', views.mycollection, name='mycollection')
]

