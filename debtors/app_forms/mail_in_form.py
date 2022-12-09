from django import forms
from ..app_models import Mail_In


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