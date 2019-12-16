from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL


class Company(models.Model):
    """ 
        Class of relocation company

        user [integer] - company owner
        name [char] - company name
        location [char] - company working area
        logo [image] - company logo

    """

    user = models.ForeignKey(User, default=1, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True, blank=False, verbose_name="Nazwa")
    location = models.CharField(max_length=100, unique=False, blank=False, verbose_name="Lokacja")
    logo = models.ImageField(upload_to="company_logo/", blank=True, null=True, verbose_name="Logo")
    tariff = models.ImageField(upload_to="company_tariff/", blank=True, null=True, verbose_name="Cennik")

    def get_absolute_url(self) -> str:
        """ method returning absolute url for company

        Returns:
            absolute url for company

        """
        return f"/companies/{self.id}"

    def get_update_url(self) -> str:
        """ method returning update url for company
        
        Returns:
            edit url for company

        """
        return f"{self.get_absolute_url()}/edit"