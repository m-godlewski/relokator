from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.db.models import Q

from accounts.models import Account
from adverts.models import Advert
from .forms import AccountCreationForm


class AccountRegister(CreateView):
    form_class = AccountCreationForm
    success_url = reverse_lazy("login")
    template_name = "accounts/account_register.html"


def account_info(request, account_id):
    template_name = 'accounts/account_info.html'
    user = Account.objects.get(username=account_id)
    qs = Advert.objects.filter(Q(user=user))
    context = {
        'username':account_id,
        'user': user
    }
    return render(request, template_name, context) 


def account_adverts(request, account_id):
    template_name = 'accounts/account_adverts.html'
    user = Account.objects.get(username=account_id)
    qs = Advert.objects.filter(Q(user=user))
    context = {
        'username': account_id,
        'object_list': qs
    }
    return render(request, template_name, context)