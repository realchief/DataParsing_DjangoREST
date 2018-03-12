from rest_framework import serializers
from .models import Vacancy
from .models import Company
from .models import City


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('vacancy', 'name', 'image_list')


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('vacancy', 'location')


class VacancySerializer(serializers.ModelSerializer):
    company = CompanySerializer(required=True)
    city = CitySerializer(required=True)

    class Meta:
        model = Vacancy
        fields = ('is_active', 'title', 'description', 'company', 'city')


