#!/usr/bin/python3
""" Module containing entry point of the command interpreter"""
import cmd
import sys
import models
from models.base_model import BaseModel
from shlex import shlex
from models.user import User
from datetime import datetime
from models.place import Place
from models.review import Review
from models.city import City
from models.amenity import Amenity
from models.state import State


class HBNBCommand(cmd.Cmd):
    """ Console program for airbnb clone"""
    prompt = '(hbnb) '
    class_list = {'BaseModel': BaseModel, 'State': State, 'City': City,
               'Amenity': Amenity, 'Place': Place, 'Review': Review,
               'User': User}

    def emptyline(self):
        """Method to ensure empty lines do not execute"""
        pass
    
    def do_create(self, class_name=None):
        """Method to create BaseModel obj, save it and prints it's id"""
        if not class_name:
            print('** class name missing **')
        elif not self.class_list.get(class_name):
            print('** class doesn\'t exist **')
        else:
            obj = self.class_list[class_name]()
            models.storage.save()
            print(obj.id)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
