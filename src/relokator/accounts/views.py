from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import logging

from accounts.models import Account
from adverts.models import Advert
from companies.models import Company

from .forms import AccountCreationForm, AccountUpdateForm


# CREATE
def account_create_view(request):
    template_name = "accounts/account-create.html"

    # get empty creation form
    form = AccountCreationForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        obj = form.save(commit=False)
        form.save()
        form = AccountCreationForm()

    context = {"form": form}
    return render(request, template_name, context)


# RETRIEVE
def account_info_view(request, account_id):
    template_name = "accounts/account-info.html"

    # getting account by account_id
    account = Account.objects.get(username=account_id)

    context = {
        "title": f"Profil użytkownika {account_id}",
        "username": account_id,
        "object": account,
    }
    return render(request, template_name, context)


def account_adverts_view(request, account_id):
    template_name = "accounts/account-adverts.html"

    # getting account by account_id
    account = Account.objects.get(username=account_id)

    # getting adverts of account by account_id
    adverts = Advert.objects.filter(Q(user=account))

    context = {
        "title": f"Ogłoszenia użytkownika {account_id}",
        "username": account_id,
        "object_list": adverts,
    }
    return render(request, template_name, context)


def account_companies_view(request, account_id):
    template_name = "accounts/account-companies.html"

    # getting account by account_id
    user = Account.objects.get(username=account_id)

    # getting company of account by account_id
    company = Company.objects.filter(user=user.id).first()

    context = {
        "title": f"Firma użytkownika {account_id}",
        "username": account_id,
        "object": company
    }
    return render(request, template_name, context)


# UPDATE
@login_required
def account_update_view(request, account_id):
    template_name = "accounts/account-update.html"

    # getting account object by account_id
    account = Account.objects.get(username=account_id)
    form = AccountUpdateForm(request.POST or None, instance=account)

    # if current user want to update other user account, redirect to error page
    if request.user.username != account.username:
        return render(request, "website/error_404.html")

    if form.is_valid():
        form.save()

    context = {
        "title": "Ustawienia konta",
        "form": form,
    }
    return render(request, template_name, context)


# TODO DELETE
@login_required
def account_delete_view(request):
    pass