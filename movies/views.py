from django.shortcuts import render, get_object_or_404, redirect
from django.forms import model_to_dict
from .models import Movie
from .forms import MovieForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})

# Деталі конкретного фільму
def movie_detail(request, id):
    movie = get_object_or_404(Movie, pk=id)
    return render(request, 'movies/movie_detail.html', {
        "movie": {
            **model_to_dict(movie),
            "genreName": dict(movie.GENRES).get(movie.genre)
            }
        })
        



def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save() 
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'movies/movie_create.html', {'form': form, "genres": Movie.GENRES})

def movie_update(request, pk): 
    movie = get_object_or_404(Movie, pk=pk) 
    
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if request.FILES and movie.photo: 
            movie.photo.delete()
        if form.is_valid():
            form.save() 
            return redirect('movie_list')
    else:
        form = MovieForm(instance=movie)
    
    return render(request, 'movies/movie_update.html', {'form': form, 'movie': movie,"genres": Movie.GENRES})


def movie_delete(request, pk):
    movie = Movie.objects.get(id=pk)
    if movie is not None:
        movie.delete()

    if movie.photo:
        movie.photo.delete()
    return HttpResponseRedirect(reverse('movie_list'))