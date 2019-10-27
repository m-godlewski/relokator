from django.conf import settings
from django.db import models
from django.db.models import Q
from django.utils import timezone


User = settings.AUTH_USER_MODEL


class AdvertQuerySet(models.QuerySet):

    def search(self, query, parameters):
        filters = {}
        if parameters['category']:
            filters['category'] = parameters['category']
        if parameters['advert_type']:
            filters['advert_type'] = parameters['advert_type']
        if parameters['furnished']:
            filters['furnished'] = parameters['furnished']
 
        return self.filter(
            **filters,
            city = query,
            price__gte = parameters['price_min'],
            price__lte = parameters['price_max']
        )


class AdvertManager(models.Manager):

    def get_queryset(self):
        return AdvertQuerySet(self.model, using=self._db)

    def search(self, query=None, parameters=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().search(query, parameters)


class Advert(models.Model):
    '''Model ogłoszenia

    user [integer] - użytkownik wystawiający ogłoszenie
    title [char] - tytuł ogłoszenia
    content [char] - opis ogłoszenia]
    category [char] - kategoria ogłoszenia (dom, miekszanie lub pokój)
    advert_type [char] - typ ogłoszenia (wynajem, sprzedaż)
    create_date [datetime] - data wystawienia ogłoszenia
    furnished [boolean] - umeblowanie
    city [char] - miasto
    address [char] - adres (ulica i numer mieszkania/domu)
    price [integer] - cena
    image [image] - zdjęcie #TODO dodaj możliwość dodania kilku zdjęć
    '''

    CATEGORY_CHOICES = (
        ('Dom', 'Dom'),
        ('Mieszkanie', 'Mieszkanie'),
        ('Pokój', 'Pokój')
    )

    TYPE_CHOICES = (
        ('Wynajem', 'Wynajem'),
        ('Sprzedaż', 'Sprzedaż')
    )

    slug = models.SlugField(null=True, blank=True)
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120, verbose_name='Tytuł')
    content = models.TextField(null=True, blank=True, verbose_name='Opis')
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, verbose_name='Kategoria')
    advert_type = models.CharField(max_length=10, choices=TYPE_CHOICES, verbose_name='Typ')
    create_date = models.DateTimeField(default=timezone.now)
    furnished = models.BooleanField(default=False, verbose_name='Umeblowanie')
    city = models.CharField(max_length=100, blank=False, verbose_name='Miasto')
    address = models.CharField(max_length=100, blank=False, verbose_name='Adres')
    price = models.PositiveIntegerField(blank=False, null=False, verbose_name='Cena')
    image = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name='Zdjęcia')

    objects = AdvertManager()

    def get_absolute_url(self):
        return f"/adverts/{self.id}"

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"