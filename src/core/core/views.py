from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    context = {
        'title':'Home'
    }
    return render(request, 'home.html', context)


def login(request):
    context = {
        'title':'Logowanie'
    }
    return render(request, 'user/login.html', context)


def register(request):
    context = {
        'title':'Rejestracja'
    }
    return render(request, 'user/register.html', context)


def account(request):
    context = {
        'title':'Moje konto'
    }
    return render(request, 'user/account.html', context)