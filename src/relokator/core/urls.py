from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from .views import home
from adverts.views import advert_create_view
from companies.views import company_create_view
from searches.views import search_view


urlpatterns = [
    # home page view
    path("", home),
    # administration panel
    path("admin/", admin.site.urls),
    # login (django.auth)
    path("accounts/", include("django.contrib.auth.urls")),
    # account app (registration and account management)
    path("accounts/", include("accounts.urls")),
    # advert app - creation view
    path("adverts/new", advert_create_view),
    # advert app
    path("adverts/", include("adverts.urls")),
    # company app - creation view
    path("companies/new", company_create_view),
    # company app
    path("companies/", include("companies.urls")),
    # search app
    path("search/", search_view),
]


# setting media url if running in debug mode
if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
