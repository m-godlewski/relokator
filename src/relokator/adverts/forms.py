from django import forms
from .models import Advert


class AdvertCreateForm(forms.Form):
    """
        class of advert creation form    
    """

    title = forms.CharField(label="Wpisz tytuł", required=True, max_length=100)
    content = forms.CharField(widget=forms.Textarea, required=True)
    city = forms.CharField(required=True)
    address = forms.CharField(required=True)
    category = forms.ChoiceField(choices=Advert.CATEGORY_CHOICES, initial="Brak", required=True)
    advert_type = forms.ChoiceField(choices=Advert.TYPE_CHOICES, initial="Brak", required=True)
    furnished = forms.BooleanField(initial=False)
    price = forms.IntegerField(min_value=1, required=True)


class AdvertUpdateForm(forms.ModelForm):
    """
        class used as update form of advert model.    
    """
    
    class Meta:
        model = Advert
        fields = [
            "title",
            "content",
            "city",
            "address",
            "category",
            "advert_type",
            "furnished",
            "price",
            "image",
        ]

        widgets = {
          'content': forms.Textarea(attrs={'rows':10, 'cols':70}),
        }


class AdvertModelForm(forms.ModelForm):
    """
        class used as form of advert model.    
    """
    
    class Meta:
        model = Advert
        fields = [
            "title",
            "content",
            "city",
            "address",
            "category",
            "advert_type",
            "furnished",
            "price",
            "image",
        ]

        widgets = {
          'content': forms.Textarea(attrs={'rows':10, 'cols':70}),
        }