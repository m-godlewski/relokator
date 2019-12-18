from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    """
        Model of account

    username [integer] -  user name
    first_name [char] - name
    last_name [char] - surname
    join_date [date] - registration date
    email [char] - e-mail
    phone_number [char] - phone number
    profile_image [image] - profile photo

    """

    username = models.CharField(max_length=50, unique=True, verbose_name="Nazwa użytkownika")
    first_name = models.CharField(max_length=100, unique=False, blank=False, verbose_name="Imię")
    last_name = models.CharField(max_length=100, unique=False, blank=True, verbose_name="Nazwisko")
    join_date = models.DateTimeField(default=timezone.now)
    email = models.EmailField(max_length=100, unique=True, blank=False, verbose_name="E-mail")
    phone_number = models.CharField(max_length=20, unique=True, blank=False, verbose_name="Numer telefonu")
    profile_image = models.ImageField(
        upload_to="profile_images/",
        blank=True,
        null=True,
        verbose_name="Zdjęcie profilowe",
    )

    # field used to login
    USERNAME_FIELD = "username"

    # required fields during registration
    REQUIRED_FIELDS = ["first_name", "email", "phone_number"]

    def get_absolute_url(self):
        """ method returns absolute url of account
        
        Returns:
            absolute url of account
        """
        return f"/accounts/{self.id}"

    def get_info_url(self):
        """ method returns url of account information
        
        Returns:
            url of account information
        """
        return f"{self.get_absolute_url()}/info"

    def get_adverts_url(self):
        """ method returns url of account adverts
        
        Returns:
            url of account adverts
        """
        return f"{self.get_absolute_url()}/adverts"

    def get_companies_url(self):
        """ method returns url of account companies
        
        Returns:
            url of account comapnies
        """
        return f"{self.get_absolute_url()}/adverts"

    def get_update_url(self):
        """ method returns url of account settings
        
        Returns:
            url of account settings
        """
        return f"{self.get_absolute_url()}/settings"
