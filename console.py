#!/usr/bin/python3
import cmd
""" console.py entry point ot the
    command interpreter
"""


class HBNBCommand(cmd.Cmd):
    intro = ""
    prompt = "(hbnb) "

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
