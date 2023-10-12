#!/usr/bin/python3
<<<<<<< HEAD

from models.base_model import BaseModel
"import the BaseModel to User"

class User(BaseModel):
    """
    User class that inherits from the BaseModel class.

    Attributes:
        email (str): The email address of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.

    Public instance attributes:
        email (str): The email address of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.

    Methods:
        The User class inherits common methods from BaseModel.
    """
=======
'''
A Python script for the User class.
'''
from models.base_model import BaseModel

class User(BaseModel):
    '''
    State class representing a state with a 'name' attribute.
    '''
>>>>>>> 26a25b5aa166a2ca01786455f4eaa86b663a08c7
    email = ""
    password = ""
    first_name = ""
    last_name = ""
