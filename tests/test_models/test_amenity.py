#!/usr/bin/python3
"""Module defining test class for amenity class"""
import unittest
from models.amenity import Amenity
from datetime import datetime
from time import sleep
import os


class Test_Amenity(unittest.TestCase):
    """class for Amenity test cases"""

    def setUp(self):
        """set up temp env for testing"""
        self.amenity = Amenity()

    def tearDown(self):
        """Clear test env as needed"""
        self.amenity = None

    def test_moduleDoc(self):
        """Test if module is documented"""
        moduleDoc = __import__("models.amenity").amenity.__doc__
        self.assertGreater(len(moduleDoc), 0)

    def test_classDoc(self):
        """test if classes are documented"""
        classDoc = __import__("models.amenity").amenity.Amenity.__doc__
        self.assertGreater(len(classDoc), 0)

    def test_id_is_string(self):
        """test id is type string"""
        self.assertEqual(str, type(Amenity().id))

    def test_id_is_unique(self):
        """test if id is unique"""
        bm1 = Amenity()
        bm2 = Amenity()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_created_at_datetime(self):
        """test if created at is datetime object"""
        self.assertEqual(datetime, type(Amenity().created_at))


if __name__ == "__main__":
    unittest.main()
