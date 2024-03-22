#!/usr/bin/python3
"module defining filestorage management class"""
from models.review import Review
from models.place import Place
from models.amenity import Amenity
from models.user import User
from models.base_model import BaseModel
from models.city import City
from models.state import State
from os.path import isfile
from json import loads, dumps


class FileSorage:
    """serializes instances to  JSON file and vice versa"""
    __objects = {}
    __file_path = "file.json"

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects
