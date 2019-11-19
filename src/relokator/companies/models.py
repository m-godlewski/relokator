from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL


class Company(models.Model):
    """Model firmy przeprowadzkowej

    user [integer] - użytkownik będący właścicielem firmy
    name [char] - nazwa firmy
    location [char] - obszar działania firmy
    logo [image] - logo firmy
    """

    user = models.ForeignKey(User, default=1, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True, blank=False, verbose_name="Nazwa")
    location = models.CharField(max_length=100, unique=False, blank=False, verbose_name="Lokacja")
    logo = models.ImageField(upload_to="company_logo/", blank=True, null=True, verbose_name="Logo")

    def get_absolute_url(self):
        return f"/companies/{self.id}"

    def get_update_url(self):
        return f"{self.get_absolute_url()}/edit"