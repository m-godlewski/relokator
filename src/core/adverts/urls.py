from django.urls import path
from .views import(
    advert_detail_view,
    advert_edit_view,
    advert_delete_view,
)

urlpatterns = [
    path('<str:advert_id>/', advert_detail_view),
    path('<str:advert_id>/edit', advert_edit_view),
    path('<str:advert_id>/delete', advert_delete_view)
]