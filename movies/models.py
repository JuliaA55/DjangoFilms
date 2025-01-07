from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    genre = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/', blank=True, null=True)
    

    def __str__(self):
        return self.title

