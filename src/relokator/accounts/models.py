from django.db import models
from django.contrib.auth.models import(
    BaseUserManager, AbstractBaseUser
)

"""
    W trakcie tworzenia
"""
class Account(AbstractBaseUser):
    name = models.CharField(max_length=100, blank=False, verbose_name="Imię")
    surname = models.CharField(max_length=100, blank=True, verbose_name="Nazwisko")
    email = models.EmailField(max_length=100, unique=True, verbose_name="E-mail")
    accepted_terms = models.BooleanField(default=False, verbose_name="Akceptuję regulamin serwisu")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email','accepted_terms']