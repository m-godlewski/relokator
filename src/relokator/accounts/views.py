from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Q

from accounts.models import Account
from adverts.models import Advert
from .forms import AccountCreationForm, AccountUpdateForm


def account_register_view(request):

    template_name = "accounts/account_register.html"
    form = AccountCreationForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        obj = form.save(commit=False)
        form.save()
        form = AccountCreationForm()

    context = {
        "form": form
    }
    return render(request, template_name, context)


def account_info_view(request, account_id):

    template_name = 'accounts/account_info.html'
    user = Account.objects.get(username=account_id)
    qs = Advert.objects.filter(Q(user=user))

    context = {
        'username':account_id,
        'user': user
    }
    return render(request, template_name, context) 


def account_adverts_view(request, account_id):

    template_name = 'accounts/account_adverts.html'
    user = Account.objects.get(username=account_id)
    qs = Advert.objects.filter(Q(user=user))

    context = {
        'username': account_id,
        'object_list': qs
    }
    return render(request, template_name, context)

@login_required
def account_update_view(request, account_id):

    template_name = 'accounts/account_update.html'
    user = Account.objects.get(username=account_id)
    form = AccountUpdateForm(request.POST or None, instance=user)

    if request.user.username != user.username:
        return render(request, 'website/error_404.html')

    if form.is_valid():
        form.save()

    context = {
        'title': 'Ustawienia konta',
        'form': form,
    }
    return render(request, template_name, context)