from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    context = {
        'title':'Home'
    }
    return render(request, 'home.html', context)
