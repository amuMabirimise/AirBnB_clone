#!/usr/bin/python 3

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class that inherits from and repesent the BaseModel.

    Attributes:
        state_id (str): The ID of the State.
        name (str): The name of that City.
    """
    state_id = ""
    name = ""

'''
This is a Python script for a City class.
'''

from models.base_model import BaseModel

class City(BaseModel):
    '''
    This City class is derived from the BaseModel.
    It contains attributes for state_id and name.
    '''
    state_id = ''
    name = ''

