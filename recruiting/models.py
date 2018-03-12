
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save


class Vacancy(models.Model):

    is_active = models.CharField(blank=True, null=True, max_length=100)
    title = models.CharField(blank=True, null=True,  max_length=100, default='')
    description = models.CharField(blank=True, null=True,  max_length=100, default='')


class Company(models.Model):
    vacancy = models.OneToOneField(Vacancy, related_name='company')
    name = models.CharField(blank=True, null=True,  max_length=100, default='')
    image_list = models.CharField(blank=True, null=True, max_length=200, default='')


class City(models.Model):
    vacancy = models.OneToOneField(Vacancy, related_name='city')
    location = models.CharField(blank=True, null=True, max_length=100, default='')


# def create_company_city(sender, **kwargs):
#     vacancy = kwargs["instance"]
#     if kwargs['created']:
#         company = Company(vacancy=vacancy)
#         company.save()
#         city = City(vacancy=vacancy)
#         city.save()
#
#
# post_save.connect(create_company_city, sender=Vacancy)