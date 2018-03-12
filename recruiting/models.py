
from __future__ import unicode_literals

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.


class Vacancy(models.Model):

    is_active = models.CharField(blank=False, max_length=100)
    title = models.CharField(blank=False, max_length=100)
    description = models.CharField(blank=False, max_length=100)


class Company(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    name = models.CharField(blank=False, max_length=100)
    image_list = models.CharField(blank=False, max_length=200)


class City(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    location = models.CharField(blank=False, max_length=100)

