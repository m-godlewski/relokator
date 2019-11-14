from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from accounts.models import Account
from adverts.models import Advert
from companies.models import Company
from .forms import AccountCreationForm, AccountUpdateForm


# CREATE
def account_create_view(request):
    template_name = "accounts/account-create.html"
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
    user = Account.objects.get(username=account_id)
    qs = Advert.objects.filter(Q(user=user))

    context = {
        "title": f"Profil użytkownika {account_id}",
        "username": account_id,
        "user": user,
    }
    return render(request, template_name, context)


def account_adverts_view(request, account_id):
    template_name = "accounts/account-adverts.html"
    user = Account.objects.get(username=account_id)
    qs = Advert.objects.filter(Q(user=user))

    context = {
        "title": f"Ogłoszenia użytkownika {account_id}",
        "username": account_id,
        "object_list": qs,
    }
    return render(request, template_name, context)


def account_companies_view(request, account_id):
    template_name = "accounts/account-companies.html"
    user = Account.objects.get(username=account_id)
    company = get_object_or_404(Company, user=user)

    context = {
        "title": f"Firma użytkownika {account_id}",
        "username": account_id,
        "company": company,
    }
    return render(request, template_name, context)


# UPDATE
@login_required
def account_update_view(request, account_id):
    template_name = "accounts/account-update.html"
    user = Account.objects.get(username=account_id)
    form = AccountUpdateForm(request.POST or None, instance=user)

    if request.user.username != user.username:
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
