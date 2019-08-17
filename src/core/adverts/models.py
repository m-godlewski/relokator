from django.conf import settings
from django.db import models
from django.db.models import Q
from django.utils import timezone

User = settings.AUTH_USER_MODEL


class AdvertQuerySet(models.QuerySet):

    def search(self, query):
        lookup = (
                    Q(title__icontains=query) |
                    Q(content__icontains=query) |
                    Q(city__icontains=query)
                    )
        return self.filter(lookup)


class AdvertManager(models.Manager):

    def get_queryset(self):
        return AdvertQuerySet(self.model, using=self._db)

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().search(query)


class Advert(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    content = models.TextField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    create_date = models.DateTimeField(default=timezone.now)
    city = models.CharField(max_length=100, blank=False)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    objects = AdvertManager()
