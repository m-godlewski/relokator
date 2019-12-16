from django import forms
from .models import Company


class CompanyCreateForm(forms.Form):

    name = forms.CharField(label="Nazwa firmy", required=True)
    location = forms.CharField(label="Obszar działania firmy", max_length=100, required=True)


class CompanyModelForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ["name", "location", "logo", "tariff"]

