from rest_framework import serializers
from ..app_models import Imported_Registry


class Imported_RegistrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Imported_Registry
        fields = ['id', 'name', 'date', 'registry', 'comment']