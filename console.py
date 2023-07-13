#!/usr/bin/python3
import cmd
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
""" console.py entry point ot the
    command interpreter
"""


# TODO: will be replaced latter
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
    prompt = "(hbnb) "
    __classes = [
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    ]

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
        if len(arg) == 0:
            print("** class name missing **")
            return
        try:
            bm1 = eval(arg)()
            models.storage.save()
            print(bm1)
        except Exception as e:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """ Prints the string representation of
            an instance based on the class name and id
        """
        # If the class name is missing, print ** class name missing **
        if len(arg[0]) == 0:
            print("** class name missing **")
            return
        # If the cls name doesn’t exist, print ** class doesn't exist
        # __** (ex: $ show MyModel)
        try:
            pass
        exept Exception as e:
            pass
        # If the id is missing, print ** instance id missing **
        # __(ex: $ show BaseModel)
        if len(arg[1]) == 0:
            print("** class name missing **")
            return
        # If the inst of the cls name doesn’t exist for the id,
        # __print ** no instance found **
        try:
            pass
        exept Exception as e:
            pass

    def do_show(self, arg):
        """ Deletes an instance based on the class name
            and id (save the change into the JSON file)
        """
        pass

    def do_all(self, arg):
        """ Prints all string representation of all
            instances based or not on the class name
        """
        pass

    def do_update(self, arg):
        """ Updates an instance based on the class
            name and id by adding or updating attribute
            (save the change into the JSON file)
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
