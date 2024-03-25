#!/usr/bin/python3
"""Module defining Amenities test class"""
import unittest
import os
from models.amenity import Amenity
from models.engine.file_storage import FileStorage

class TestAmenity(unittest.TestCase):
    """TestAmenity class docs"""

    def test_name(self):
        """Test to check amenity name"""
        new = Amenity()
        self.assertIs(type(new.name), str)

    def test_moduleDocs:
        """test to check for amenity module docs"""

    if __name__ == "__main__":
        unittest.main()

