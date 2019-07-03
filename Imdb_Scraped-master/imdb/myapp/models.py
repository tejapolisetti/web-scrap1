# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_id=models.IntegerField()
    name = models.CharField(max_length=100)
    rating  = models.FloatField()
    cast  = models.CharField(max_length=1000)
