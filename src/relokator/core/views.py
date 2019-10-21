from django.http import HttpResponse
from django.shortcuts import render

from adverts.models import Advert


def home(request):
    qs = Advert.objects.all().order_by('-create_date')[:6] # 6 najnowszych ogłoszeń
    context = {
        'qs':qs
    }
    return render(request, 'website/home.html', context)