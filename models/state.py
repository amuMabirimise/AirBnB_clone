#!/usr/bin/python3
'''
Import the BaseModel
'''
from models.base_model import BaseModel


class State(BaseModel):
    '''
     State class representing a state in a larger data model.

    Attributes:
        name (str): The name of the state.

    Public instance attributes:
        name (str): The name of the state.
    '''
    name = ""
