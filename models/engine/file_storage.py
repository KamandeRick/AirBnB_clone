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


class FileStorage:
    """serializes instances to  JSON file and vice versa"""
    __objects = {}
    __file_path = "file.json"

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        dictionary_to_serialize = {
                Key: value.to_dict() for key, value
                in FileStorage.__objects.items()}
        j_string = dumps(dictionary_to_serialize)
        filename = FileStorage.__file_path
        with open(filename, 'w')as f:
            f.write(j_string)
