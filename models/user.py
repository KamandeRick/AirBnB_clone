#!/usr/bin/python3
"""Module defining user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """user class docs"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
