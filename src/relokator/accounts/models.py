from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    """Model konta użytkownika

    username [integer] - nazwa użytkownika
    first_name [char] - imię
    last_name [char] - nazwisko
    join_date [date] - data rejestracji
    email [char] - email
    phone_number [char] - numer telefonu
    profile_image [image] - zdjęcie profilowe
    """

    username = models.CharField(max_length=50, unique=True, verbose_name="Nazwa użytkownika")
    first_name = models.CharField(max_length=100, unique=False, blank=False, verbose_name="Imię")
    last_name = models.CharField(max_length=100, unique=False, blank=True, verbose_name="Nazwisko")
    join_date = models.DateTimeField(default=timezone.now)
    email = models.EmailField(max_length=100, unique=True, verbose_name="E-mail")
    phone_number = models.CharField(max_length=20, unique=True, blank=False, verbose_name="Numer telefonu")
    profile_image = models.ImageField(
        upload_to="profile_images/",
        blank=True,
        null=True,
        verbose_name="Zdjęcie profilowe",
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["first_name", "email", "phone_number"]

    def get_absolute_url(self):
        return f"/accounts/{self.id}"

    def get_info_url(self):
        return f"{self.get_absolute_url()}/info"

    def get_adverts_url(self):
        return f"{self.get_absolute_url()}/adverts"

    def get_companies_url(self):
        return f"{self.get_absolute_url()}/adverts"

    def get_update_url(self):
        return f"{self.get_absolute_url()}/settings"
