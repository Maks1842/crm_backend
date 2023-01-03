from django.urls import path, include, re_path
from .views import *
from rest_framework import routers

from rest_framework import permissions
from drf_yasg2.views import get_schema_view
from drf_yasg2 import openapi

from .views_api.registry_fields import GetRegistryFieldsAPIView, GetHeadersAPIView
from .views_api.tests import GetDebtorsAPIView

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.SimpleRouter()

#V1 Основной вариант
urlpatterns = [
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^api/v1/auth/', include('djoser.urls.authtoken')),

    path('swagger.json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('', index, name='home'),
    path('api/v1/getDebtors/', GetDebtorsAPIView.as_view(), name='getDebtors'),
    path('api/v1/getRegistryFields/', GetRegistryFieldsAPIView.as_view(), name='GetRegistryFields'),
    path('api/v1/getHeaders/', GetHeadersAPIView.as_view(), name='GetHeaders'),
]