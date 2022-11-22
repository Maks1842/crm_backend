from django import forms
# from .models import Category         # для работы с Формами, НЕ связанные с Моделями
from .models import *                  # для работы с Формами, связанные с Моделями
# import re
# from django.core.exceptions import ValidationError
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['department', 'position', 'birthday', 'is_deleted']
        widgets = {
            'department': forms.Select(attrs={"class": "form-control"}),
            'position': forms.Select(attrs={"class": "form-control"}),
            'birthday': forms.DateInput(attrs={"class": "form-control"}),
            'is_deleted': forms.TextInput(attrs={"class": "form-control"}),
        }


class DepartmentsForm(forms.ModelForm):
    class Meta:
        model = Departments
        fields = ['name', 'is_deleted']
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'is_deleted': forms.Select(attrs={"class": "form-control"}),
        }


class PositionsForm(forms.ModelForm):
    class Meta:
        model = Positions
        fields = ['name', 'is_deleted']
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'is_deleted': forms.Select(attrs={"class": "form-control"}),
        }


class LibraryForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = ['name', 'list', 'comment', 'is_deleted']
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'list': forms.TextInput(attrs={"class": "form-control"}),
            'comment': forms.TextInput(attrs={"class": "form-control"}),
            'is_deleted': forms.Select(attrs={"class": "form-control"}),
        }


class CessionForm(forms.ModelForm):
    class Meta:
        model = Cession
        fields = ['name', 'number', 'date', 'summa', 'cedent', 'cessionari', 'date_old_cession', 'is_deleted']
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'number': forms.TextInput(attrs={"class": "form-control"}),
            'date': forms.DateInput(attrs={"class": "form-control"}),
            'summa': forms.TextInput(attrs={"class": "form-control"}),
            'cedent': forms.TextInput(attrs={"class": "form-control"}),
            'cessionari': forms.TextInput(attrs={"class": "form-control"}),
            'date_old_cession': forms.TextInput(attrs={"class": "form-control"}),
            'is_deleted': forms.Select(attrs={"class": "form-control"}),
        }


class DebtorsForm(forms.ModelForm):
    class Meta:
        model = Debtors
        fields = ['name_1', 'name_2', 'pol', 'birthday', 'place_of_birth', 'passport_series', 'passport_num',
                  'passport_date', 'passport_department', 'inn', 'snils', 'address_1', 'address_2', 'index_add_1',
                  'index_add_2', 'comment', 'is_deleted']
        widgets = {
            'name_1': forms.TextInput(attrs={"class": "form-control"}),
            'name_2': forms.TextInput(attrs={"class": "form-control"}),
            'pol': forms.DateInput(attrs={"class": "form-control"}),
            'birthday': forms.DateInput(attrs={"class": "form-control"}),
            'place_of_birth': forms.TextInput(attrs={"class": "form-control"}),
            'passport_series': forms.TextInput(attrs={"class": "form-control"}),
            'passport_num': forms.TextInput(attrs={"class": "form-control"}),
            'passport_date': forms.TextInput(attrs={"class": "form-control"}),
            'passport_department': forms.TextInput(attrs={"class": "form-control"}),
            'inn': forms.TextInput(attrs={"class": "form-control"}),
            'snils': forms.DateInput(attrs={"class": "form-control"}),
            'address_1': forms.TextInput(attrs={"class": "form-control"}),
            'address_2': forms.TextInput(attrs={"class": "form-control"}),
            'index_add_1': forms.TextInput(attrs={"class": "form-control"}),
            'index_add_2': forms.TextInput(attrs={"class": "form-control"}),
            'comment': forms.TextInput(attrs={"class": "form-control"}),
            'is_deleted': forms.Select(attrs={"class": "form-control"}),
        }


class CreditsForm(forms.ModelForm):
    class Meta:
        model = Credits
        fields = ['creditor', 'number', 'date_start', 'date_ent', 'summa', 'interest_rate', 'overdue_od',
                  'overdue_percent', 'penalty', 'percent_of_od', 'gov_toll', 'debtor', 'cession', 'comment',
                  'is_deleted']
        widgets = {
            'creditor': forms.TextInput(attrs={"class": "form-control"}),
            'number': forms.TextInput(attrs={"class": "form-control"}),
            'date_start': forms.DateInput(attrs={"class": "form-control"}),
            'date_ent': forms.DateInput(attrs={"class": "form-control"}),
            'summa': forms.TextInput(attrs={"class": "form-control"}),
            'interest_rate': forms.TextInput(attrs={"class": "form-control"}),
            'overdue_od': forms.TextInput(attrs={"class": "form-control"}),
            'overdue_percent': forms.TextInput(attrs={"class": "form-control"}),
            'penalty': forms.TextInput(attrs={"class": "form-control"}),
            'percent_of_od': forms.TextInput(attrs={"class": "form-control"}),
            'gov_toll': forms.DateInput(attrs={"class": "form-control"}),
            'debtor': forms.Select(attrs={"class": "form-control"}),
            'cession': forms.Select(attrs={"class": "form-control"}),
            'comment': forms.TextInput(attrs={"class": "form-control"}),
            'is_deleted': forms.Select(attrs={"class": "form-control"}),
        }


