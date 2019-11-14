from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from .views import home
from adverts.views import advert_create_view
from companies.views import company_create_view
from searches.views import search_view


urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), # login (django auth app)
    path('accounts/', include('accounts.urls')), # sign in and others (accounts app)
    path('adverts/new', advert_create_view), # advert app creation
    path('adverts/', include('adverts.urls')), # advert app
    path('companies/new', company_create_view), # company app creation
    path('companies/', include('companies.urls')), # company app
    path('search/', search_view) # search app
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)