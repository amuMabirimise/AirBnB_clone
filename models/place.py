#!/usr/bin/python3
<<<<<<< HEAD

from models.base_model import BaseModel

"Imports the BaseModel"

class Place(BaseModel):
    """
    Place class that inherits from BaseModel and represents properties for rent..

    Attributes:
        city_id (str): The ID City of who it belongs.
        user_id (str): The ID User who owns this Place.
        name (str): The name of Place.
        description (str): A description of the Place.
        number_rooms (int): The number of rooms in the Place.
        number_bathrooms (int): The number of the bathrooms Place.
        max_guest (int): The max number of guests accommodate place.`
        price_by_night (int): The price of Place per night.
        latitude (float): The latitude of Place's location.
        longitude (float): The longitude of Place's location.
        amenity_ids (list): A list ID
    """
=======
'''
A Python script for the Place class.
'''
from models.base_model import BaseModel

class Place(BaseModel):
    '''
    Place class inherits from the BaseModel and represents a rental property.
    It includes attributes such as city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, and longitude.
    Additionally, it has a list of amenity_ids to store amenities associated with the place.
    '''
>>>>>>> 26a25b5aa166a2ca01786455f4eaa86b663a08c7
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
