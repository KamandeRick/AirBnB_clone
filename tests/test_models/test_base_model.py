#!/usr/bin/python3
"""Module defining test class for BaseModel"""
import unittest
from models.base_model import BaseModel
from unittest.mock import patch
from datetime import datetime
from uuid import UUID


class Test_BaseModel(unittest.TestCase):
    """Basemodel class test"""
    def setUp(self):
        """method to setup env for each test case"""
        self.base_model = BaseModel()

    def tearDown(self):
        """Clean up test environment as needed"""
        pass

    def test_moduleDoc(self):
        """Test if module is documented"""
        moduleDoc = __import__("models.base_model").base_model.__doc__
        self.assertGreater(len(moduleDoc), 0)

    def test_classDoc(self):
        """test if classes are documented"""
        classDoc = __import__("models.base_model").base_model.BaseModel.__doc__
        self.assertGreater(len(classDoc), 0)

    def test_id_is_string(self):
        """test id is type string"""
        self.assertEqual(str, type(BaseModel().id))

    def test_id_is_valid(self):
        """test if id is valid"""
        bm = BaseModel()
        id_value = UUID(bm.id)
        self.assertIs(UUID, type(id_value))

    def test_id_is_unique(self):
        """test if id is unique"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_created_at_datetime(self):
        """test if created at is datetime object"""
        self.assertEqual(datetime, type(BaseModel().created_at))


if __name__ == "__main__":
    unittest.main()
