from django import forms
from ..app_models import Library


class LibraryForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = ['name', 'list', 'comment', 'is_deleted']
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'list': forms.TextInput(attrs={"class": "form-control"}),
            'comment': forms.TextInput(attrs={"class": "form-control"}),
            'is_deleted': forms.Select(attrs={"class": "form-control"}),
        }