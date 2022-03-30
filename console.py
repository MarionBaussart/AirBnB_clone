#!/usr/bin/python3
"""
Module containing the command line interpreter for the Airbnb Console
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Class HBNBCommand: command interpreter
    """

    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "State", "City", "Amenity", "Place",
               "Review"]

    def do_quit(self, line):
        """ quit the program """
        return True

    def do_EOF(self, line):
        """ exit the program when EOF """
        return True

    def emptyline(self):
        pass

    def do_create(self, class_name):
        """
        create <class_name>
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        Args:
            self: first argument to instance methods
            args: class_name
        returns: no return
        """
        if not class_name:
            print("** class name missing **")
        elif class_name not in classes:
            print("** class doesn't exist **")
        else:
            new_instance = class_name()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, args):
        """
        show <class_name> <id>
        Prints the string representation of an instance
        based on the class name and id
        """
        if not args[0]:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        if not args[1]:
            print("** instance id missing **")
        else:
            for key, value in storage.all().items():
                if value.id is args[1]:
                    print(value)
                    return
            print("** no instance found **")

    def help_help(self):
        """ help for help """
        print("help command to describe the function of a command\n")

    def help_quit(self):
        """ help for quit """
        print("quit command to exit the program\n")

    def help_EOF(self):
        """ help for EOF """
        print("EOF command to exit the program when end of file\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
