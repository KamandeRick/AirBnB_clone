#!/usr/bin/python3
"""Module defining unit tests for file storage"""
import os
import models
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
#from models.engine.file_storage import reload, all, new, save


class TestFileStorage(unittest.TestCase):
    """unittests for filestorage class"""

    def test_moduleDocs(self):
        """test filestorage module is documented"""
        moduleDoc = (
                __import__("models.engine.file_storage")
                .engine.file_storage.__doc__)
        self.assertGreater(len(moduleDoc), 0)

    def test_classDocs(self):
        """test if class is documented"""
        classDoc = (
                __import__("models.engine.file_storage")
                .engine.file_storage.FileStorage.__doc__)
        self.assertGreater(len(classDoc), 0)

    # def test_methodDocs(self):
        # """Test to check all methods are documented"""
        # methods = (all, save, reload, new)
        # for method in methods:
        # methodDoc = (
        # __import__("models.engine.file_storage")
        # .engine.file_storage.FileStorage.method.__doc__)
        # self.assertGreater(len(methodDoc), 0)

    def test_FileStorage_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_with_args(self):
        with self.assertRaises(TypeError):
            FileStorage(None)


if __name__ == "__main__":
    unittest.main()
