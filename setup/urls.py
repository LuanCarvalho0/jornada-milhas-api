from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from jornada_milhas.views import DepoimentosViewSet, DepoimentosHomeViewSet, DestinosViewSet
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Jornada Milhas",
      default_version='v1',
      description="É uma API REST que disponibiliza possíveis destinos de viagem.",
      terms_of_service="#",
      contact=openapi.Contact(email="luan_carvalho1997@hotmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register('depoimentos', DepoimentosViewSet, basename='Depoimentos')
router.register('destinos', DestinosViewSet, basename='Destinos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('depoimentos-home/', DepoimentosHomeViewSet.as_view()),
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
