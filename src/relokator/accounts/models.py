from django.db import models
from django.contrib.auth.models import(
    BaseUserManager, AbstractBaseUser
)



class Account(AbstractBaseUser):
    email = models.EmailField(max_length=100, unique=True, verbose_name="E-mail")
    name = models.CharField(max_length=100, blank=False, verbose_name="Imię")
    surname = models.CharField(max_length=100, blank=True, verbose_name="Nazwisko")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['']