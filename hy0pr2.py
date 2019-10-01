# CS5 Black, hy0pr2
# Filename: hw0pr2.py
# Name: Myles Fabre
# Problem description: Google's "Secret"

from functools import reduce
import math

def inverse(n):
"""Returns the inverse of n"""
    return 1/n

def initialE(n):
    """Returns the reciprocal of the factorial of a number n that was taken in"""
    return 1/factorial(n)

def e(n):
    initialList = list(range(1, n+1))
    numList = list(map(initialE, initialList))
     return 1+sum(numList)

def error(n):
    """Returns the absolute value of the approximated e value minus mathematical e"""
    return abs(e(n)-math.e)

def mult(x, y):
    """Returns the product of x and y"""
    return x*y

def factorial(n):
    multList = list(range(1, n+1))
    return reduce(mult, multList)

def mean(L):
    addList = list(L)
    return sum(addList)/len(addList)
