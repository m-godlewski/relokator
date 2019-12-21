from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms.widgets import ClearableFileInput

from .models import Account


class AccountCreationForm(UserCreationForm):
    """
        Form class using for account registration
    """

    username = forms.CharField(max_length=50, required=True, label="Nazwa użytkownika")
    first_name = forms.CharField(max_length=100, required=True, label="Imię")
    last_name = forms.CharField(max_length=100, required=False, label="Nazwisko")
    email = forms.EmailField(max_length=100, required=True, label="E-mail")
    phone_number = forms.RegexField(regex=r"^\+?1?\d{9,15}$", max_length=20, required=True, label="Numer telefonu")

    # overwriting of user creation function
    def __init__(self, *args, **kwargs):
        super(AccountCreationForm, self).__init__(*args, **kwargs)
        # set off password and username tips in register form
        for fieldname in ["username", "password1", "password2"]:
            self.fields[fieldname].help_text = None

    class Meta:
        model = Account
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "profile_image",
        )


class AccountUpdateForm(UserChangeForm):
    """
        Form class using for account settings
    """

    # disable editing password in user account
    password = None

    # clearing profile image field in settings
    class ClearableFileInput(ClearableFileInput):
        initial_text = 'Obecne'
        input_text = 'Nowe'
        clear_checkbox_label = 'Wyczyść'

    profile_image = forms.ImageField(label='Select Profile Image',required = False, widget=ClearableFileInput)

    class Meta:
        model = Account
        fields = ("first_name", "last_name", "email", "phone_number", "profile_image")