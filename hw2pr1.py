#
# hw2pr1.py
#
# Name: Myles Fabre
#
# Turtle graphics and recursion
#

import time
from turtle import *
from random import *

def setup_window():
    """ sets up the turtle window
        type   bye()   at the prompt to close it
        """
    window = Screen()  # this turtle window
    # customize for your screen!
    window.setup(width=542,height=542,startx=10,starty=10)
# the startx and starty are the location of the upper-left corner


def tri(n):
    """Draws n 100-pixel sides of an equilateral triangle.
        Note that n doesn't have to be 3 (!)
        """
    if n == 0:
        return      # No sides to draw, so stop drawing
    else:
        dot(10, 'red')
        width(2*n+1)
        forward(100)
        left(120)
        tri(n-1)    # Recur to draw the rest of the sides!


def spiral(initialLength, angle, multiplier):
    """Spiral-drawing function.  Arguments:
        initialLength = the length of the first leg of the spiral
        angle = the angle, in degrees, turned after each spiral's leg
        multiplier = the fraction by which each leg of the spiral changes
        """
    if initialLength <= 1:
        return     # No more to draw, so stop this call to spiral
    else:
        forward(initialLength)
        left(angle)
        spiral(initialLength*multiplier, angle, multiplier)



def chai(size):
    """Our chai function!"""
        if (size < 5):
            return
                else:
forward(size)
left(90)
    forward(size/2)
    right(90)
    
    right(90)
        forward(size)
        left(90)
        chai(size/2)
        left(90)
        forward(size/2.0)
        right(90)
        backward(size)
        return



def svtree(trunklength, levels):
    """svtree: draws a side-view tree
        trunklength = the length of the first line drawn ("the trunk")
        levels = the depth of recursion to which it continues branching
        """
    if levels == 0:
        return
    else:
        forward(trunklength)
        left(35)
        svtree(trunklength/2, levels-1)
        right(70)
        svtree(trunklength/2, levels-1)
        left(35)
        forward(-trunklength)




def flakeside(sidelength, levels):
    if levels == 0:
    forward(sidelength)
        else:
            #forward(sidelength/3)
#left(60)
#forward(sidelength/3)
#right(120)
#forward(sidelength/3)
#left(60)
#forward(sidelength/3)
#right(60)
flakeside(sidelength/3, levels-1)
left(60)
flakeside(sidelength/3, levels-1)
right(120)
flakeside(sidelength/3, levels-1)
left(60)
flakeside(sidelength/3, levels-1)




def snowflake(sidelength, levels):
    """Fractal snowflake function, complete.
        sidelength: pixels in the largest-scale triangle side
        levels: the number of recursive levels in each side
        """
    flakeside(sidelength, levels)
    left(120)
    flakeside(sidelength, levels)
    left(120)
    flakeside(sidelength, levels)
    left(120)

snowflake(100,3)
