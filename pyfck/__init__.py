# pyfck
import os
import re
import sys


class Interpreter(object):
    operators = ['+', '-', ',', '.', '>', '<']
    operators_regex = re.compile('[^\+><\[\],.-]')  # Select everything that's not an operator
    pointer = 0
    tape = [0 for x in range(0, 30000)]
    program = ""

    def __init__(self, filename="main.bf", direct_input=None):
        # Do setup stuff here
        # Check if we're getting direct input from the command line
        if direct_input is not None:
            self.program = self._parse_program(direct_input)
        else:
            self.program = self._load_file(filename)

        print self.program

    @classmethod
    def _load_file(cls, filename):
        try:
            # Try to load the file
            read_file = os.path.realpath(os.path.join(os.curdir, filename))
            with open(read_file, 'rb') as file:
                temp_program = file.read()
        except IOError:
            # Catch the file load error and exit gracefully
            print "Cannot open file {}".format(filename)
            sys.exit(1)

        return cls._parse_program(temp_program)

    @classmethod
    def _parse_program(cls, source_string):
        """
        This function should strip any whitespace and clean up the input. Our goal is to have a program string of only
        viable operators. By default, we'll ignore any and all non-valid characters instead of throwing a fit
        :return:
        """
        return cls.operators_regex.sub('', source_string)
