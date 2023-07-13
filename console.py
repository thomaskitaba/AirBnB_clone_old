#!/usr/bin/python3
import cmd
import re
from shlex import split
import string
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
""" console.py entry point ot the
    command interpreter
"""


# TODO: will be replaced latter
# TODO: Borrowed code
def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """ Holberton Command interpretor
        using cmd module
    """
    prompt = "(hbnb) "
    # get all subclasses of BaseModel
    subclasses = BaseModel.__subclasses__()
    # output>>>
    __classes = [str(sub.__name__) for sub in subclasses]
    # append "BaseModel" to classes
    # output>>> classes = ["User", "State", City",
    # "Place", "Amenity", "Review"]
    __classes.append("BaseModel")
    # we can also use this instead
    # __classes = {
    #     "BaseModel",
    #     "User",
    #     "State",
    #     "City",
    #     "Place",
    #     "Amenity",
    #     "Review"
    # }

    def do_quit(self, arg):
        """ quit the command interpreter """
        return True

    def do_EOF(self, arg):
        """ this method simply prints a newline
            character and returns True to exit
            the program.
        """
        print('')
        return True

    def do_create(self, arg):
        """ 1- Creates a new instance of BaseModel,
            2 - saves it (to the JSON file)
            3 - and prints the id.
        """
        new_arg = parse(arg)
        # we can us print(HBNBCommand.__classes) to see
        # content of the __classes we just created
        if len(arg) == 0:
            print("** class name missing **")
            return
        # ----- We can also use this
        try:
            bm1 = eval(new_arg[0])()
            storage.save()
            # print(bm1.__class__.__name__)
            print(bm1.id)
        except NameError:
            print("** class doesn't exist **")
        # -------------------------------------

        # elif new_arg[0] not in HBNBCommand.__classes:
        #     print("** class doesn't exist **")
        # else:
        #     bm1 = eval(new_arg[0])()
        #     print(bm1.id)
        #     # or in short
        #     # print(eval(new_arg[0])().id)
        #     storage.save()

    def do_show(self, arg):
        """ Prints the string representation of
            an instance based on the class name and id
        """
        new_arg = parse(arg)
        # If the class name is missing, print ** class name missing **
        if len(new_arg) == 0:
            print("** class name missing **")
        # If the cls name doesn’t exist, print ** class doesn't exist
        # __** (ex: $ show MyModel)
        elif new_arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        # If the id is missing, print ** instance id missing **
        # __(ex: $ show BaseModel)
        elif len(new_arg) == 1:
            print("** instance id missing **")
        # If the inst of the cls name doesn’t exist for the id,
        # __print ** no instance found **
        elif "{}.{}".format(new_arg[0], new_arg[1]) not in storage.all():
            print("** no instance found **")
        else:
            # print(FileStorage.__objects["{}.{}".format
            # (new_arg[0], new_arg[1])])
            # we can use the above or the bellow
            print(storage.all()["{}.{}".format(new_arg[0], new_arg[1])])

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name
            and id (save the change into the JSON file)
        """
        new_arg = parse(arg)
        if len(new_arg) == 0:
            print("** class name missing **")
        elif new_arg[0] not in HBNBCommand.__classes:
            print("** instance id missing **")
        elif len(new_arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(new_arg[0], new_arg[1]) not in storage.all():
            print("** no instance found **")
        else:
            all_obj = storage.all()
            key = "{}.{}".format(new_arg[0], new_arg[1])
            del all_obj[key]
            print("destroyed")

    def do_all(self, arg):
        """ Prints all string representation of all
            instances based or not on the class name
        """
        new_arg = parse(arg)
        if new_arg:
            if str(new_arg[0]) != "BaseModel":
                print("** class doesn't exist **")
            else:
                print(storage.all())
        else:
            print([storage.all()])

    def do_update(self, arg):
        """ Updates an instance based on the class
            name and id by adding or updating attribute
            (save the change into the JSON file)
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
