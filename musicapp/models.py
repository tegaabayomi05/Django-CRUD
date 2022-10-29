from email.policy import default
from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField
from datetime import datetime

# Create your models here.

class Artiste(models.Model):
    first_name= models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    age= models.IntegerField()

class Song(models.Model):
    Artiste= models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title= models.CharField(max_length=100)
    date_released= models.DateField(default=datetime.today)
    likes= models.IntegerField()
    artiste_id= models.IntegerField()


class Lyric(models.Model):
    song= models.ForeignKey(Song, on_delete=models.CASCADE)
    content= models.CharField(max_length=700)
    home= models.IntegerField()
