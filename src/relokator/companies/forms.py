from django import forms
from .models import Company
from django.forms.widgets import ClearableFileInput


class CompanyModelForm(forms.ModelForm):
    """
        class of form used for create and upated company objects
    """

    # clearing logo and tariff image in settings
    class ClearableFileInput(ClearableFileInput):
        initial_text = 'Obecne'
        input_text = 'Nowe'
        clear_checkbox_label = 'Wyczyść'

    logo = forms.ImageField(label='Select Profile Image',required = False, widget=ClearableFileInput)
    tariff = forms.ImageField(label='Select Profile Image',required = False, widget=ClearableFileInput)

    class Meta:
        model = Company
        fields = ["name", "location", "logo", "tariff"]
