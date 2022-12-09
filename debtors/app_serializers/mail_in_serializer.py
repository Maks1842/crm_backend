from rest_framework import serializers
from ..app_models import Mail_In


class Mail_InSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mail_In
        fields = ['id', 'sequence_num', 'debtor', 'status_ed', 'date', 'addresser', 'name_doc', 'legal', 'comment', 'is_deleted']