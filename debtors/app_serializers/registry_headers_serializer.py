from rest_framework import serializers
from ..app_models import Registry_Headers


class Registry_HeadersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registry_Headers
        fields = ['id', 'headers', 'name_field', 'turn', 'redactor']