#!/usr/bin/env python

import sys
from pyjon import jsparser, interpr

ctx = interpr.PyJS()

def main(args):
    if len(args)>1:
        filename = args[1]
        f = file(filename, 'r')
        script = f.read()
    else:
        filename = "(stdin)"
        script = sys.stdin.read()
    t = jsparser.parse(script, filename)
    dump = ctx.exec_(t)
    if dump != None: print dump
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))


