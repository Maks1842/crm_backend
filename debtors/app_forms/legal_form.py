from django import forms
from ..app_models import Legal


class LegalForm(forms.ModelForm):
    class Meta:
        model = Legal
        fields = ['debtor', 'executive_document', 'user', 'status', 'comment', 'is_deleted']
        widgets = {
            'debtor': forms.Select(attrs={"class": "form-control"}),
            'executive_document': forms.Select(attrs={"class": "form-control"}),
            'user': forms.Select(attrs={"class": "form-control"}),
            'status': forms.Select(attrs={"class": "form-control"}),
            'comment': forms.TextInput(attrs={"class": "form-control"}),
            'is_deleted': forms.Select(attrs={"class": "form-control"}),
        }