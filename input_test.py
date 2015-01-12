#!/usr/bin/env python
""" Input system module demo
"""

from doormon.input import Input

if __name__ == "__main__":
    def open():
        print "Open!"
    def close():
        print "Close!"
    input = Input(open, close)
    input.start()
