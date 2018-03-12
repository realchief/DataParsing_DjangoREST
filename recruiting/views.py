
# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render
from django.contrib.auth.models import User, Group
from .models import Vacancy, Company, City
from rest_framework import viewsets

from recruiting.serializers import UserSerializer
from recruiting.serializers import GroupSerializer
from recruiting.serializers import VacancySerializer
from recruiting.serializers import CompanySerializer
from recruiting.serializers import CitySerializer

from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from rest_framework import status
from lxml import html

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class Parser(APIView):

    def get(self, request, format=None):
        # locationkey = request.path.split('/')[-1]
        start_requests = 'https://www.trainee.de/traineestellen/'
        r = requests.get(start_requests)
        dom = html.fromstring(r.text)

        list = []

        for index in range(0, 80, 4):

            title = dom.xpath('//div[@id="jobs"]//ul/li')[index].xpath('.//h4//text()')
            company_name = dom.xpath('//div[@id="jobs"]//ul/li')[index].xpath('.//span//text()')
            image_list = dom.xpath('//div[@id="jobs"]//ul/li')[index].xpath('.//img//@src')
            location = dom.xpath('//div[@id="jobs"]//ul/li')[index].xpath('.//ul[@class="tr-list tr-mrgv"]//text()')

            if title:
                title = str(title[0])
            else:
                title = None

            if company_name:
                company_name = str(company_name[0])
            else:
                company_name = None

            if image_list:
                image_list = str(image_list[0])
            else:
                image_list = None

            if location:
                location = str(location[0])
            else:
                location = None

            json_data_Vacancy = {
                "is_active": "true",
                "title": title,
                "description": 'description'
            }

            json_data_Company = {
                "name": company_name,
                "image_list": image_list
            }

            json_data_City = {
                "location": location
            }

            serializer_Vacancy = VacancySerializer(data=json_data_Vacancy)
            serializer_Company = CompanySerializer(data=json_data_Company)
            serializer_City = CitySerializer(data=json_data_City)

        return Response("Inserting Success", status=status.HTTP_200_OK)









