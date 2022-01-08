#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 14:50:56 2022

@author: raphaelmunoz
"""

import timeit
from Integral2 import midPoint as midPoint_vec
from Integral import midPoint
from numpy import exp

v = lambda t: 3*t**2*exp(t**3)

t = timeit.Timer('midPoint(v, 0, 1, 1000000)', \
                 setup='from __main__ import midPoint, v')
time_midPoint = t.timeit(10)
print('Time, midpoint: {:g} seconds'.format(time_midPoint))

t = timeit.Timer('midPoint_vec(v, 0, 1, 1000000)', \
                 setup='from __main__ import midPoint_vec, v')
time_midPoint_vec = t.timeit(10)
print('Time, midpoint vec: {:g} seconds'.format(time_midPoint_vec))

print('Efficiency factor {:g}'.format(time_midPoint/time_midPoint_vec))