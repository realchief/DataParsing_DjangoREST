
from __future__ import unicode_literals

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User, Group

# from pygments.lexers import get_all_lexers
# from pygments.styles import get_all_styles
# LEXERS = [item for item in get_all_lexers() if item[1]]
# LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
# STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

# Create your models here.


class Vacancy(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.CharField(blank=False, max_length=100)
    title = models.CharField(blank=False, max_length=100)
    location = models.CharField(blank=False, max_length=100)
    description = models.CharField(blank=False, max_length=100)
    starts_at = models.DateField(blank=False)
    ends_at = models.DateField(blank=False)


class Company(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(blank=False, max_length=100)
    location = models.CharField(blank=False, max_length=100)
    image_list = models.CharField(blank=False, max_length=200)


class City(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    location = models.CharField(blank=False, max_length=100)

