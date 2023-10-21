#!/usr/bin/python 3

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class that inherits from and repesent the BaseModel.

    Attributes:
        state_id (str): The ID of the State.
        name (str): The name of that City.
    """

    state_id = ''
    name = ''
