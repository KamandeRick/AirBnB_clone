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
        """ Test to check if docs are present """
        classDoc = __import__("console").HBNB.__doc__
        self.assertGreater(len(classDoc), 0)

    if __name__ == "__main__":
        unittest.main()
