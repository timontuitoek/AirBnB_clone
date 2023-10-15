#!/usr/bin/python3
"""
test condole
"""
import unittest
from unittest.mock import patch
from console import HBNBCommand
from io import StringIO


class TestConsole(unittest.TestCase):
    """
    test_console
    """
    def test_moduleDocs(self):
        """
        test moduleDocs
        """
        moduleDoc = __import__("console").__doc__
        self.assertGreater(len(moduleDoc), 0)

    def test_ClassDocs(self):
        """
        test class documentation
        """
        classDoc = __import__("console").HBNBCommand.__doc__
        self.assertGreater(len(classDoc), 0)

    def test_quit(self):
        """
        test quit
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            expected_output = ""
            self.assertEqual(expected_output, f.getvalue().strip())

    def test_EOF(self):
        """
        test End of File
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            expected_output = ""
            self.assertEqual(expected_output, f.getvalue().strip())

    def test_help(self):
        """
        test help
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            expected_output = """Documented commands (type help <topic>):
========================================
Amenity    City  Place   State  all     destroy  quit  update
BaseModel  EOF   Review  User   create  help     show"""
            self.assertEqual(expected_output, f.getvalue().strip())

    def test_create_BaseModel_success(self):
        """
        test create BaseModel
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            expected_output = 36
            self.assertEqual(expected_output, len(f.getvalue().strip()))

    def test_create_BaseModel_no_class_name(self):
        """
        test create BaseModel no class_name
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            expected_output = "** class name missing **"
            self.assertEqual(expected_output, f.getvalue().strip())

    def test_create_BaseModel_wrong_class_name(self):
        """
        est BaseModel wrong class_name
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create MyClass")
            expected_output = "** class doesn't exist **"
            self.assertEqual(expected_output, f.getvalue().strip())

    def test_show_BaseModel_no_class_name(self):
        """
        test show BaseModel no class_name
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            expected_output = "** class name missing **"
            self.assertEqual(expected_output, f.getvalue().strip())

    def test_show_BaseModel_wrong_class_name(self):
        """
        test show BaseModel
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show MyClass")
            expected_output = "** class doesn't exist **"
            self.assertEqual(expected_output, f.getvalue().strip())

    def test_show_BaseModel_no_instance_id(self):
        """
        test show instance_id
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            expected_output = "** instance id missing **"
            self.assertEqual(expected_output, f.getvalue().strip())

    def test_show_BaseModel_instance_not_found(self):
        """
        test show instance not found
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel 121212")
            expected_output = "** no instance found **"
            self.assertEqual(expected_output, f.getvalue().strip())

    def test_destroy_BaseModel_no_class_name(self):
        """
        test destroy no class_name
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            expected_output = "** class name missing **"
            self.assertEqual(expected_output, f.getvalue().strip())

    def test_destroy_BaseModel_wrong_class_name(self):
        """
        test BaseModel_wrong_class_name
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy MyClass")
            expected_output = "** class doesn't exist **"
            self.assertEqual(expected_output, f.getvalue().strip())

    def test_destroy_BaseModel_no_instance_id(self):
        """
        test no instance id
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            expected_output = "** instance id missing **"
            self.assertEqual(expected_output, f.getvalue().strip())

    def test_destroy_BaseModel_instance_not_found(self):
        """
        test instance not found
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 121212")
            expected_output = "** no instance found **"
            self.assertEqual(expected_output, f.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
