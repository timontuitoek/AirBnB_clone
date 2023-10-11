#!/usr/bin/python3
"""
module docs
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    console module
    """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """
        quit
        """
        return True

    def do_EOF(self, line):
        """
        exit/quit
        """
        return True

    def do_emptyline(self):
        """
        empty line
        """
        pass

    def do_help(self, line):
        """
        help manual
        """
        cmd.Cmd.do_help(self, line)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
