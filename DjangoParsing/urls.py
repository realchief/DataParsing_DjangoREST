from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers
from recruiting import urls


router = routers.DefaultRouter()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += urls.urlpatterns