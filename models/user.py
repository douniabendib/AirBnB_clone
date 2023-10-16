#!/usr/bin/python3
"""Creating a user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Add some info"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
