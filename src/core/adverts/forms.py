from django import forms
from .models import Advert


class AdvertCreateForm(forms.Form):
    title = forms.CharField(label='Wpisz tytuł', required=True)
    content = forms.CharField(widget=forms.Textarea, required=True)
    city = forms.CharField(required=True)
    address = forms.CharField(required=True)


class AdvertModelForm(forms.ModelForm):
    class Meta:
        model = Advert
        fields = ['title', 'content', 'city', 'address', 'image']