from django.urls import path

from .views import (
    account_create_view,
    account_info_view,
    account_adverts_view,
    account_companies_view,
    account_update_view,
)

urlpatterns = [
    # account registration url
    path("register/", account_create_view),
    # account information url
    path("<str:account_id>/info", account_info_view),
    # account adverts url
    path("<str:account_id>/adverts", account_adverts_view),
    # account companies url
    path("<str:account_id>/companies", account_companies_view),
    # account settings url 
    path("<str:account_id>/settings", account_update_view),
]