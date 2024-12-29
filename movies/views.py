from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie

# Create your views here.
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})

# Деталі конкретного фільму
def movie_detail(request, id):
    movie = get_object_or_404(Movie, pk=id)
    return render(request, 'movies/movie_detail.html', {'movie': movie})


def movie_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        release_date = request.POST['release_date']
        director = request.POST['director']
        genre = request.POST['genre']

        Movie.objects.create(
            title=title,
            description=description,
            release_date=release_date,
            director=director,
            genre=genre
        )

        return redirect('movie_list')

    return render(request, 'movies/movie_create.html')