from django.urls import path

from .views import (
    account_create_view,
    account_info_view,
    account_adverts_view,
    account_companies_view,
    account_update_view,
)

urlpatterns = [
    path("register/", account_create_view),
    path("<str:account_id>/info", account_info_view),
    path("<str:account_id>/adverts", account_adverts_view),
    path("<str:account_id>/companies", account_companies_view),
    path("<str:account_id>/settings", account_update_view),
]