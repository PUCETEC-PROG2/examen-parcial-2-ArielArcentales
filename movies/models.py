from django.db import models

# Create your models here.
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    director_name = models.CharField(max_length=100)
    release_year = models.DateField()
    synopsis = models.TextField()

    def __str__(self):
        return self.title
