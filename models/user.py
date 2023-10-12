#!/usr/bin/python3
'''
A Python script for the User class.
'''
from models.base_model import BaseModel

class User(BaseModel):
    '''
    State class representing a state with a 'name' attribute.
    '''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
