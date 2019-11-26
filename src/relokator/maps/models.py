from django.db import models
import requests


class GoogleMaps(object):
    """
        Google Maps class

        Main purpose of this class is constructing a url's for google maps
        and retrieving data from google maps serivces.

    """

    # google maps url, used for displaying location in google maps.
    GOOGLE_MAPS_URL = "http://maps.google.com/maps"

    # google geolocation url, used for retrieving x and y of address
    GOOGLE_GEOLOCATION_URL = "https://maps.googleapis.com/maps/api/geocode/json"

    # google places url, used for search objects nearby location
    GOOGLE_PLACE_URL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

    
    def preprocess_address(self, city, address):
        # convert address and city parameter to word plus joined string
        return f'{address} {city}'


    def get_location_map_url(self, city, address):
        # returning google maps url that show location given in parameters
        return f'{self.GOOGLE_MAPS_URL}?q={self.preprocess_address(city, address)}&output=embed'


    def get_location_coords(self, city, address):
        """ function requesting for x and y coords of location.
        
        Function returns:
        x = longitude, y = latitude of location given in arguments.
        """

        # google geocoding api request
        response = requests.get(
            url = self.GOOGLE_GEOLOCATION_URL,
            params = {
                # preprocessing adress
                'address': self.preprocess_address(city, address), 
                # api key # TODO storing in DB for security!
                'key': 'AIzaSyC5rVKcoTfCep0GE7wnJc56P0ZfNbuLto8'
            }
        )

        # retrieving x(longitude) and y(latitude) coords from request
        geolocation_data = response.json()
        x = geolocation_data['results'][0]['geometry']['location']['lng']
        y = geolocation_data['results'][0]['geometry']['location']['lat']
        return x, y

    '''
    def calculate_distance(self, location_a, location_b):
        """ function calculates distance between two (a and b) locations.
        """
        pass


    def find_nearby_objects(self, location, object_type):
        """ function searching for objects of given type nearby of given location
        """
        pass
    '''

    def filter_list_of_adverts(self, list_of_adverts, object_type, radius):
        """ function filtering given list of adverts by location priority given by user
        """

        # list of adverts matching location criteria given by user
        filtred_list_of_adverts = []

        print(object_type)
        print(radius)

        print('--------------------------------------------------------------------------------------------------------------------------------------------')

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
            print(locations)

            # if advert matching location cirteria, add to filtred list
            if len(locations) > 0:
                filtred_list_of_adverts.append(advert)

        print('--------------------------------------------------------------------------------------------------------------------------------------------')

        return filtred_list_of_adverts