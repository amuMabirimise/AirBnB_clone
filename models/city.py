#!/usr/bin/python3
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
