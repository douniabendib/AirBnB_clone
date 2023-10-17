#!/usr/bin/python3
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

# Define valid class names
VALID_CLASSES = {
    "BaseModel",
    "User",
    "State",
    "City",
    "Place",
    "Amenity",
    "Review"
}

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def emptyline(self):
        pass

    def default(self, arg):
        print("*** Unknown syntax: {}".format(arg))

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """Create a new class instance and print its id."""
        args = parse(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in VALID_CLASSES:
            print("** class doesn't exist **")
        else:
            instance = eval(args[0])()
            instance.save()
            print(instance.id)

    def do_show(self, arg):
        """Display the string representation of a class instance."""
        args = parse(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in VALID_CLASSES:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            instance = find_instance(args[0], args[1])
            if instance:
                print(instance)

    def do_destroy(self, arg):
        """Delete a class instance of a given id."""
        args = parse(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in VALID_CLASSES:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            instance = find_instance(args[0], args[1])
            if instance:
                storage.delete(instance)
                storage.save()

    def do_all(self, arg):
        """Display string representations of all instances."""
        args = parse(arg)
        objects = []
        if args and args[0] not in VALID_CLASSES:
            print("** class doesn't exist **")
        else:
            instances = storage.all()
            for instance in instances.values():
                if not args or instance.__class__.__name__ == args[0]:
                    objects.append(str(instance))
            print(objects)

    def do_count(self, arg):
        """Retrieve the number of instances of a given class."""
        args = parse(arg)
        count = 0
        instances = storage.all()
        if args and args[0] not in VALID_CLASSES:
            print("** class doesn't exist **")
        else:
            for instance in instances.values():
                if not args or instance.__class__.__name__ == args[0]:
                    count += 1
            print(count)

    def do_update(self, arg):
        """Update a class instance with new attribute values."""
        args = parse(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in VALID_CLASSES:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance = find_instance(args[0], args[1])
        if not instance:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        attribute_name = args[2]
        attribute_value = args[3]
        try:
            attribute_value = eval(attribute_value)
        except (NameError, SyntaxError):
            pass

        setattr(instance, attribute_name, attribute_value)
        instance.save()

def parse(arg):
    """Parse command-line arguments."""
    tokens = re.findall(r'(\[.*?\]|\{.*?\}|[^\s]+)', arg)
    return [t.strip(",") for t in tokens]

def find_instance(class_name, instance_id):
    """Find a class instance by class name and instance ID."""
    key = "{}.{}".format(class_name, instance_id)
    return storage.get(key)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
