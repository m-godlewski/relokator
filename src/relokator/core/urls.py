from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from .views import home
from adverts.views import advert_create_view
from searches.views import search_view


urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), # login (django auth app)
    path('accounts/', include('accounts.urls')), # sign in (accounts app)
    path('adverts/new', advert_create_view), # advert creation
    path('adverts/', include('adverts.urls')), # advert app
    path('search/', search_view) 
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)