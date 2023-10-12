#!/usr/bin/python3
"""
<<<<<<< HEAD
Import from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that inherits from BaseModel and represents user reviews for places.

Attributes:
    place_id (str): The ID of the place associated with the review.
    user_id (str): The ID of the user who created the review.
    text (str): The text content of the review.
=======
A Python script for the Review class.
"""
from models.base_model import BaseModel

class Review(BaseModel):
    """
    Review class for representing reviews.
>>>>>>> 26a25b5aa166a2ca01786455f4eaa86b663a08c7
    """
    place_id = ""
    user_id = ""
    text = ""
<<<<<<< HEAD
=======

>>>>>>> 26a25b5aa166a2ca01786455f4eaa86b663a08c7
