from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import AccountCreationForm, AccountUpdateForm
from .models import Account


class AccountAdmin(UserAdmin):
    """
        Class overwrites default user class of Django
    """

    add_form = AccountCreationForm
    form = AccountUpdateForm
    model = Account


admin.site.register(Account, AccountAdmin)