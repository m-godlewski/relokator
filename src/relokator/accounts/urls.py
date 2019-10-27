from django.urls import path

from .views import (
    AccountRegister,
    account_info,
    account_adverts
)

urlpatterns = [
    path('register/',AccountRegister.as_view(), name='signup'),
    path('<str:account_id>/info', account_info),
    path('<str:account_id>/adverts', account_adverts)
]