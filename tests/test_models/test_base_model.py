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
        self.assertEqual(type(BaseModel().id, str))


if __name__ == "__main__":
    unittest.main()
