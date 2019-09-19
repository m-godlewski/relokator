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
    '''Model ogłoszenia

    user [id] - użytkownik wystawiający ogłoszenie
    title [str] - tytuł ogłoszenia
    content [str] - opis ogłoszenia]
    category [str] - kategoria ogłoszenia (dom, miekszanie lub pokój)
    create_date [datetime] - data wystawienia ogłoszenia
    city [str] - miasto
    address [str] - adres (ulica i numer mieszkania/domu)
    prize [str] - cena
    image [imagefield] - zdjęcie #TODO dodaj możliwość dodania kilku zdjęć
    '''

    CATEGORY_CHOICES = (
        ('Dom', 'Dom'),
        ('Mieszkanie', 'Mieszkanie'),
        ('Pokój', 'Pokój')
    )

    slug = models.SlugField(null=True, blank=True)
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    content = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    create_date = models.DateTimeField(default=timezone.now)
    city = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=100, blank=False)
    prize = models.CharField(max_length=10, blank=False)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    objects = AdvertManager()

    def get_absolute_url(self):
        return f"/adverts/{self.id}"

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"