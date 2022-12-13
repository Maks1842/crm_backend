from rest_framework import serializers
from ..app_models import Credits


class CreditsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credits
        fields = ['id', 'creditor', 'number', 'date_start', 'date_end', 'summa', 'interest_rate', 'overdue_od',
                  'overdue_percent', 'penalty', 'percent_of_od', 'gov_toll', 'debtor', 'cession', 'comment',
                  'is_deleted']