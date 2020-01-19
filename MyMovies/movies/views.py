from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie, MyFavoriteMovies
from django.template import loader, RequestContext

# Create your views here.
def index(request):
    my_movies = MyFavoriteMovies.objects.all()
    my_movies_ids = [x.movie.id for x in my_movies]
    all_movies = Movie.objects.exclude(pk__in=my_movies_ids)  
    return render(request, 'movies/index.html', {
                'all_movies':all_movies
            })


def add(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    favorite = MyFavoriteMovies(movie = movie)
    favorite.save()
    response = redirect('/movies/')
    return response

def delete(request, movie_id):
    favorite = MyFavoriteMovies.objects.get(movie=movie_id)
    favorite.delete()
    response = redirect('/movies/mycollection/')
    return response

def mycollection(request):
    my_movies = MyFavoriteMovies.objects.all()
    my_movies_ids = [x.movie.id for x in my_movies]
    all_movies = Movie.objects.filter(pk__in=my_movies_ids)  
    return render(request, 'movies/mycollection.html', {
                'all_movies':all_movies
            })