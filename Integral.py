#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 16:37:39 2021

@author: raphaelmunoz
"""


""" Integral Method 1"""

    
def trapezoidal(f, a, b, n):
    h = (b - a)/n
    f_sum = 0
    for i in range(0, n, 1):
        x = a + i*h
        f_sum = f_sum + f(x)
    return(h*(0.5*f(a) + f_sum + 0.5*f(b)))

def midPoint(f, a, b, n):
    h = (b - a)/n
    f_sum = 0
    for i in range(0, n, 1):
        x = a + 0.5*h + i*h
        f_sum = f_sum + f(x)
    return(h*f_sum)


def application():           
    from math import exp
    n = int(input('n :'))
    v = lambda t: 3*(t**2)*exp(t**3)
    value_trapezodal = trapezoidal(v, 0, 1, n)
    value_midPoint = midPoint(v, 0, 1, n)
    print(n, value_trapezodal, value_midPoint)
#        print('{:.7d}, {:.16f}, {:.16f}, '.format(n, value_trapezodal, value_midPoint))
    
if __name__ == "__main__":
    application()
        