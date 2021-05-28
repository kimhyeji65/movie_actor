from os import name
from django.db import models
from django.db.models.deletion import CASCADE
# from django.db.models.fields.related import ManyToManyField

# Create your models here.

class Actor(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    class Meta:
        db_table = 'actors'

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    running_time = models.IntegerField()
    actor = models.ManyToManyField(Actor)

    class Meta:
        db_table = 'movies'

