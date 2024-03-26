#!/usr/bin/python3
"""Module defining test class for BaseModel"""
import unittest
from models.base_model import BaseModel
from unittest.mock import patch
from dtetime import datetime
from uuid import UUID

class TestBaseModel(unittest.TestCase):
    """Basemodel class test"""
