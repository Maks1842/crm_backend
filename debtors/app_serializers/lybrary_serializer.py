from rest_framework import serializers
from ..app_models import Library


class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = ['id', 'name', 'list', 'comment', 'is_deleted']