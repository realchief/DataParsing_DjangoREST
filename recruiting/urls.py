
from django.conf.urls import url, include
from rest_framework import routers
from recruiting import views

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api/parser', views.Parser.as_view()),
    url(r'^api/vacancies$', views.Display.as_view()),
]