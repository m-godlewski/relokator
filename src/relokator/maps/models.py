from django.db import models


class GoogleMapLocation:
    
    google_maps_url = "http://maps.google.com/maps"

    def __init__(self, address, city):
        self.city = city
        self.address = address
    
    def __str__(self):
        return f'{self.address} {self.city}'

    def preprocess_address(self):
        address = self.address
        city = self.city
        
        if ' ' in address:
            address = address.replace(' ', '+')
        if ' ' in city:
            address = address.replace(' ', '+')
        
        return address, city

    def get_location_url(self):
        address, city = self.preprocess_address()
        return f'{GoogleMapLocation.get_google_maps_url}?q={address}+{city}&output=embed'