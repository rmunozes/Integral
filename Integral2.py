#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 22:32:29 2022

@author: raphaelmunoz
"""

""" Integral Method 2 """


from numpy import linspace, sum

    
def trapezoidal(f, a, b, n):
    h = (b - a)/n
    x = linspace(a, b, n+1)
    return(h*(sum(f(x)) - 0.5*f(a) - 0.5*f(b)))


def midPoint(f, a, b, n):
    h = (b - a)/n
    x = linspace(a + h/2, b - h/2, n)
    return(h*sum(f(x)))
    

def application():           
    from math import exp
    n = int(input('n :'))
    v = lambda t: 3*(t**2)*exp(t**3)
    value_trapezodal = trapezoidal(v, 0, 1, n)
    value_midPoint = midPoint(v, 0, 1, n)
    # print(n, value_trapezodal, value_midPoint)
    print('{:.7d}, {:.16f}, {:.16f}, '.format(n, value_trapezodal, value_midPoint))
    
if __name__ == "__main__":
    application()