#!/usr/bin/python3
""" the console file """

from models.base_model import BaseModel
import cmd


class HBNBCommand(cmd.Cmd):
    """class for the console"""

    prompt = "(hbnb) "

    def empty_line(self):
        """an empty line + ENTER shouldn’t execute anything"""
        pass
    def do_EOF(self, arg):
        """Exit the program on EOF (Ctrl+D)."""
        return True
    def do_quit(self, arg):
        """Quit the command interpreter."""
        return True
    
    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if arg is None:
            print('** class name missing **')
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if len(args) == 0:
            print('** class name missing **')
            return
        class_name = args[0]
        if len(args) == 1:
            print('** instance id missing **')
            return
        instance_id = args[1]



if __name__ == '__main__':
    HBNBCommand().cmdloop()
