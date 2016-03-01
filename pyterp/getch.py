# -*- coding: utf-8 -*-


"""
Gets a single character from standard input.
Does not echo to the terminal
"""


class _Getch:
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self):
        return self.impl()


class _GetchUnix:
    def __call__(self):
        # Termios only available on Unix-type systems
        # See: https://docs.python.org/2/library/termios.html
        import sys, tty, termios
        fd = sys.stdin.fileno()
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, termios.tcgetattr(fd))
        return ch


class _GetchWindows:
    def __call__(self):
        import msvcrt
        return msvcrt.getch()
