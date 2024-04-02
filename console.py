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

    def do_quit(self, arg):
        """Method to quit and exit the program"""
        return True

    def do_EOF(self, arg):
        """Method to exit program on EOF"""
        return True

    def emptyline(self):
        """Method to ensure empty lines do not execute"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
