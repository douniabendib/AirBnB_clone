#!/usr/bin/python3
"""creating a review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """ info about review"""
    place_id = ""
    user_id = ""
    text = ""
