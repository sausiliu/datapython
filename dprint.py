import sys
debug=True

GREEN = lambda x: "\x1b[32;01m" + x + "\x1b[39;49;00m"
BLUE = lambda x: "\x1b[34;01m" + x + "\x1b[39;49;00m"
BOLD = lambda x: "\033[1m" + x + "\033[0m"
YELLOW = lambda x: "\x1b[33;01m" + x + "\x1b[39;49;00m"


def dprint(*args):

    if debug:

        s = ""
        for a in args:
            s += ("%s" % a)

        co = sys._getframe(1).f_code

        frame = BOLD(co.co_name)

        print("%s %s" % (frame, "(%s:%d)" % (co.co_filename, co.co_firstlineno)))
        print(s)
