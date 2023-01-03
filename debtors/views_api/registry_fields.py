import re

from rest_framework.permissions import IsAdminUser

from ..app_models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from ..app_serializers.debtors_serializer import DebtorsSerializer
from rest_framework import generics, viewsets, status, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action, permission_classes
from rest_framework.viewsets import GenericViewSet
from drf_yasg2.utils import swagger_auto_schema, unset
from drf_yasg2 import openapi

'''
GetRegistryFieldsAPIView - извлекаю название полей всех моделей, составляющих реестр должников.
 - Извлекаю все headers.
 
'''

"""ОГРАНИЧЕНИЯ ДОСТУПА:
Дефолтные permissions:
AllowAny - полный доступ;
IsAdminUser - только для Администраторов;
IsAuthenticated - только для авторизованных пользователей;
IsAuthenticatedOrReadOnly - только для авторизованных или всем, но для чтения.

Кастомные permissions:
IsAdminOrReadOnly - запись может просматривать любой, а удалять только Администратор;
IsOwnerAndAdminOrReadOnly - запись может менять только пользователь который её создал и Админ, просматривать может любой.
"""


class GetRegistryFieldsAPIView(APIView):
    @swagger_auto_schema(
        method='get',
        tags=['Поля реестра должников'],
        operation_description="Получить список полей всех моделей для реестра",)
    @action(detail=False, methods=['get'])
    def get(self, request):

        models = [Collection_Debt, Credits, Debtors, Data_from_ROSP_Execut_Product, Executive_Documents,
                  Executive_Productions, Legal, Pyments]

        result = []
        for m in models:
            model_fields = m._meta.local_fields
            model_name = m._meta.object_name

            field_names = []
            for f in model_fields:
                if m._meta.get_field(f'{f.name}').get_internal_type() != 'ForeignKey' and \
                        m._meta.get_field(f'{f.name}').get_internal_type() != 'BooleanField':
                    field_names.append(f.name)

            result.append({f'{model_name}': field_names})

        return Response({'data': result})


class GetHeadersAPIView(APIView):
    @swagger_auto_schema(
        method='get',
        tags=['Поля реестра должников'],
        operation_description="Получить список заголовков реестра",)
    @action(detail=False, methods=['get'])
    def get(self, request):

        queryset = Registry_Headers.objects.values_list('headers_key').order_by('turn')

        headers = []
        for q in queryset:
            headers.append(q[0])

        return Response({"data": headers})