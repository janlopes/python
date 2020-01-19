from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField('launch date')

    def __str__(self):
        return self.title + ' ' + self.date.strftime("%m/%d/%Y, %H:%M:%S")

class MyFavoriteMovies(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)