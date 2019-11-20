from django.urls import path

from .views import (
    company_create_view,
    company_detail_view,
    company_browse_view,
    company_update_view,
    company_delete_view,
)

urlpatterns = [
    path("", company_browse_view),
    path("<str:company_id>/", company_detail_view),
    path("<str:company_id>/edit", company_update_view),
]
