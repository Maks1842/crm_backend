from rest_framework import serializers
from ..app_models import Legal


class LegalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Legal
        fields = ['id', 'debtor', 'executive_document', 'user', 'status', 'comment', 'is_deleted']