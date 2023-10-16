#!/usr/bin/python3
"""Create a city class"""

from models.base_model import BaseModel


class City(BaseModel):
    """City attribute"""
    state_id = ""
    name = ""
