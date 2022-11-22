from .models import *
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'department', 'position', 'birthday', 'is_deleted']


class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'name', 'is_deleted']


class PositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'name', 'is_deleted']


class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'name', 'list', 'comment', 'is_deleted']


class CessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'name', 'number', 'date', 'summa', 'cedent', 'cessionari', 'date_old_cession', 'is_deleted']


class DebtorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'name_1', 'name_2', 'pol', 'birthday', 'place_of_birth', 'passport_series', 'passport_num',
                  'passport_date', 'passport_department', 'inn', 'snils', 'address_1', 'address_2', 'index_add_1',
                  'index_add_2', 'comment', 'is_deleted']


class CreditsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'creditor', 'number', 'date_start', 'date_ent', 'summa', 'interest_rate', 'overdue_od',
                  'overdue_percent', 'penalty', 'percent_of_od', 'gov_toll', 'debtor', 'cession', 'comment',
                  'is_deleted']


class Executive_DocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'type_ed', 'number', 'date', 'case_number', 'date_of_receipt_ed', 'date_decision',
                  'status_ed', 'credit', 'user', 'comment', 'is_deleted']


class Executive_ProductionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'number', 'date_on', 'date_end', 'reason_end', 'curent_debt',
                  'summa_debt', 'date_request', 'executive_document', 'comment', 'is_deleted']


class Collection_DebtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'department_of_presentation', 'name_department', 'address_department', 'executive_document',
                  'date_presentation', 'date_return', 'reason_end', 'comment', 'is_deleted']


class Data_from_ROSP_Execut_ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'number', 'debtor', 'date_on', 'date_end', 'reason_end', 'curent_debt', 'summa_debt',
                  'gov_toll', 'repay', 'object_ep', 'executive_document', 'rosp', 'address_rosp', 'pristav',
                  'pristav_phone', 'date_request']


class PymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'debtor', 'executive_document', 'date', 'summa', 'payment_doc_num', 'comment', 'is_deleted']


class LegalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'debtor', 'executive_document', 'user', 'status', 'comment', 'is_deleted']


class Mail_InSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'sequence_num', 'debtor', 'status_ed', 'date', 'addresser', 'name_doc', 'legal', 'comment', 'is_deleted']


class Mail_OutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'sequence_num', 'executive_document', 'date', 'name_doc', 'addresser', 'recipient_organisation',
                  'recipient_address', 'recipient_index', 'mass', 'gov_toll', 'trek', 'type_mail', 'type_package',
                  'type_mark', 'num_symbol', 'debtor', 'user', 'comment', 'is_deleted']


class Transaction_ExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'model', 'field', 'old_data', 'new_data', 'date_exchange', 'user']