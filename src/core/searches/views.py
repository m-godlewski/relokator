from django.shortcuts import render
from adverts.models import Advert
from .models import SearchQuery


def search_view(request):
    query = request.GET.get('q', None )
    user = None

    if request.user.is_authenticated:
        user = request.user

    context = {'query':query}

    if query is not None:
        SearchQuery.objects.create(user=user, query=query)
        adverts_list = Advert.objects.search(query=query)
        context['adverts_list'] = adverts_list

    return render(request, 'searches/search-view.html', context)
