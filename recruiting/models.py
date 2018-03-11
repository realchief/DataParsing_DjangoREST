
from __future__ import unicode_literals

from django.db.models.signals import post_save
from django.dispatch import receiver
# from rest_framework.authtoken.models import Token
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.


class Vacancy(models.Model):
    is_active = models.CharField(blank=False, max_length=100)
    title = models.CharField(blank=False, max_length=100)
    location = models.CharField(blank=False, max_length=100)
    description = models.CharField(blank=False, max_length=100)
    starts_at = models.DateField(blank=False)
    ends_at = models.DateField(blank=False)


class Company(models.Model):
    name = models.CharField(blank=False, max_length=100)
    location = models.CharField(blank=False, max_length=100)
    image_list = models.CharField(blank=False, max_length=200)


class City(models.Model):
    location = models.CharField(blank=False, max_length=100)

