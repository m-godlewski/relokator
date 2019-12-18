from django import forms
from .models import Company


class CompanyModelForm(forms.ModelForm):
    """
        class of form used for create and upated company objects
    """

    class Meta:
        model = Company
        fields = ["name", "location", "logo", "tariff"]
