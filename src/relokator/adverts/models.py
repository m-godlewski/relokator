from django.conf import settings
from django.db import models
from django.db.models import Q
from django.utils import timezone

from maps.models import GoogleMaps


User = settings.AUTH_USER_MODEL


class AdvertQuerySet(models.QuerySet):
    """ 
        class used for making base search query to db
    """
    
    def search(self, query:str, parameters:dict):
        """ method making query to db based of given (based) parameters
        
        Arguments:
            query {[str]} -- [city of searched advert]
            parameters {dict} -- [dictionary of searched parameters]
        
        Returns:
            return list of adverts filtred by given parameters

        """

        # dict containing base search parameters
        filters = {}
        if parameters["category"]:
            filters["category"] = parameters["category"]
        if parameters["advert_type"]:
            filters["advert_type"] = parameters["advert_type"]
        if parameters["furnished"] is not None:
            filters["furnished"] = parameters["furnished"]

        # making search query and returns result
        return self.filter(
            **filters,
            city=query,
            price__gte=parameters["price_min"],
            price__lte=parameters["price_max"],
        )


class AdvertManager(models.Manager):
    """
        class used for manage Advert model objects
    """
    
    def get_queryset(self):
        """ method getting AdvertQuerySet object
        
        Returns:
            AdvertQuerySet object

        """
        return AdvertQuerySet(self.model, using=self._db)

    def search(self, query:str=None, parameters:dict=None):
        """ making search in db base on AdvertQuerySet object
        
        Keyword Arguments:
            query {[str]} -- [city of searched adverts] (default: {None})
            parameters {[dict]} -- [base parameters of searched adverts] (default: {None})
        
        Returns:
            [type] -- [description]
        """
        
        if query is None:
            return self.get_queryset().none()
        
        return self.get_queryset().search(query, parameters)


class Advert(models.Model):
    """

        Advert class model

        user [integer] - owner of advert
        title [char] - advert title
        content [char] - advert description
        category [char] - advert category
        advert_type [char] - advert type
        create_date [datetime] - timestamp of advert creation
        furnished [boolean] - furnished of advert
        city [char] - city
        address [char] - adres (street and number)
        price [integer] - price
        image [image] - advert photo

    """

    objects = AdvertManager()   # advert manager, used for search
    location = GoogleMaps()     # adver google maps location object

    CATEGORY_CHOICES = (
        ("Dom", "Dom"),
        ("Mieszkanie", "Mieszkanie"),
        ("Pokój", "Pokój"),
    )

    TYPE_CHOICES = (
        ("Wynajem", "Wynajem"), 
        ("Sprzedaż", "Sprzedaż")
    )

    slug = models.SlugField(null=True, blank=True)
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, verbose_name="Tytuł")
    content = models.TextField(null=True, blank=True, verbose_name="Opis")
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, verbose_name="Kategoria")
    advert_type = models.CharField(max_length=10, choices=TYPE_CHOICES, verbose_name="Typ")
    create_date = models.DateTimeField(default=timezone.now)
    furnished = models.BooleanField(default=False, verbose_name="Umeblowanie")
    city = models.CharField(max_length=100, blank=False, verbose_name="Miasto")
    address = models.CharField(max_length=100, blank=False, verbose_name="Adres")
    price = models.PositiveIntegerField(blank=False, null=False, verbose_name="Cena")
    image = models.ImageField(upload_to="images/", blank=True, null=True, verbose_name="Zdjęcia")

    # location fields
    map_url = models.CharField(max_length=200, default="") # google maps url
    map_coord_x = models.FloatField(default=0)  # longitude
    map_coord_y = models.FloatField(default=0)  # latitude

    def save(self, *args, **kwargs):
        # saving google maps url created by google maps object to model field 
        self.map_url = self.location.get_location_map_url(self.city, self.address)
        # saving longitude and latitude of advert location
        self.map_coord_x, self.map_coord_y = self.location.get_location_coords(self.city, self.address)
        # overriding base saving function
        super(Advert, self).save(*args, **kwargs)

    def get_absolute_url(self) -> str:
        """ method retrieving absolute url of advert object
        
        Returns:
            absolute url of advert object
        """
        return f"/adverts/{self.id}"

    def get_update_url(self) -> str:
        """ method retrieving edit url of advert object
        
        Returns:
            edit url of advert object
        """
        return f"{self.get_absolute_url()}/edit"

    def get_delete_url(self) -> str:
        """ method retrieving delete url of advert object
        
        Returns:
            delete url of advert object
        """
        return f"{self.get_absolute_url()}/delete"
