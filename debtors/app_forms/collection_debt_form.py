from django import forms
from ..app_models import Collection_Debt


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