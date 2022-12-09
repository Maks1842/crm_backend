from django import forms
from ..app_models import Transaction_Exchange


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