from rest_framework import serializers
from ..app_models import Cession


class CessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cession
        fields = ['id', 'name', 'number', 'date', 'summa', 'cedent', 'cessionari', 'date_old_cession', 'is_deleted']