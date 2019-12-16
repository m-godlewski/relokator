import requests, logging
from django.db import models
from typing import Iterable


class GoogleMaps(object):
    """
        Google Maps class

        Main purposes of this class are:
        - constructing a url's for google maps services,
        - retrieving longitude and latitude of given address from google geocoding api
        - filtering lists of adverts by object type and radius using google places api

    """

    # google maps url, used for displaying location in google maps
    GOOGLE_MAPS_URL = "http://maps.google.com/maps"

    # google geocoding url, used for retrieving x and y of address
    GOOGLE_GEOCODING_URL = "https://maps.googleapis.com/maps/api/geocode/json"

    # google places url, used for search objects nearby location
    GOOGLE_PLACE_URL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

    
    def preprocess_address(self, city:str, address:str) -> str:
        """ address preprocessing method

        Arguments:
            city {[string]} -- [city of advert]
            address {[string]} -- [street and number of advert]
        
        Returns:
            convert address and city parameter to word plus joined string

        """
        return f'{address} {city}'


    def get_location_map_url(self, city:str, address:str) -> str:
        """ method getting google maps url based on preprocess address string

        Arguments:
            city {[string]} -- [city of advert]
            address {[string]} -- [street and number of advert]
        
        Returns:
            returning google maps url that show location given in parameters

        """
        return f'{self.GOOGLE_MAPS_URL}?q={self.preprocess_address(city, address)}&output=embed'


    def get_location_coords(self, city:str, address:str) -> int:
        """ function requesting for x and y coords of location from google geocoding api

        Arguments:
            city {[string]} -- [city of advert]
            address {[string]} -- [street and number of advert]
        
        Returns:
            x = longitude, y = latitude of location given in arguments.

        """

        try:

            # google geocoding api request
            response = requests.get(
                url = self.GOOGLE_GEOCODING_URL,
                params = {
                    # preprocessing adress
                    'address': self.preprocess_address(city, address), 
                    # api key # TODO storing in DB for security!
                    'key': 'AIzaSyC5rVKcoTfCep0GE7wnJc56P0ZfNbuLto8'
                }
            )

            # retrieving x(longitude) and y(latitude) coords from request
            geocode_data = response.json()
            x = geocode_data['results'][0]['geometry']['location']['lng']
            y = geocode_data['results'][0]['geometry']['location']['lat']

        except Exception as e:
            logging.error(f'GoogleMaps.get_location_coords() error -> {e}')
        else:
            return x, y


    def filter_list_of_adverts(self, list_of_adverts:Iterable[object], object_type:str, radius:str) -> Iterable[object]:
        """ function filtering given list of adverts by location priority given by user

        Arguments:
            list_of_adverts {[list[string]]} -- [list of adverts to filtering]
            object_type {[string]} -- [type of object to sort list_of_adverts by]
            radius {[string]} -- [maximum possible distance between object and advert]
        
        Returns:
            x = longitude, y = latitude of location given in arguments.

        """

        try:

            # list of adverts matching location criteria given by user
            filtred_list_of_adverts = []

            for advert in list_of_adverts:

                # google places api request
                response = requests.get(
                    url = self.GOOGLE_PLACE_URL,
                    params = {
                        'location': f'{advert.map_coord_y},{advert.map_coord_x}',
                        'type': object_type,
                        'radius': radius,
                        'key': 'AIzaSyC5rVKcoTfCep0GE7wnJc56P0ZfNbuLto8'
                    }
                )

                search_data = response.json()
                locations = [location["name"] for location in search_data["results"]]

                # if advert matching location cirteria, add to filtred list
                if len(locations) > 0:
                    filtred_list_of_adverts.append(advert)
        
        except Exception as e:
            logging.error(f'GoogleMaps.filter_list_of_adverts() error -> {e}')
        else:
            return filtred_list_of_adverts
