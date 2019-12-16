from django.db import models
from django.conf import settings

from maps.models import GoogleMaps


class SearchQuery(models.Model):
    """ search query model
    
        user {[object]} -- [user making query]
        query {[string]} -- [string from city input from search form]
        location {[object]} -- [GoogleMaps object responsible for filtering adverts by location priority]

    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL)
    query = models.CharField(max_length=100)
    location = GoogleMaps()