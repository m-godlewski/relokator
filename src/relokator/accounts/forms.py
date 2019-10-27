from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from core import settings
from .models import Account


class AccountCreationForm(UserCreationForm):

    username = forms.CharField(max_length=50, required=True, label="Nazwa użytkownika")
    email = forms.EmailField(max_length=100, required=True, label="E-mail")
    name = forms.CharField(max_length=100, required=True, label="Imię")
    surname = forms.CharField(max_length=100, required=False, label="Nazwisko")
    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$', max_length=20, required=True, label="Numer telefonu")
    
    def __init__(self, *args, **kwargs):
        super(AccountCreationForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = Account
        fields = ('username', 'name', 'surname', 'email', 'phone_number', 'profile_image')


class AccountEditForm(UserChangeForm):
    class Meta:
        model = Account
        fields = ('name', 'surname', 'email', 'phone_number', 'profile_image')