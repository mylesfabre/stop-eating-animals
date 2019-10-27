# Myles Fabre
# 10/02/2019
# hw4pr3.py

import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from functools import *

# A sample 8x8 image represented as a sequence of 64 bits
test1 = "0000001100001100000000110000001111111111111111111111111111111111"

def powerOfTwo(num):
    # CODE SUPPLIED BY INSTRUCTOR.
    """Accepts a positive integer and returns True if and only if it
       is a power of two. """
    if num == 1:
        return True
    elif num % 2 == 1:
        return False
    else:
        return powerOfTwo(num//2)

def pngToArray(filename, threshold = 2):
    # CODE SUPPLIED BY INSTRUCTOR
    """Accepts the name of a file that contains a .png image, and
       returns a binary 2D array as output.  The image must be a
       square whose dimensions are a power of two.  Pixels whose
       total brightness are less than the threshold will be rendered
       as black; all others will become white."""
    img = mpimg.imread(filename)        # Read the image
    dimensions = img.shape              # Get the dimensions
    rows = dimensions[0]                # Extract the number of rows...
    columns = dimensions[1]             # ... and columns
    # Insist on appropriate dimensions
    if rows != columns or not powerOfTwo(rows):
        return None  
    image = []                          # This will become the final image
    for r in range(rows):
        row = []
        for c in range(columns):
            if sum(img[r][c]) >= threshold:
                row.append(0)
            else:
                row.append(1)
        image.append(row)
    return image

def renderASCII(array):
    # CODE SUPPLIED BY INSTRUCTOR
    """Accepts a 2D array of 0's and 1's and renders it on the screen
       in ASCII, using spaces and asterisks to represent 0's and 1's,
       respectively."""
    for row in array:
        row = list(map(lambda x: ' ' if x == 0 else '*', row))
        stringify = reduce(lambda x, y: x + y, row)
        print(stringify)
            
def renderImage(array):
    # CODE SUPPLIED BY INSTRUCTOR
    """Accepts a 2D array of 0's and 1's and renders it on the screen
       using matplotlib."""
    dim = len(array)
    image = np.zeros((dim, dim), dtype = np.float)
    for r in range(dim):
        for c in range(dim):
            image[r][c] = float(array[r][c]) 
    plt.imshow(image, cmap = "Greys", interpolation = 'nearest')
    plt.show()
    
def stringToArray(bstring):
    # CODE SUPPLIED BY INSTRUCTOR
    """Accepts a binary string input and returns its 2D array
       representation as an image."""
    dim = int(math.sqrt(len(bstring)))
    charArray = [list(bstring[i:i+dim]) for i in range(0, len(bstring), dim)]
    array = [ [int(x) for x in row] for row in charArray ]
    return array

def quadrants(array):
    """Accepts an array of bits and returns a list of quadrants of the
    form [NW, NE, SW, SE] where each entry is the array for that quadrant."""
    # if len(array) < 4 or len(array)%16 != 0:
    #     print("Array not capable of quadrants")
    #     return None
    # else: 
    firstHalf = [array[x] for x in range(len(array)//2)]
    secondHalf = array[len(array)//2:len(array)]
    firstQuarter = [firstHalf[x][0:len(firstHalf[0])//2]for x in range(len(array)//2)]
    secondQuarter = [firstHalf[x][len(firstHalf[0])//2:]for x in range(len(array)//2)]
    thirdQuarter = [secondHalf[x][0:len(secondHalf[0])//2]for x in range(len(array)//2)]
    fourthQuarter = [secondHalf[x][len(secondHalf[0])//2:]for x in range(len(array)//2)]
    # firstQuarter = [array[x] for x in firstHalfLong[0:len(firstHalfLong)//2]]
    # secondQuarter = [array[x] for x in firstHalfLong[(1+ len(firstHalfLong)//2):(len(firstHalfLong))]]
    # secondHalfLong = array[halfMult:]
    # thirdQuarter = [array[x] for x in secondHalfLong]
        # secondQuadLong = array[quadMult: (quadMult * 2)]
        # thirdQuadLong = array[(quadMult * 2):(quadMult * 3)]
        # fourthQuadLong = array[(quadMult * 3): (4 * quadMult)]
        # firstQuad = [firstQuadLong[0:3], firstQuadLong[4:8], firstQuadLong[9:12], firstQuadLong[13:16]]
        # secondQuad = [secondQuadLong[0:3], secondQuadLong[4:8], secondQuadLong[9:12], secondQuadLong[13:16]]
        # thirdQuad = [thirdQuadLong[0:3], thirdQuadLong[4:8], thirdQuadLong[9:12], thirdQuadLong[13:16]]
        # fourthQ = [fourthQuadLong[0:3], fourthQuadLong[4:8], fourthQuadLong[9:12], fourthQuadLong[13:16]]
        # quads = firstQuad + secondQuad + thirdQuad + fourthQuad
    quads = [firstQuarter, secondQuarter, thirdQuarter, fourthQuarter]
    return quads

def solidZero(array):
    """Accepts a 2D binary array and returns True if every bit is a 0
       and False otherwise."""
    return max(max(array)) == 0

def solidOne(array):
    """Takes a 2D binary array as input and returns True if every bit
       is a 1 and False otherwise."""
    return min(min(array)) == 1

def makeQuadTree(array):
    """Returns a quadtree representation of the given array."""
    if solidOne(array):
        newArray = list(map(lambda x: array[x]=1, array))
        return newArray
    elif solidZero(array):
        coolArray = list(map(lambda x: array[x]=0 , array))
        return coolArray
    else:
        newArray = [makeQuadTree(i) for i in array]
        return newArray

    # TFList0 = list(map(lambda x: solidZero(array[x]) for x in len(array), array))
    # TFList1 = list(map(lambda x: solidOne(array[x]) for x in len(array), array))
    # if True in TFList0 and True in TFList1:
    #     num = TFList0.index(True)
    #     array[num] = 0
    #     num2 = TFList1.index(True)
    #     array[num2] = 1
    #     return array
    # elif True in TFList0 and True not in TFList1:
    #     num = TFList0.index(True)
    #     array[num] = 0
    #     return array
    # elif True not in TFList0 and True in TFList1:
    #     num2 = TFList1.index(True)
    #     array[num2] = 1
    #     return array
    # else:
    #     return array

def solidArray(value, pixels):
    """Accepts a value (0 or 1) and a number of pixels, and returns a
    2D array of pixels-by-pixels bits, all of which are set to the
    given value."""
    return [[value]*pixels for row in range(pixels)]

def makeArray(quadtree, dim):
    """Given a quadtree and a dimension, returns the 2D array
    representation of the quadtree."""
    #separateList = 
    
    #return array

def rotateRight(quadtree):
    """Given a quadtree, returns the quadtree that results after
       rotating that image clockwise 90 degrees."""
    
    return result

def flipHorizontal(quadtree):
    """Given a quadtree, returns the quadtree that results from
    flipping the image about the horizontal axis of symmetry."""
    return result

def flipDiagonal(quadtree):
    """Given a quadtree, returns the quadtree that results from
       flipping the image about the diagonal line through the NE and
       SW corners of the image."""
    
    #return result

def invert(quadtree):
    """Given a quadtree, returns the quadtree that results replacing
       every white pixel with a black pixel and vice versa."""

    #return result