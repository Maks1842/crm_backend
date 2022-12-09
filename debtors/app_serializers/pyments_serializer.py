from rest_framework import serializers
from ..app_models import Pyments


class PymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pyments
        fields = ['id', 'debtor', 'executive_document', 'date', 'summa', 'payment_doc_num', 'comment', 'is_deleted']