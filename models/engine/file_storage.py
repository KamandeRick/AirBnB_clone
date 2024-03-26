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
                key: value.to_dict() for key, value
                in FileStorage.__objects.items()}
        j_string = dumps(dictionary_to_serialize)
        file_name = FileStorage.__file_path
        with open(file_name, 'w')as f:
            f.write(j_string)

        # with open(FileStorage.__file_path, 'w') as f:
        # dictionary_to_serialize = {}
        # dictionary_to_serialize.update(FileStorage.__objects)
        # for key, val in dictionary_to_serialize.items():
        #   dictionary_to_serialize = val..to_dict()
        #   json.dump(temp, f)

    def reload(self):
        """Desiarilizes JSON file"""
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]
        file_name = FileStorage.__file_path
        if isfile(file_name):
            with open(file_name, 'r') as f:
                j_string = f.read()
                dictionary_to_deserialize = loads(j_string)
                for key, value in dictionary_to_desirialize.items():
                    cls_name, obj_id = key.split(".")
                    if cls_name in classes:
                        class_obj = globals()[cls_name]
                        instance = class_obj(**value)
                        self.new(instance)

                    # if cls_name in classes:
                    #    eval("self.new({}(**value))".format(cls_name)
