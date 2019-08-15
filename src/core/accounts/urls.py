from django.urls import path

from .views import (
    Registration,
    account_info
)


urlpatterns = [
    path('register/',Registration.as_view(), name='signup'),
    path('<str:account_id>/', account_info)
]