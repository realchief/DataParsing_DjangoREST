from .models import Vacancy, Company, City

from recruiting.serializers import VacancySerializer
from recruiting.serializers import CompanySerializer
from recruiting.serializers import CitySerializer

from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from rest_framework import status
from lxml import html


class Parser(APIView):

    def get(self, request):

        start_requests = 'https://www.trainee.de/traineestellen/'
        r = requests.get(start_requests)
        dom = html.fromstring(r.text)

        try:
            Company.objects.all().delete()
            City.objects.all().delete()
            Vacancy.objects.all().delete()

            for index in range(0, 80, 4):

                title = dom.xpath('//div[@id="jobs"]//ul/li')[index].xpath('.//h4//text()')
                company_name = dom.xpath('//div[@id="jobs"]//ul/li')[index].xpath('.//span//text()')
                image_list = dom.xpath('//div[@id="jobs"]//ul/li')[index].xpath('.//img//@src')
                location = dom.xpath('//div[@id="jobs"]//ul/li')[index].xpath('.//ul[@class="tr-list tr-mrgv"]//text()')

                if title:
                    title = str(title[0])
                else:
                    title = ''

                if company_name:
                    company_name = str(company_name[0])
                else:
                    company_name = ''

                if image_list:
                    image_list = str(image_list[0])
                else:
                    image_list = ''

                if location:
                    location = str(location[9]).replace('\n', '').replace(' ', '')
                else:
                    location = ''

                vacancy = Vacancy.objects.create(
                    is_active="true",
                    title=title,
                    description='description'
                )

                Company.objects.create(name=company_name, image_list=image_list, vacancy=vacancy)

                City.objects.create(location=location, vacancy=vacancy)

            return Response("Inserting Success", status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": e}, status=status.HTTP_200_OK)


class Display(APIView):

    def get(self, request):
        locationkey = request.GET.get('location')
        vacancy = VacancySerializer(Vacancy.objects.filter(city__location=locationkey), many=True)
        return Response({"data": vacancy.data}, status=status.HTTP_200_OK)









