#!/usr/bin/python3

from models.base_model import BaseModel

"Imports the BaseModel"


from models.base_model import BaseModel


class Place(BaseModel):
    '''
    Place class inherits from the BaseModel.
    Represents a rental property.
    It includes attributes such as city_id, user_id, name, 
    description, number_rooms, number_bathrooms
    max_guest, price_by_night, latitude, and longitude.
    Additionally, it has a list of amenity_ids.
    Store amenities associated with the place.
    '''

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
