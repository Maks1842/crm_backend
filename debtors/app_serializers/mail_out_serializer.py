from rest_framework import serializers
from ..app_models import Mail_Out


class Mail_OutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mail_Out
        fields = ['id', 'sequence_num', 'executive_document', 'date', 'name_doc', 'addresser', 'recipient_organisation',
                  'recipient_address', 'recipient_index', 'mass', 'gov_toll', 'trek', 'type_mail', 'type_package',
                  'type_mark', 'num_symbol', 'debtor', 'user', 'comment', 'is_deleted']