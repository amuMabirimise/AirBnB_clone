#!/usr/bin/python3


from models.base_model import BaseModel
"import the BaseModel"


class Amenity(BaseModel):
    """
    Amenity class that inherits from and represents the BaseModel.

    Attributes:
        name (str)of the name amenity.
    """

'''
A Python script for the Amenity class.
'''

from models.base_model import BaseModel

class Amenity(BaseModel):
    '''
    Amenity class representing an amenity with a 'name' attribute.
    '''
    name = ""
