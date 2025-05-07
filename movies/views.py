from django.shortcuts import render
from movies.models import Movies
from django.core.paginator import Paginator

# Create your views here.

def listMovies(request):
  movie_objects = Movies.objects.all()


  movieName = request.GET.get('movieName')
  if movieName:
    movie_objects = movie_objects.filter(name__icontains=movieName)


  paginator = Paginator(movie_objects, 4)
  page = request.GET.get('page')
  movie_objects = paginator.get_page(page)

  return render( request, 'movies/list_movies.html', {'movie_objects': movie_objects } )