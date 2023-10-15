#!/usr/bin/python3
"""
console
"""

import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Console DOC
    """
    prompt = "(hbnb) "
    allowed_classes = [
            "BaseModel",
            "User",
            "State",
            "City",
            "Amenity",
            "Place",
            "Review"
            ]

    def do_quit(self, args):
        """
        DOC
        """
        return True

    def do_EOF(self, args):
        """
        DOC
        """
        return True

    def emptyline(self):
        """
        DOC
        """
        pass

    def do_create(self, line):
        """
        DOC
        """
        if not line:
            print("** class name missing **")
            return
        class_name = line.split()[0]
        if class_name not in self.allowed_classes:
            print("** class doesn't exist **")
            return
        obj = eval(class_name)()
        obj.save()
        print(obj.id)

    def do_show(self, line):
        """
        DOC
        """
        self.show_or_destroy(line, "show")

    def do_destroy(self, line):
        """
        DOC
        """
        self.show_or_destroy(line, "destroy")

    def show_or_destroy(self, line, action):
        """
        Helper method for showing or destroying an object
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.allowed_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instances = storage.all()
        key = "{}.{}".format(class_name, args[1])
        if key in instances:
            obj = instances[key]
            if action == "show":
                print(obj)
            else:  # action == "destroy"
                del instances[key]
                storage.save()
        else:
            print("** no instance found **")

    def do_update(self, line):
        """
        do updates
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.allowed_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instances = storage.all()
        key = "{}.{}".format(class_name, args[1])
        if key not in instances:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = instances[key]
        setattr(obj, args[2], args[3].strip('\"'))
        obj.save()

    def do_User(self, line):
        """
        DOC
        """
        self.handle_class_commands(line, "User")

    def do_BaseModel(self, line):
        """
        DOC
        """
        self.handle_class_commands(line, "BaseModel")

    def do_State(self, line):
        """
        DOC
        """
        self.handle_class_commands(line, "State")

    def do_City(self, line):
        """
        DOC
        """
        self.handle_class_commands(line, "City")

    def do_Amenity(self, line):
        """
        DOC
        """
        self.handle_class_commands(line, "Amenity")

    def do_Place(self, line):
        """
        DOC
        """
        self.handle_class_commands(line, "Place")

    def do_Review(self, line):
        """
        DOC
        """
        self.handle_class_commands(line, "Review")

    def handle_class_commands(self, line, class_name):
        """
        Helper method for handling class-specific commands
        """
        class_commands = {
            ".all()": self.do_all,
            ".count()": self.get_count,
        }
        args = line.split()
        if args and args[0] in class_commands:
            class_commands[args[0]](class_name)
        else:
            print("** invalid command **")

    def get_count(self, class_name):
        """
        Helper method for counting instances
        """
        allowed_classes = [
                "BaseModel", "User", "State",
                "City", "Amenity", "Place", "Review"]
        if class_name in allowed_classes:
            final_list = []
            for key, value in models.storage.all().items():
                if (class_name in key):
                    final_list.append(str(value))
            print(len(final_list))
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
