from django.http import HttpResponse
from django.shortcuts import render

from adverts.models import Advert


def home(request):
    qs = Advert.objects.all().order_by('-create_date')
    context = {
        'qs':qs
    }
    return render(request, 'website/home.html', context)