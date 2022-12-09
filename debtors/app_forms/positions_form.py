from django import forms
from ..app_models import Positions


class PositionsForm(forms.ModelForm):
    class Meta:
        model = Positions
        fields = ['name', 'is_deleted']
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'is_deleted': forms.Select(attrs={"class": "form-control"}),
        }