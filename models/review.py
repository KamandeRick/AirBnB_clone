#!/usr/bin/python3
"""module defining review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class docs"""
    place_id = ""
    user_id = ""
    text = ""
