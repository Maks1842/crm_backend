from django import forms
from ..app_models import Credits


class CreditsForm(forms.ModelForm):
    class Meta:
        model = Credits
        fields = ['creditor', 'number', 'date_start', 'date_end', 'summa', 'interest_rate', 'overdue_od',
                  'overdue_percent', 'penalty', 'percent_of_od', 'gov_toll', 'debtor', 'cession', 'comment',
                  'is_deleted']
        widgets = {
            'creditor': forms.TextInput(attrs={"class": "form-control"}),
            'number': forms.TextInput(attrs={"class": "form-control"}),
            'date_start': forms.DateInput(attrs={"class": "form-control"}),
            'date_end': forms.DateInput(attrs={"class": "form-control"}),
            'summa': forms.TextInput(attrs={"class": "form-control"}),
            'interest_rate': forms.TextInput(attrs={"class": "form-control"}),
            'overdue_od': forms.TextInput(attrs={"class": "form-control"}),
            'overdue_percent': forms.TextInput(attrs={"class": "form-control"}),
            'penalty': forms.TextInput(attrs={"class": "form-control"}),
            'percent_of_od': forms.TextInput(attrs={"class": "form-control"}),
            'gov_toll': forms.DateInput(attrs={"class": "form-control"}),
            'debtor': forms.Select(attrs={"class": "form-control"}),
            'cession': forms.Select(attrs={"class": "form-control"}),
            'comment': forms.TextInput(attrs={"class": "form-control"}),
            'is_deleted': forms.Select(attrs={"class": "form-control"}),
        }