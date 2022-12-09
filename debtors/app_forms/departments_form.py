from django import forms
from ..app_models import Departments


class DepartmentsForm(forms.ModelForm):
    class Meta:
        model = Departments
        fields = ['name', 'is_deleted']
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'is_deleted': forms.Select(attrs={"class": "form-control"}),
        }