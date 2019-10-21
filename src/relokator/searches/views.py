from django.shortcuts import render
from adverts.models import Advert
from .models import SearchQuery
import sys


def get_search_parameters(request):

    parameters = {}
    parameters['category'] = request.GET.get('category', None)
    parameters['advert_type'] = request.GET.get('advert_type', None)

    # umeblowanie
    parameters['furnished'] = request.GET.get('furnished', False)
    if parameters['furnished'] == "Tak":
        parameters['furnished'] = True
    elif parameters['furnished'] == "Nie":
        parameters['furnished'] = False

    # cena minimalna
    parameters['price_min'] = request.GET.get('price_min', 0)
    if parameters['price_min'] == '':
        parameters['price_min'] = 0

    # cena maksymalna
    parameters['price_max'] = request.GET.get('price_max', 0)
    if parameters['price_max'] == '':
        parameters['price_max'] = int(sys.maxsize) - 1

    return parameters


def search_view(request):
    query = request.GET.get('q', None )
    parameters = get_search_parameters(request)

    if request.user.is_authenticated:
        user = request.user
    else:
        user = None

    context = {
        'query' : query,
        'parameters' : parameters
    }

    if query is not None:
        SearchQuery.objects.create(user=user, query=query)
        adverts_list = Advert.objects.search(query=query, parameters=parameters)
        context['adverts_list'] = adverts_list
        context['counter'] = len(adverts_list)

    return render(request, 'searches/search-view.html', context)
