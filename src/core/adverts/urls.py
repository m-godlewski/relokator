from django.urls import path
from .views import(
    advert_detail_view
)

urlpatterns = [
    path('<str:advert_id>/', advert_detail_view)
]