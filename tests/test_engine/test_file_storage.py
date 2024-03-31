#!/usr/bin/python3
"""Module defining unit tests for file storage"""
import os
import models
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
# from models.engine.file_storage import reload, all, new, save


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
        """test FileStorage instantiation without args"""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_with_args(self):
        """test FileStorage instantiation with args"""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_file_path_type(self):
        """test FileStorage file path is private"""
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        """test if storage object is private dictionary"""
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_objects(self):
        """Test for objects method"""
        file_storage = FileStorage()
        file_storage._FileStorage__objects = {}
        self.assertEqual(file_storage._FileStorage__objects, {})
        obj = BaseModel()
        file_storage.new(obj)
        objects = file_storage.all()
        self.assertIn("BaseModel.{}".format(obj.id), objects)
        self.assertEqual(objects["BaseModel.{}".format(obj.id)], obj)

    def test_method_all(self):
        """test for all method of FileStorageClass"""
        file_storage = FileStorage()
        objects = file_storage.all()
        self.assertEqual(objects, file_storage._FileStorage__objects)

    def test_method_save(self):
        """test case for save method of fileStorage class"""
        file_storage = FileStorage()
        obj1 = BaseModel()

        file_storage.save()

        with open("file.json", "r") as f:
            json_string = f.read()

        self.assertIn("BaseModel.{}".format(obj1.id), json_string)

    def test_method_new(self):
        """Test case for new method"""
        file_storage = FileStorage()
        obj1 = BaseModel()
        obj2 = BaseModel()

        file_storage.new(obj1)
        file_storage.new(obj2)

        self.assertIn(
                "BaseModel.{}".format(obj1.id),
                file_storage._FileStorage__objects)
        self.assertIn(
                "BaseModel.{}".format(obj2.id),
                file_storage._FileStorage__objects)

        self.assertEqual(
                file_storage._FileStorage__objects[
                    "BaseModel.{}".format(obj1.id)], obj1)
        self.assertEqual(
                file_storage._FileStorage__objects[
                    "BaseModel.{}".format(obj2.id)], obj2)

    def test_method_reload(self):
        """Test for reload method"""
        file_storage = FileStorage()
        base_model = BaseModel()
        file_storage.save()
        models.storage.reload()
        objects = file_storage._FileStorage__objects

        self.assertIn("BaseModel.{}".format(base_model.id), objects)


if __name__ == "__main__":
    unittest.main()