class Executive_DocumentsForm(forms.ModelForm):
    class Meta:
        model = Executive_Documents
        fields = ['type_ed', 'number', 'date', 'case_number', 'date_of_receipt_ed', 'date_decision',
                  'status_ed', 'credit', 'user', 'comment', 'is_deleted']
        widgets = {
            'type_ed': forms.TextInput(attrs={"class": "form-control"}),
            'number': forms.TextInput(attrs={"class": "form-control"}),
            'date': forms.DateInput(attrs={"class": "form-control"}),
            'case_number': forms.TextInput(attrs={"class": "form-control"}),
            'date_of_receipt_ed': forms.DateInput(attrs={"class": "form-control"}),
            'date_decision': forms.DateInput(attrs={"class": "form-control"}),
            'status_ed': forms.TextInput(attrs={"class": "form-control"}),
            'credit': forms.Select(attrs={"class": "form-control"}),
            'user': forms.Select(attrs={"class": "form-control"}),
            'comment': forms.TextInput(attrs={"class": "form-control"}),
            'is_deleted': forms.Select(attrs={"class": "form-control"}),
        }


class Executive_ProductionsForm(forms.ModelForm):
    class Meta:
        model = Executive_Productions
        fields = ['number', 'date_on', 'date_end', 'reason_end', 'curent_debt',
                  'summa_debt', 'date_request', 'executive_document', 'comment', 'is_deleted']
        widgets = {
            'number': forms.TextInput(attrs={"class": "form-control"}),
            'date_on': forms.DateInput(attrs={"class": "form-control"}),
            'date_end': forms.DateInput(attrs={"class": "form-control"}),
            'reason_end': forms.TextInput(attrs={"class": "form-control"}),
            'curent_debt': forms.TextInput(attrs={"class": "form-control"}),
            'summa_debt': forms.TextInput(attrs={"class": "form-control"}),
            'date_request': forms.TextInput(attrs={"class": "form-control"}),
            'executive_document': forms.Select(attrs={"class": "form-control"}),
            'comment': forms.TextInput(attrs={"class": "form-control"}),
            'is_deleted': forms.Select(attrs={"class": "form-control"}),
        }


class Collection_DebtForm(forms.ModelForm):
    class Meta:
        model = Collection_Debt
        fields = ['department_of_presentation', 'name_department', 'address_department', 'executive_document',
                  'date_presentation', 'date_return', 'reason_end', 'comment', 'is_deleted']
        widgets = {
            'department_of_presentation': forms.Select(attrs={"class": "form-control"}),
            'name_department': forms.TextInput(attrs={"class": "form-control"}),
            'address_department': forms.DateInput(attrs={"class": "form-control"}),
            'executive_document': forms.Select(attrs={"class": "form-control"}),
            'date_presentation': forms.DateInput(attrs={"class": "form-control"}),
            'date_return': forms.DateInput(attrs={"class": "form-control"}),
            'reason_end': forms.TextInput(attrs={"class": "form-control"}),
            'comment': forms.TextInput(attrs={"class": "form-control"}),
            'is_deleted': forms.Select(attrs={"class": "form-control"}),
        }


class Data_from_ROSP_Execut_ProductForm(forms.ModelForm):
    class Meta:
        model = Data_from_ROSP_Execut_Product
        fields = ['number', 'debtor', 'date_on', 'date_end', 'reason_end', 'curent_debt', 'summa_debt',
                  'gov_toll', 'repay', 'object_ep', 'executive_document', 'rosp', 'address_rosp', 'pristav',
                  'pristav_phone', 'date_request']
        widgets = {
            'number': forms.TextInput(attrs={"class": "form-control"}),
            'debtor': forms.TextInput(attrs={"class": "form-control"}),
            'date_on': forms.DateInput(attrs={"class": "form-control"}),
            'date_end': forms.DateInput(attrs={"class": "form-control"}),
            'reason_end': forms.TextInput(attrs={"class": "form-control"}),
            'curent_debt': forms.TextInput(attrs={"class": "form-control"}),
            'summa_debt': forms.TextInput(attrs={"class": "form-control"}),
            'gov_toll': forms.TextInput(attrs={"class": "form-control"}),
            'repay': forms.TextInput(attrs={"class": "form-control"}),
            'object_ep': forms.TextInput(attrs={"class": "form-control"}),
            'executive_document': forms.TextInput(attrs={"class": "form-control"}),
            'rosp': forms.TextInput(attrs={"class": "form-control"}),
            'address_rosp': forms.TextInput(attrs={"class": "form-control"}),
            'pristav': forms.TextInput(attrs={"class": "form-control"}),
            'pristav_phone': forms.TextInput(attrs={"class": "form-control"}),
            'date_request': forms.DateInput(attrs={"class": "form-control"}),
        }


