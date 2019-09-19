from django.db import models


class GoogleMaps:
    google_maps_url = "http://maps.google.com/maps"


class GoogleMapsLocation(GoogleMaps):
    
    def __init__(self, address, city):
        self.address = address
        self.city = city

    def preprocess_location_string(self):
        if ' ' in self.address:
            self.address.replace(' ', '+')
        if ' ' in self.city:
            self.city.replace(' ', '+')

    def get_location_url(self):
        self.location_url = f'{self.google_maps_url}?q={self.address}+{self.city}&output=embed'
        return self.location_url