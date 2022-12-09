from rest_framework import serializers
from ..app_models import Executive_Documents


class Executive_DocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Executive_Documents
        fields = ['id', 'type_ed', 'number', 'date', 'case_number', 'date_of_receipt_ed', 'date_decision',
                  'status_ed', 'credit', 'user', 'comment', 'is_deleted']