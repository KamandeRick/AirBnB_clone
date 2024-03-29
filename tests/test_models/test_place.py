#!/usr/bin/python3
"""Module defining test class for Place"""
import unittest
from models.place import Place
from unittest.mock import patch
from datetime import datetime
from uuid import UUID
from time import sleep


class Test_Place(unittest.TestCase):
    """Basemodel class test"""
    def setUp(self):
        """method to setup env for each test case"""
        self.place = Place()

    def tearDown(self):
        """Clean up test environment as needed"""
        pass

    def test_moduleDoc(self):
        """Test if module is documented"""
        moduleDoc = __import__("models.place").place.__doc__
        self.assertGreater(len(moduleDoc), 0)

    def test_classDoc(self):
        """test if classes are documented"""
        classDoc = __import__("models.place").place.Place.__doc__
        self.assertGreater(len(classDoc), 0)

    def test_id_is_string(self):
        """test id is type string"""
        self.assertEqual(str, type(Place().id))

    def test_id_is_valid(self):
        """test if id is valid"""
        bm = Place()
        id_value = UUID(bm.id)
        self.assertIs(UUID, type(id_value))

    def test_id_is_unique(self):
        """test if id is unique"""
        bm1 = Place()
        bm2 = Place()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_created_at_datetime(self):
        """test if created at is datetime object"""
        self.assertEqual(datetime, type(Place().created_at))

    def test_created_at_timestamp(self):
        """Test if timestamp is not simillar"""
        bm1 = Place()
        sleep(0.1)
        bm2 = Place()
        self.assertNotEqual(bm1.created_at, bm2.created_at)

    def test_updated_at_is_datetime(self):
        """test if updated at is datetime object"""
        self.assertEqual(datetime, type(Place().updated_at))

    def test__str__(self):
        """test the string representation output"""
        bm1 = Place()
        bm2 = Place()
        self.assertNotEqual(bm1.__str__(), bm2.__str__())

    def test_to_dict_is_dictionary(self):
        """Test if the method to_dict returns a dictionary"""
        bm = Place()
        self.assertTrue(dict, type(bm.to_dict()))

    def test_to_dict(self):
        """test the dictionary representation of object"""
        dictionary_mapping = {
                'id': self.place.id,
                'created_at': self.place.created_at.isoformat(),
                'updated_at': self.place.updated_at.isoformat(),
                '__class__': 'Place'
        }
        self.assertEqual(self.place.to_dict(), dictionary_mapping)

    def test_save(self):
        """test if save method works as expected"""
        bm = Place()
        sleep(0.5)
        updated_at = bm.updated_at
        bm.save()
        self.assertLess(updated_at, bm.updated_at)


if __name__ == "__main__":
    unittest.main()
