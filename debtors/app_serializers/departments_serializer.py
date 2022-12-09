from rest_framework import serializers
from ..app_models import Departments


class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ['id', 'name', 'is_deleted']