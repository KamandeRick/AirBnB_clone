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

    def do_show(self, arg):
        """Method to Show instance based on id and class name"""
        class_name, obj_id = None, None
        args = arg.split(' ')
        if len(args) > 0:
            class_name = args[0]
        if len(args) > 1:
            obj_id = args[1]
        if not class_name:
            print('** class name missing **')
        elif not obj_id:
            print('** instance id missing **')
        elif not self.class_list.get(class_name):
            print("** class doesn't exist **")
        else:
            key = class_name + "." + obj_id
            obj = models.storage.all().get(key)
            if not obj:
                print('** no instance found **')
            else:
                print(obj)

    def do_destroy(self, arg):
        """Method to destroy instance based on id"""
        class_name, obj_id = None, None
        args = arg.split(' ')
        if len(args) > 0:
            class_name = args[0]
        if len(args) > 1:
            obj_id = args[1]
        if not class_name:
            print('** class name missing **')
        elif not obj_id:
            print('** instance id missing **')
        elif not self.class_list.get(class_name):
            print("** class doesn't exist **")
        else:
            key = class_name + "." + obj_id
            obj = models.storage.all().get(key)
            if not obj:
                print('** no instance found **')
            else:
                del models.storage.all()[key]
                models.storage.save()

    def do_all(self, arg):
        """Prints all instances based on the class name or not"""
        if not arg:
            insts = [str(inst) for inst in models.storage.all().values()]
            print(insts)
        else:
            if arg not in self.class_list:
                print("** class doesn't exist **")
                return False
            insts = [
                    str(inst)
                    for inst in models.storage.all().values()
                    if isinstance(inst, self.class_list[arg])
                    ]
            print(insts)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        class_name = None
        obj_id = None
        attribute_name = None
        attribute_value = None
        updatetime = datetime.now()
        args = arg.split(' ', 3)
        if len(args) > 0:
            class_name = args[0]
        if len(args) > 1:
            obj_id = args[1]
        if len(args) > 2:
            attribute_name = args[2]
        if len(args) > 3:
            attribute_value = list(shlex(args[3]))[0].strip('"')
        if not class_name:
            print('** class name missing **')
        elif not obj_id:
            print('** instance id missing **')
        elif not attribute_name:
            print('** attribute name missing **')
        elif not attribute_value:
            print('** value missing **')
        elif not self.class_list.get(class_name):
            print("** class doesn't exist **")
        else:
            key = class_name + "." + obj_id
            obj = models.storage.all().get(key)
            if not obj:
                print('** no instance found **')
            else:
                if hasattr(obj, attribute_name):
                    attribute_type = type(getattr(obj, attribute_name))
                    if callable(attribute_type):
                        attribute_value = attribute_type(attribute_value)
                    else:
                        pass
                else:
                    attribute_type = self.getType(attribute_value)
                    attribute_value = attribute_type(attribute_value)
                setattr(obj, attribute_name, attribute_value)
                obj.updated_at = updatetime
                models.storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
