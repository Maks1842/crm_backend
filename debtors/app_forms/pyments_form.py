from django import forms
from ..app_models import Pyments


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