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

    if __name__ == "__main__":
        unittest.main()
