from django import forms
from .models import Advert


class AdvertCreateForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)


class AdvertModelForm(forms.ModelForm):
    class Meta:
        model = Advert
        fields = ['title', 'content', 'slug']