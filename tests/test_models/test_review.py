#!/usr/bin/python3
"""Module defining test class for Review"""
import unittest
from models.review import Review
from unittest.mock import patch
from datetime import datetime
from uuid import UUID
from time import sleep


class Test_Review(unittest.TestCase):
    """Basemodel class test"""
    def setUp(self):
        """method to setup env for each test case"""
        self.review = Review()

    def tearDown(self):
        """Clean up test environment as needed"""
        pass

    def test_moduleDoc(self):
        """Test if module is documented"""
        moduleDoc = __import__("models.review").review.__doc__
        self.assertGreater(len(moduleDoc), 0)

    def test_classDoc(self):
        """test if classes are documented"""
        classDoc = __import__("models.review").review.Review.__doc__
        self.assertGreater(len(classDoc), 0)

    def test_id_is_string(self):
        """test id is type string"""
        self.assertEqual(str, type(Review().id))

    def test_id_is_valid(self):
        """test if id is valid"""
        bm = Review()
        id_value = UUID(bm.id)
        self.assertIs(UUID, type(id_value))

    def test_id_is_unique(self):
        """test if id is unique"""
        bm1 = Review()
        bm2 = Review()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_created_at_datetime(self):
        """test if created at is datetime object"""
        self.assertEqual(datetime, type(Review().created_at))

    def test_created_at_timestamp(self):
        """Test if timestamp is not simillar"""
        bm1 = Review()
        sleep(0.1)
        bm2 = Review()
        self.assertNotEqual(bm1.created_at, bm2.created_at)

    def test_updated_at_is_datetime(self):
        """test if updated at is datetime object"""
        self.assertEqual(datetime, type(Review().updated_at))

    def test__str__(self):
        """test the string representation output"""
        bm1 = Review()
        bm2 = Review()
        self.assertNotEqual(bm1.__str__(), bm2.__str__())

    def test_to_dict_is_dictionary(self):
        """Test if the method to_dict returns a dictionary"""
        bm = Review()
        self.assertTrue(dict, type(bm.to_dict()))

    def test_to_dict(self):
        """test the dictionary representation of object"""
        dictionary_mapping = {
                'id': self.review.id,
                'created_at': self.review.created_at.isoformat(),
                'updated_at': self.review.updated_at.isoformat(),
                '__class__': 'Review'
        }
        self.assertEqual(self.review.to_dict(), dictionary_mapping)

    def test_save(self):
        """test if save method works as expected"""
        bm = Review()
        sleep(0.5)
        updated_at = bm.updated_at
        bm.save()
        self.assertLess(updated_at, bm.updated_at)


if __name__ == "__main__":
    unittest.main()
