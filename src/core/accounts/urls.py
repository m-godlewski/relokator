from django.urls import path

from .views import (
    Registration,
    account_info,
    account_adverts
)


urlpatterns = [
    path('register/',Registration.as_view(), name='signup'),
    path('<str:account_id>/', account_info),
    path('<str:account_id>/adverts', account_adverts)
]