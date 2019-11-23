from django.db import models
from django.conf import settings

from maps.models import GoogleMaps


class SearchQuery(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL)
    query = models.CharField(max_length=100)
    location = GoogleMaps()