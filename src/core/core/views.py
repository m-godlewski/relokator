from django.http import HttpResponse
from django.shortcuts import render

from adverts.models import Advert


def home(request):
    qs = Advert.objects.all()
    context = {
        'qs':qs
    }
    return render(request, 'home.html', context)