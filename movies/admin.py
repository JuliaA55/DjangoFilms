from django.contrib import admin
from .models import Movie

# Register your models here.
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'release_date', 'director', 'photo')
    search_fields = ('title', 'director', 'description')
    list_filter = ('genre', 'release_date', 'director')
    list_per_page = 10

admin.site.register(Movie, MovieAdmin)
