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
        with patch("sys.stdout", new=StringIO()) as output_stream:
            HBNBCommand().onecmd("help")
            expected_output = """Documented commands (type help <topic>):
========================================
Amenity    City  Place   State  all     destroy  quit  update
BaseModel  EOF   Review  User   create  help     show"""
            self.assertEqual(expected_output, output_stream.getvalue().strip())

    def test_EOF(self):
        """ Test if EOF method behaves as expected"""
        with patch("sys.stdout", new=StringIO()) as output_stream:
            HBNBCommand().onecmd("EOF")
            expected_output = ""
            self.assertEqual(expected_output, output_stream.getvalue().strip())

    def test_quit(self):
        """Test to check if quit command works as expected"""
        with patch("sys.stdout", new=StringIO()) as output_stream:
            HBNBCommand().onecmd("quit")
            expected_output = ""
            self.assertEqual(expected_output, output_stream.getvalue().strip())

    if __name__ == "__main__":
        unittest.main()
