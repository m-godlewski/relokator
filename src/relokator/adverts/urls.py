from django.urls import path
from .views import(
    advert_detail_view,
    advert_browse_view,
    advert_update_view,
    advert_delete_view,
)

urlpatterns = [
    # all adverts browsing url
    path("", advert_browse_view),
    # url for detail view of selected advert
    path("<str:advert_id>/", advert_detail_view),
    # url for edit view of selected advert
    path("<str:advert_id>/edit", advert_update_view),
    # url for delete view of selected advert
    path("<str:advert_id>/delete", advert_delete_view)
]