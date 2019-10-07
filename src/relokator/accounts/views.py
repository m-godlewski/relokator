from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from django.db.models import Q

from adverts.models import Advert


class Registration(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/account_register.html'


def account_info(request, account_id):
    template_name = 'accounts/account_info.html'
    context = {
        'username':account_id,
    }
    return render(request, template_name, context) 


def account_adverts(request, account_id):
    template_name = 'accounts/account_adverts.html'
    if request.user.is_authenticated:
        qs = Advert.objects.filter(Q(user=request.user)) # TODO not request user, but user profile

    context = {
        'username': account_id,
        'object_list': qs
    }
    return render(request, template_name, context) 