from django import forms
from ..app_models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['department', 'position', 'birthday', 'is_deleted']
        widgets = {
            'department': forms.Select(attrs={"class": "form-control"}),
            'position': forms.Select(attrs={"class": "form-control"}),
            'birthday': forms.DateInput(attrs={"class": "form-control"}),
            'is_deleted': forms.TextInput(attrs={"class": "form-control"}),
        }