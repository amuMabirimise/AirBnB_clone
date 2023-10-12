#!/usr/bin/python3
'''
<<<<<<< HEAD
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
=======
A Python script for the State class.
'''
from models.base_model import BaseModel

class State(BaseModel):
    '''
    State class representing a state with a 'name' attribute.
>>>>>>> 26a25b5aa166a2ca01786455f4eaa86b663a08c7
    '''
    name = ""
