from django.shortcuts import render
from adverts.models import Advert
from .models import SearchQuery


def get_search_parameters(request):
    parameters = {}
    parameters['category'] = request.GET.get('category', None)
    parameters['advert_type'] = request.GET.get('advert_type', None)
    parameters['furnished'] = request.GET.get('furnished', False)
    return parameters


def search_view(request):
    query = request.GET.get('q', None )
    parameters = get_search_parameters(request)

    if request.user.is_authenticated:
        user = request.user

    context = {
        'query' : query,
        'parameters' : parameters
    }

    if query is not None:
        SearchQuery.objects.create(user=user, query=query)
        adverts_list = Advert.objects.search(query=query, parameters=parameters)
        context['adverts_list'] = adverts_list

    return render(request, 'searches/search-view.html', context)
