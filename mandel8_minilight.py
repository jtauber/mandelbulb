#!/usr/bin/env python

import sys

ITERATIONS = 10
WIDTH = 100
HEIGHT = 100

# view from one side

header_1 = """#MiniLight

%(iterations)s

%(width)s %(height)s

(-5 0 -10) (0.5 0 1) 20

(0 0 0) (0 0 0)

(-0.2 2 -2)   (0.2 2 -2)    (0.2 2 -1.8)      (0 0 0) (200 1000 2000)
(0.2 2 -1.8)  (-0.2 2 -1.8) (-0.2 2 -2)       (0 0 0) (200 1000 2000)

(-2.2 2 -2)   (-1.8 2 -2)   (-1.8 2 -1.8)     (0 0 0) (200 1000 2000)
(-1.8 2 -1.8) (-2.2 2 -1.8) (-2.2 2 -2)       (0 0 0) (2000 1000 200)

""" % dict(iterations=ITERATIONS, width=WIDTH, height=HEIGHT)

# view from other side with different lighting

header_2 = """#MiniLight

%(iterations)s

%(width)s %(height)s

(-5 -5 10) (0.5 0.5 -1) 10

(0 0 0) (0 0 0)

(-2 0 15) (-3 0 15) (-3 1 15)       (0 0 0) (200 500 2000)
(-3 1 15) (-2 1 15) (-2 0 15)       (0 0 0) (200 500 2000)

(-6 0 10) (-7 0 10) (-7 1 10)       (0 0 0) (1500 1000 200)
(-7 1 10) (-6 1 10) (-6 0 10)       (0 0 0) (1500 1000 200)


""" % dict(iterations=ITERATIONS, width=WIDTH, height=HEIGHT)



print header_1

for line in open(sys.argv[1]):
    sys.stdout.write(line)
