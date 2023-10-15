#!/usr/bin/python3
"""
Console DOC
"""
import cmd
import re
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models


class HBNBCommand(cmd.Cmd):
    """
    Class Doc
    """
    prompt = "(hbnb) "

    def do_quit(self, args):
        """
        Command to quit the application
        """
        return True

    def do_EOF(self, args):
        """
        Command to exit the application with EOF (Ctrl+D)
        """
        return True

    def emptyline(self):
        """
        Handle empty input
        """
        pass

    def do_create(self, arg):
        """
        Create a new instance of a class and print its ID
        """
        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
        }

        # Check if class name is provided
        if not arg:
            print("** class name missing **")
            return

        args_array = arg.split()
        class_name = args_array[0]

        # Check if the provided class name is valid
        if class_name not in classes:
            print("** class doesn't exist **")
            return

        # Create an instance of the specified class, save it, and print its ID
        obj = classes[class_name]()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """
        Show details of a specific instance
        """
        allowed_classes = [
                "BaseModel", "User", "State",
                "City", "Amenity", "Place", "Review"]
        if not arg:
            print("** class name missing **")
            return

        args_array = arg.split()

        if not args_array:
            print("** instance id missing **")
            return

        class_name = args_array[0]

        # Check if the provided class name is valid
        if class_name not in allowed_classes:
            print("** class doesn't exist **")
            return

        if len(args_array) < 2:
            print("** instance id missing **")
            return

        objs_dict = models.storage.all()
        sstr = "{}.{}".format(class_name, args_array[1])

        if sstr in objs_dict:
            print(objs_dict[sstr])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Delete a specific instance
        """
        allowed_classes = [
                "BaseModel", "User", "State",
                "City", "Amenity", "Place", "Review"]
        if not arg:
            print("** class name missing **")
            return

        args_array = arg.split()

        if not args_array:
            print("** instance id missing **")
            return

        class_name = args_array[0]

        # Check if the provided class name is valid
        if class_name not in allowed_classes:
            print("** class doesn't exist **")
            return

        if len(args_array) < 2:
            print("** instance id missing **")
            return

        objs_dict = models.storage.all()
        sstr = "{}.{}".format(class_name, args_array[1])

        if sstr in objs_dict:
            del objs_dict[sstr]
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        List all instances or instances of a specific class
        """
        allowed_classes = [
                "BaseModel", "User", "State",
                "City", "Amenity", "Place", "Review"]
        args_array = arg.split()

        if args_array and args_array[0] not in allowed_classes:
            print("** class doesn't exist **")
            return

        finlist = []
        for key, value in models.storage.all().items():
            if (class_name in key):
                finlist.append(str(value))
        print(finlist)

    def do_update(self, arg):
        """
        Update an instance's attribute
        """
        allowed_classes = [
                "BaseModel", "User", "State",
                "City", "Amenity", "Place", "Review"]
        if not arg:
            print("** class name missing **")
            return

        args_array = arg.split()

        if not args_array:
            print("** instance id missing **")
            return

        class_name = args_array[0]

        # Check if the provided class name is valid
        if class_name not in allowed_classes:
            print("** class doesn't exist **")
            return

        if len(args_array) < 2:
            print("** instance id missing **")
            return

        objs_dict = models.storage.all()
        sstr = "{}.{}".format(class_name, args_array[1])

        if sstr not in objs_dict:
            print("** no instance found **")
            return

        if len(args_array) < 3:
            print("** attribute name missing **")
            return

        if len(args_array) < 4:
            print("** value missing **")
            return

        setattr(objs_dict[sstr], str(args_array[2]), str(args_array[3]))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
