from rest_framework import serializers
from ..app_models import Data_from_ROSP_Execut_Product


class Data_from_ROSP_Execut_ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data_from_ROSP_Execut_Product
        fields = ['id', 'number', 'debtor', 'date_on', 'date_end', 'reason_end', 'curent_debt', 'summa_debt',
                  'gov_toll', 'repay', 'object_ep', 'executive_document', 'rosp', 'address_rosp', 'pristav',
                  'pristav_phone', 'date_request']