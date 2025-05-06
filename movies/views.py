from django.shortcuts import render
from movies.models import Movies

# Create your views here.

def listMovies(request):
  movie_objects = Movies.objects.all()
  return render( request, 'movies/list_movies.html', {'movie_objects': movie_objects } )