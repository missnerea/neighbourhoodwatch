from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.

class Neighbourhood(models.Model):
    neighbourhoodid = models.CharField(max_length=255, primary_key=True, db_column='neighbourhoodID', blank=True)
    name = models.CharField(max_length=60)
    location = models.CharField(max_length=60)
    occupants_count = models.CharField(max_length=60)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name


class Business(models.Model):
    businessid = models.CharField(max_length=255, primary_key=True, db_column='businessID', blank=True)
    name = models.CharField(max_length=30)
    emailaddress = models.CharField(max_length=60)
    user = models.ForeignKey(User)
    neighbourhoodid = models.ForeignKey(Neighbourhood,null=True,db_column='neighbourhoodID',blank=True)

    def __unicode__(self):
        return self.name