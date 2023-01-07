import pandas as pd

from rest_framework.permissions import IsAdminUser

from ..app_models import *
from rest_framework import generics, viewsets, status, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action, permission_classes
from drf_yasg2.utils import swagger_auto_schema, unset
from drf_yasg2 import openapi
from django.db import IntegrityError, transaction

'''Импорт данных из файлов CSV в DataBase'''

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


class ImportFromCSVAPIView(APIView):
    @swagger_auto_schema(
        method='get',
        tags=['Импорт из CSV'],
        operation_description="Импортировать реестр должников", )
    @action(detail=False, methods=['get'])
    def get(self, request):
        x = import_csv()

        return Response({"data": x})







def import_csv():
    csv_file = pd.read_csv("./data/baza_1.csv")
    # csv_file.to_json("./data/data.json")
    return csv_file


#
#
# class OrganisationPersonsAPIView(APIView):
#     permission_classes = [IsAdminUser]
#     @swagger_auto_schema(
#         methods=['get'],
#         tags=['Представитель организации'],
#         operation_description="Получить представителя организации",
#         manual_parameters=[
#             openapi.Parameter('id_organisation', openapi.IN_QUERY, description="Идентификатор организации",
#                               type=openapi.TYPE_INTEGER),
#         ])
#     @action(methods=['get'], detail=False)
#     def get(self, request):
#         organisation = request.query_params.get('id_organisation')
#         persons = Form_Organisation_Persons.objects.filter(organisation_id=organisation)
#         result = []
#         if len(persons) > 0:
#             for item in persons:
#                 result.append({
#                     'id': item.person_id,
#                     'name': f"{item.person.last_name} {item.person.first_name} {item.person.second_name or ''}"
#                 })
#         return Response({'data': result})
#
#     @swagger_auto_schema(
#         methods=['post'],
#         tags=['Представитель организации'],
#         operation_description="Добавить представителя организации",
#         request_body=openapi.Schema(
#             type=openapi.TYPE_OBJECT,
#             properties={
#                 'id_organisation': openapi.Schema(type=openapi.TYPE_INTEGER, description='Идентификатор организации'),
#                 'first_name': openapi.Schema(type=openapi.TYPE_STRING, description='Имя'),
#                 'second_name': openapi.Schema(type=openapi.TYPE_STRING, description='Отчество'),
#                 'last_name': openapi.Schema(type=openapi.TYPE_STRING, description='Фамилия'),
#                 'position': openapi.Schema(type=openapi.TYPE_STRING, description='Должность'),
#                 'phone': openapi.Schema(type=openapi.TYPE_STRING, description='Телефон'),
#                 'email': openapi.Schema(type=openapi.FORMAT_EMAIL, description='Эл. почта'),
#             }
#         ))
#     @action(methods=['post'], detail=True)
#     # @transaction.atomic
#     def post(self, request):
#         req_data = request.data
#
#         # .pop()ищет указанный ключ (аналогично .get(), но), возвращает и удаляет его, если он найден, иначе генерируется исключение.
#         id_org = req_data.pop('id_organisation')
#         serializers = Organisation_PersonsSerializer(data=req_data)
#         fio = f"{req_data['last_name']} {req_data['first_name']} {req_data['second_name'] or ''}"
#         serializers.is_valid(raise_exception=True)
#         error = "Не удалось добавить представителя!"
#         try:
#             with transaction.atomic():
#                 res = serializers.save()
#                 data = {'organisation': id_org, 'person': res.pk}
#                 serializers_person = Form_Organisation_PersonsSerializer(data=data)
#                 serializers_person.is_valid(raise_exception=True)
#                 serializers_person.save()
#                 return Response({'data': {'id': res.pk, 'name': fio}})
#         except IntegrityError as exception:
#             if 'violates unique constraint' in exception.args[0]:
#                 error = f"{error} Такой человек уже существует."
#             return Response({'error': error})