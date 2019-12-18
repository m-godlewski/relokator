import sys, logging
from django.shortcuts import render
from adverts.models import Advert
from .models import SearchQuery


def get_search_parameters(request) -> dict:
    """ retrieving search parameters from http request
    
    Arguments:
        request {[object]} -- [http request]
    
    Returns:
        parameters {dict} -- [dictionary contains search query parameters]
        
    """

    parameters = {}

    # advert category
    parameters["category"] = request.GET.get("category", None)

    # advert type
    parameters["advert_type"] = request.GET.get("advert_type", None)

    # advert furnished
    parameters["furnished"] = request.GET.get("furnished", None)
    if parameters["furnished"] == "Tak":
        parameters["furnished"] = True
    elif parameters["furnished"] == "Nie":
        parameters["furnished"] = False

    # advert minimal price
    parameters["price_min"] = request.GET.get("price_min", 0)
    if parameters["price_min"] == "":
        parameters["price_min"] = 0

    # advert maximum price
    parameters["price_max"] = request.GET.get("price_max", 0)
    if parameters["price_max"] == "":
        parameters["price_max"] = int(sys.maxsize) - 1

    # Location priority 0
    parameters["location_priority"] = request.GET.get("location_priority", None)
    # Location priority radius 0
    parameters["location_priority_radius"] = request.GET.get(
        "location_priority_radius", None
    )

    # Location priority 1
    parameters["location_priority_1"] = request.GET.get("location_priority_1", None)
    # Location priority radius 1
    parameters["location_priority_radius_1"] = request.GET.get(
        "location_priority_radius_1", None
    )

    # Location priority 2
    parameters["location_priority_2"] = request.GET.get("location_priority_2", None)
    # Location priority radius 2
    parameters["location_priority_radius_2"] = request.GET.get(
        "location_priority_radius_2", None
    )

    return parameters


def search_view(request):
    """ advert search view
    
    Arguments:
        request {[object]} -- [http request]
    
    Returns:
        rendering template contains adverts fulfilling search query parameters

    """

    # value from city input in search form
    query = request.GET.get("q", None)

    # parameters from search form
    parameters = get_search_parameters(request)

    # checking if user is logged in or not
    if request.user.is_authenticated:
        user = request.user
    else:
        user = None

    # preparing base context dictionary
    context = {"query": query, "parameters": parameters}

    if query is not None:

        # filtering by base parameters
        SearchQuery.objects.create(user=user, query=query)
        adverts_list = Advert.objects.search(query=query, parameters=parameters)

        # filtering by location priorities if any location parameters are given
        if parameters['location_priority'] or parameters['location_priority_1'] or parameters['location_priority_2']:
            adverts_list = SearchQuery.location.filter_list_of_adverts(
                list(adverts_list),
                parameters["location_priority"],
                parameters["location_priority_radius"],
            )
        
        # setting adverts fulfilling all parameters to context dictionary
        context["adverts_list"] = adverts_list
        context["counter"] = len(adverts_list)

    return render(request, "searches/search-view.html", context)
