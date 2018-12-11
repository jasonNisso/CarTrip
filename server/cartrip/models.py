# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime
# reporter=1 article =many report goes into article so the field that is inside the other autos pou mpainei einai 1
# Create your models here.
class Engine(models.Model) :
    title = models.CharField(max_length=200)
    engine_cubic_centimeters = models.CharField(max_length=20)
    engine_manufacturer = models.CharField(max_length=20)
    def __str__(self):
        return self.title
#Location in progress
class Location(models.Model) :
    location_address = models.CharField(max_length=200)
    map_location = models.CharField(max_length=200)

class Car(models.Model) :
    company = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    year = models.IntegerField('year', default=0)
    color = models.CharField(max_length=200)
    engine = models.ForeignKey(Engine, on_delete=models.CASCADE, blank=True) #in case of a car with two engines this will need to change
    extra_information = models.CharField(max_length=500, null=True, blank=True)
    def __str__(self):
        return "%s %s %s" % (self.company, self.model, self.year)
    #maybe i can manage photos with photologue django
    #car_image =
class Exhibition(models.Model) :
    title = models.CharField(max_length=200, unique=True)
    location = models.ManyToManyField(Location)
    date = models.DateTimeField('exhibitionDate')
    cars = models.ManyToManyField(Car)
    description = models.TextField(max_length=800, blank=True, null=True)
    price = models.IntegerField('price', default=0)
    def __str__(self):
        return self.title
class Excursion(models.Model) :
    title = models.CharField(max_length=200, unique=True)
    location = models.ManyToManyField(Location)
    date = models.DateTimeField('excursionDate')
    price = models.IntegerField('price', default=0)
    cars = models.ManyToManyField(Car)
    def __str__(self):
        return self.title
class Bundle(models.Model) :
    title = models.CharField(max_length=200, unique=True)
    exhibitions = models.ManyToManyField(Exhibition)
    excursion = models.ManyToManyField(Excursion)
    date = models.DateTimeField('BundleDates')
    price = models.IntegerField('price', default=0)
    def __str__(self):
        return self.title
#class Like(models.Model) :
    #recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    #giver = models.ForeignKey(User, on_delete=models.CASCADE)

class Post(models.Model) :
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(default='Post')
    #likes = models.ManyToManyField(Like)
    post_date = models.DateTimeField(auto_now=True )
class Comment(models.Model) :
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.TextField(default='Comment')
    comment_date = models.DateTimeField(auto_now=True)