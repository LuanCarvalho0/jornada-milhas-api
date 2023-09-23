
from django.contrib import admin
from django.urls import path, include
from jornada_milhas.views import DepoimentosViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('depoimentos', DepoimentosViewSet, basename='Depoimentos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
