from django.db import models

# Create your models here.
class Movie(models.Model):
    GENRES = [
        ("Drama", "Drama"),
        ("Crime", "Crime"),
        ("Sci-Fi", "Sci-Fi"),
        ("Action", "Action"),
        ("Horror", "Horror"),
        ("Fantasy", "Fantasy"),
        ("Thriller", "Thriller"),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    genre = models.CharField(max_length=255, choices=GENRES, blank=True, null=True)
    director = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/', blank=True, null=True)
    

    def __str__(self):
        return self.title

