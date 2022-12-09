from django import forms
from ..app_models import Executive_Documents


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