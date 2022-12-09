from rest_framework import serializers
from ..app_models import Positions


class PositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Positions
        fields = ['id', 'name', 'is_deleted']