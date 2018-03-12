
# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from recruiting.serializers import UserSerializer, GroupSerializer
from rest_framework.views import APIView
from recruiting.serializers import UserSerializer
import requests
from rest_framework.parsers import FormParser
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
        locationkey = request.path.split('/')[-1]
        start_requests = 'https://www.trainee.de/traineestellen/?search_job%5Bquery%5D=&search_job%5Blocation%' \
                         '5D=' + locationkey + '&search_job%5Bdistance%5D=25'
        r = requests.get(start_requests)
        dom = html.fromstring(r.text)
        for index in range(0, 20):
            title = str(dom.xpath('//div[@id="jobs"]//ul/li')[index].xpath('.//h4//text()')[0])
            company_name = str(dom.xpath('//div[@id="jobs"]//ul/li')[index].xpath('.//span//text()')[0])
            image_list = str(dom.xpath('//div[@id="jobs"]//ul/li')[index].xpath('.//img//@src')[0])

        print(start_requests)


