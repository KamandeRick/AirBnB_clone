#!/usr/bin/python3
""" Test for console """

from io import StringIO
from console import HBNBcommand
from unittest.mock import patch
import unittest
import console


class TestConsole(unittest.TestCase):
    """ Testconsole class """
    def test_ClassDocs(self):
        """ Test to check if class docs are present """
        classDoc = __import__("console").HBNBCommand.__doc__
        self.assertGreater(len(classDoc), 0)

    def test_moduleDocs(self):
        """ Test to check if module docs are present """
        moduleDoc = __import__("console").__doc__
        self.assertGreater(len(moduleDoc), 0)

    def test_help(self):
        """ Test to check if help works as expected """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            expected_outpt = """Documented commands (type help <topic>):
========================================
Amenity    City  Place   State  all     destroy  quit  update
BaseModel  EOF   Review  User   create  help     show"""
            self.assertEqual(expected_output, f.getvalue().strip())

    if __name__ == "__main__":
        unittest.main()
