from django import forms
from ..app_models import Mail_Out


class Mail_OutForm(forms.ModelForm):
    class Meta:
        model = Mail_Out
        fields = ['sequence_num', 'executive_document', 'date', 'name_doc', 'addresser', 'recipient_organisation',
                  'recipient_address', 'recipient_index', 'mass', 'gov_toll', 'trek', 'type_mail', 'type_package',
                  'type_mark', 'num_symbol', 'debtor', 'user', 'comment', 'is_deleted']
        widgets = {
            'sequence_num': forms.TextInput(attrs={"class": "form-control"}),
            'executive_document': forms.Select(attrs={"class": "form-control"}),
            'date': forms.DateInput(attrs={"class": "form-control"}),
            'name_doc': forms.TextInput(attrs={"class": "form-control"}),
            'addresser': forms.TextInput(attrs={"class": "form-control"}),
            'recipient_organisation': forms.TextInput(attrs={"class": "form-control"}),
            'recipient_address': forms.TextInput(attrs={"class": "form-control"}),
            'recipient_index': forms.TextInput(attrs={"class": "form-control"}),
            'mass': forms.TextInput(attrs={"class": "form-control"}),
            'gov_toll': forms.TextInput(attrs={"class": "form-control"}),
            'trek': forms.TextInput(attrs={"class": "form-control"}),
            'type_mail': forms.Select(attrs={"class": "form-control"}),
            'type_package': forms.Select(attrs={"class": "form-control"}),
            'type_mark': forms.Select(attrs={"class": "form-control"}),
            'num_symbol': forms.TextInput(attrs={"class": "form-control"}),
            'debtor': forms.Select(attrs={"class": "form-control"}),
            'user': forms.Select(attrs={"class": "form-control"}),
            'comment': forms.TextInput(attrs={"class": "form-control"}),
            'is_deleted': forms.Select(attrs={"class": "form-control"}),
        }