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

    def empty_line(self):
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
        """Method to Show instance based on id"""
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
        """Method to Print all instances based on the class name"""
        if not arg:
            print([str(value) for key, value in models.storage.all().items()])
        else:
            if not self.class_list.get(arg):
                print("** class doesn't exist **")
                return False
            print([str(value) for key, value in models.storage.all().items()
                   if type(value) is self.class_list.get(arg)])

    def do_quit(self, arg):
        """Method to quit and exit the program"""
        return True

    def do_EOF(self, arg):
        """Method to exit program on EOF"""
        return True

    def default(self, line):
        """Method to handle class commands"""
        split_line = line.split('.', 1)
        if len(ln) < 2:
            print('*** Unknown syntax:', split_line[0])
            return False
        class_name, line = split_line[0], split_line[1]
        if class_name not in list(self.class_list.keys()):
            print('*** Unknown syntax: {}.{}'.format(class_name, line))
            return False
        split_line = line.split('(', 1)
        if len(split_line) < 2:
            print('*** Unknown syntax: {}.{}'.format(class_name, split_line[0]))
            return False
        method_name, args = split_line[0], split_line[1].rstrip(')')
        if method_name not in ['all', 'count', 'show', 'destroy', 'update']:
            print('*** Unknown syntax: {}.{}'.format(class_name, line))
            return False
        if method_name == 'all':
            self.do_all(class_name)
        elif method_name == 'count':
            print(self.count_class(class_name))
        elif method_name == 'show':
            self.do_show(class_name + " " + args.strip('"'))
        elif method_name == 'destroy':
            self.do_destroy(class_name + " " + args.strip('"'))
        elif method_name == 'update':
            lb, rb = args.find('{'), args.find('}')
            d = None
            if args[lb:rb + 1] != '':
                d = eval(args[lb:rb + 1])
            split_line = args.split(',', 1)
            obj_id, args = split_line[0].strip('"'), ln[1]
            if d and type(d) is dict:
                self.handle_dict(class_name, obj_id, d)
            else:
                from shlex import shlex
                args = args.replace(',', ' ', 1)
                split_line = list(shlex(args))
                split_line[0] = split_line[0].strip('"')
                self.do_update(" ".join([class_name, obj_id, split_line[0], split_line[1]]))


if __name__ == "__main__":
    HBNBCommand().cmdloop()
