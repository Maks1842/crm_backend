from django import forms
from ..app_models import Debtors


class DebtorsForm(forms.ModelForm):
    class Meta:
        model = Debtors
        fields = ['last_name_1', 'first_name_1', 'second_name_1', 'last_name_2', 'first_name_2', 'second_name_2', 'pol', 'birthday', 'place_of_birth', 'passport_series', 'passport_num',
                  'passport_date', 'passport_department', 'inn', 'snils', 'address_1', 'address_2', 'index_add_1',
                  'index_add_2', 'comment', 'is_deleted']
        widgets = {
            'last_name_1': forms.TextInput(attrs={"class": "form-control"}),
            'first_name_1': forms.TextInput(attrs={"class": "form-control"}),
            'second_name_1': forms.TextInput(attrs={"class": "form-control"}),
            'last_name_2': forms.TextInput(attrs={"class": "form-control"}),
            'first_name_2': forms.TextInput(attrs={"class": "form-control"}),
            'second_name_2': forms.TextInput(attrs={"class": "form-control"}),
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