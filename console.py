#!/usr/bin/python3
""" the console file """


from models.base_model import BaseModel
import cmd
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State



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

        def do_all(self, arg):
            """Print string representations of instances
            based on class name or all instances."""
            if not arg:
                instance_strings = self.get_all_instances()
                if instance_strings:
                    for instance_str in instance_strings:
                        print(instance_str)
                else:
                    print("No instances found.")
            else:
                class_name = arg
                if not check_class_exists(class_name):
                    print('** class doesn\'t exist **')
                else:
                    instance_strings = self.get_instances_by_class(class_name)
                    if instance_strings:
                        for instance_str in instance_strings:
                            print(instance_str)
                    else:
                         print("No instances of {} found.".format(class_name))



if __name__ == '__main__':
    HBNBCommand().cmdloop()
