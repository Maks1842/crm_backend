from django import forms
from ..app_models import Cession


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