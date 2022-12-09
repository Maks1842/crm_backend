from rest_framework import serializers
from ..app_models import Collection_Debt


class Collection_DebtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection_Debt
        fields = ['id', 'department_of_presentation', 'name_department', 'address_department', 'executive_document',
                  'date_presentation', 'date_return', 'reason_end', 'comment', 'is_deleted']