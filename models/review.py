#!/usr/bin/python3
"""
Import from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that inherits from BaseModel.
    represents user reviews for places.

    Attributes:
    place_id (str): The ID of the place associated with the review.
    user_id (str): The ID of the user who created the review.
    text (str): The text content of the review.

    A Python script for the Review class.
    """
    place_id = ""
    user_id = ""
    text = ""
