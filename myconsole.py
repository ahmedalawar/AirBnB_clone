#!/usr/bin/python3

import cmd


class Command(cmd.Cmd):

    """ BaseModel command line interperter"""

    def do_greet(self, arg):
        print("Hello this BaseModel command interperter")


if __name__ == '__main__':
    Command().cmdloop()
