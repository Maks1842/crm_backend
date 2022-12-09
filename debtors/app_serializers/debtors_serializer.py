from rest_framework import serializers
from ..app_models import Debtors


class DebtorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debtors
        fields = ['id', 'last_name_1', 'first_name_1', 'second_name_1', 'last_name_2', 'first_name_2', 'second_name_2',
                  'pol', 'birthday', 'place_of_birth', 'passport_series', 'passport_num', 'passport_date',
                  'passport_department', 'inn', 'snils', 'address_1', 'address_2', 'index_add_1',
                  'index_add_2', 'comment', 'is_deleted']