#!/usr/bin/python3
import cmd
import sys

"""
Module containing class BaseModel
"""

class HBNBCommand(cmd.Cmd):
    """
    Class HBNBCommand: command interpreter
    """

    prompt = "(hbnb) "

    def do_quit(self, line):
        """ quit the program """
        return True

    def do_EOF(self, line):
        """ exit the program when EOF """
        return True

    def emptyline(self):
        pass

    """ Help commands """

    def help_help(self):
        print("help command to describe the function of a command\n")

    def help_quit(self):
        """ help for quit """
        print("quit command to exit the program\n")

    def help_EOF(self):
        """ help for EOF """
        print("EOF command to exit the program when end of file\n")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
