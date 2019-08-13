from django.urls import path
from .views import(
    advert_list_view
)

urlpatterns = [
    path('', advert_list_view)
]