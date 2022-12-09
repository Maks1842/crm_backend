from rest_framework import serializers
from ..app_models import Transaction_Exchange


class Transaction_ExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction_Exchange
        fields = ['id', 'model', 'field', 'old_data', 'new_data', 'date_exchange', 'user']