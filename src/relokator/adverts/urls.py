from django.urls import path
from .views import(
    advert_detail_view,
    advert_browse_view,
    advert_update_view,
    advert_delete_view,
)

urlpatterns = [
    path('', advert_browse_view),
    path('<str:advert_id>/', advert_detail_view),
    path('<str:advert_id>/edit', advert_update_view),
    path('<str:advert_id>/delete', advert_delete_view)
]