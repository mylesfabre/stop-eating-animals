# Myles Fabre
#CS5 Gold HW

def matmult(M, v):
    """matmult returns the matrix multiplication Mv.
       M is a list of lists, same # of rows and cols (a square matrix).
       v is a list of the same length as each element (row) of M.
    """

    result = [ ]
    for i in range(len(M)):
        result.append(dot(M[i], v))
    return result

def dot(row, v):
    """Returns the dot product of the list row with the list v.
       Note that row and v should have the same number of elements.
       Otherwise, we will return 0 here...
    """
    if len(row) != len(v):
        return 0

    result = 0
    for i in range(len(v)):
        result = result + row[i]*v[i]
    return result