class PymentsForm(forms.ModelForm):
    class Meta:
        model = Pyments
        fields = ['debtor', 'executive_document', 'date', 'summa', 'payment_doc_num', 'comment', 'is_deleted']
        widgets = {
            'debtor': forms.Select(attrs={"class": "form-control"}),
            'executive_document': forms.Select(attrs={"class": "form-control"}),
            'date': forms.DateInput(attrs={"class": "form-control"}),
            'summa': forms.TextInput(attrs={"class": "form-control"}),
            'payment_doc_num': forms.TextInput(attrs={"class": "form-control"}),
            'comment': forms.TextInput(attrs={"class": "form-control"}),
            'is_deleted': forms.Select(attrs={"class": "form-control"}),
        }


class LegalForm(forms.ModelForm):
    class Meta:
        model = Legal
        fields = ['debtor', 'executive_document', 'user', 'status', 'comment', 'is_deleted']
        widgets = {
            'debtor': forms.Select(attrs={"class": "form-control"}),
            'executive_document': forms.Select(attrs={"class": "form-control"}),
            'user': forms.Select(attrs={"class": "form-control"}),
            'status': forms.Select(attrs={"class": "form-control"}),
            'comment': forms.TextInput(attrs={"class": "form-control"}),
            'is_deleted': forms.Select(attrs={"class": "form-control"}),
        }


class Mail_InForm(forms.ModelForm):
    class Meta:
        model = Mail_In
        fields = ['sequence_num', 'debtor', 'status_ed', 'date', 'addresser', 'name_doc', 'legal', 'comment', 'is_deleted']
        widgets = {
            'sequence_num': forms.TextInput(attrs={"class": "form-control"}),
            'debtor': forms.Select(attrs={"class": "form-control"}),
            'status_ed': forms.TextInput(attrs={"class": "form-control"}),
            'date': forms.DateInput(attrs={"class": "form-control"}),
            'addresser': forms.TextInput(attrs={"class": "form-control"}),
            'name_doc': forms.TextInput(attrs={"class": "form-control"}),
            'legal': forms.Select(attrs={"class": "form-control"}),
            'comment': forms.TextInput(attrs={"class": "form-control"}),
            'is_deleted': forms.Select(attrs={"class": "form-control"}),
        }


class Mail_OutForm(forms.ModelForm):
    class Meta:
        model = Mail_Out
        fields = ['sequence_num', 'executive_document', 'date', 'name_doc', 'addresser', 'recipient_organisation',
                  'recipient_address', 'recipient_index', 'mass', 'gov_toll', 'trek', 'type_mail', 'type_package',
                  'type_mark', 'num_symbol', 'debtor', 'user', 'comment', 'is_deleted']
        widgets = {
            'sequence_num': forms.TextInput(attrs={"class": "form-control"}),
            'executive_document': forms.Select(attrs={"class": "form-control"}),
            'date': forms.DateInput(attrs={"class": "form-control"}),
            'name_doc': forms.TextInput(attrs={"class": "form-control"}),
            'addresser': forms.TextInput(attrs={"class": "form-control"}),
            'recipient_organisation': forms.TextInput(attrs={"class": "form-control"}),
            'recipient_address': forms.TextInput(attrs={"class": "form-control"}),
            'recipient_index': forms.TextInput(attrs={"class": "form-control"}),
            'mass': forms.TextInput(attrs={"class": "form-control"}),
            'gov_toll': forms.TextInput(attrs={"class": "form-control"}),
            'trek': forms.TextInput(attrs={"class": "form-control"}),
            'type_mail': forms.Select(attrs={"class": "form-control"}),
            'type_package': forms.Select(attrs={"class": "form-control"}),
            'type_mark': forms.Select(attrs={"class": "form-control"}),
            'num_symbol': forms.TextInput(attrs={"class": "form-control"}),
            'debtor': forms.Select(attrs={"class": "form-control"}),
            'user': forms.Select(attrs={"class": "form-control"}),
            'comment': forms.TextInput(attrs={"class": "form-control"}),
            'is_deleted': forms.Select(attrs={"class": "form-control"}),
        }


class Transaction_ExchangeForm(forms.ModelForm):
    class Meta:
        model = Transaction_Exchange
        fields = ['model', 'field', 'old_data', 'new_data', 'user']
        widgets = {
            'model': forms.TextInput(attrs={"class": "form-control"}),
            'field': forms.TextInput(attrs={"class": "form-control"}),
            'old_data': forms.TextInput(attrs={"class": "form-control"}),
            'new_data': forms.TextInput(attrs={"class": "form-control"}),
            'user': forms.Select(attrs={"class": "form-control"}),
        }