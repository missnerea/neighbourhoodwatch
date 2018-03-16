from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Neighbourhood(admin.ModelAdmin):
    name = model.CharField(max_length=60)
    location = model.CharField(max_length=60)
    occupants_count = model.CharField(max_length=60)
    user = models.ForeignKey(User)