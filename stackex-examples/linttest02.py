#!/usr/bin/env python2
# by Daniel Rosengren, modified by e-satis
"""
Module doctring
https://stackoverflow.com/a/1429145/6709630
"""


import time
from sys import stdout

BAILOUT = 16
MAX_ITERATIONS = 1000

def mandelbrot(dim_1, dim_2):
    """
    function doc string
    """
    cr1 = dim_1 - 0.5
    ci1 = dim_2
    zi1 = 0.0
    zr1 = 0.0

    for i in xrange(MAX_ITERATIONS) :
        temp = zr1 * zi1
        zr2 = zr1 * zr1
        zi2 = zi1 * zi1
        zr1 = zr2 - zi2 + cr1
        zi1 = temp + temp + ci1

        if zi2 + zr2 > BAILOUT:
            return i

    return 0

def execute() :
    """
    func doc string
    """
    print 'Rendering...'
    for dim_1 in xrange(-39, 39):
        stdout.write('\n')
        for dim_2 in xrange(-39, 39):
            if mandelbrot(dim_1/40.0, dim_2/40.0) :
                stdout.write(' ')
            else:
                stdout.write('*')


START_TIME = time.time()
execute()
print '\nPython Elapsed %.02f' % (time.time() - START_TIME)
