from rest_framework import serializers
from ..app_models import Executive_Productions


class Executive_ProductionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Executive_Productions
        fields = ['id', 'number', 'date_on', 'date_end', 'reason_end', 'curent_debt',
                  'summa_debt', 'date_request', 'executive_document', 'comment', 'is_deleted']