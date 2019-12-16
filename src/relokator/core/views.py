from django.shortcuts import render
from adverts.models import Advert


def home(request):
    """ home view
    
    Arguments:
        request {[object]} -- [http request]
    
    Returns:
        Rendering home page with list of six latest created adverts.

    """

    # getting 6 latest created by users adverts
    qs = Advert.objects.all().order_by("-create_date")[:6]

    context = {"qs": qs}

    return render(request, "website/home.html", context)
