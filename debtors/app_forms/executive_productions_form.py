from django import forms
from ..app_models import Executive_Productions


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