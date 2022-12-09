from django import forms
from ..app_models import Data_from_ROSP_Execut_Product


class Data_from_ROSP_Execut_ProductForm(forms.ModelForm):
    class Meta:
        model = Data_from_ROSP_Execut_Product
        fields = ['number', 'debtor', 'date_on', 'date_end', 'reason_end', 'curent_debt', 'summa_debt',
                  'gov_toll', 'repay', 'object_ep', 'executive_document', 'rosp', 'address_rosp', 'pristav',
                  'pristav_phone', 'date_request']
        widgets = {
            'number': forms.TextInput(attrs={"class": "form-control"}),
            'debtor': forms.TextInput(attrs={"class": "form-control"}),
            'date_on': forms.DateInput(attrs={"class": "form-control"}),
            'date_end': forms.DateInput(attrs={"class": "form-control"}),
            'reason_end': forms.TextInput(attrs={"class": "form-control"}),
            'curent_debt': forms.TextInput(attrs={"class": "form-control"}),
            'summa_debt': forms.TextInput(attrs={"class": "form-control"}),
            'gov_toll': forms.TextInput(attrs={"class": "form-control"}),
            'repay': forms.TextInput(attrs={"class": "form-control"}),
            'object_ep': forms.TextInput(attrs={"class": "form-control"}),
            'executive_document': forms.TextInput(attrs={"class": "form-control"}),
            'rosp': forms.TextInput(attrs={"class": "form-control"}),
            'address_rosp': forms.TextInput(attrs={"class": "form-control"}),
            'pristav': forms.TextInput(attrs={"class": "form-control"}),
            'pristav_phone': forms.TextInput(attrs={"class": "form-control"}),
            'date_request': forms.DateInput(attrs={"class": "form-control"}),
        }