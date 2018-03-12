
from django.conf.urls import url, include
from rest_framework import routers
# from compounding_dashboard.home import views
from rest_framework.authtoken import views as auth_views
from recruiting import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api/parser', views.Parser.as_view()),
    url(r'^api/vacancies/.*?$', views.Parser.as_view()),
    ]