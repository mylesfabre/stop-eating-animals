# CS5 Black, hw4pr1
# Filename: hw4pr1.py
# Name: Myles Fabre
# Problem description: Binary <-> decimal conversions

def isOdd(n):
    '''takes in an integer and returns true if n is odd and false if not'''
    if n == 0:
        return False
    elif n == 1:
        return True
    else:
        if n%2 == 1:
            return True
        else:
            return False

def numToBinary(N):
    """ takes in a number n and returns its in binary"""
    if N == 0:
        return ''
    elif N%2 == 1:
        return  numToBinary((N-1)/2) + '1'
    else:
        return   numToBinary(N/2) + '0'

def binaryToNum(S):
    """ takes in a string of a number in binary and returns the number in base 10"""
    if S == '':
        return 0
    # if the last digit is a '1'...
    elif S[-1] ==  '1':
        return 2*binaryToNum(S[:-1]) + 1
    else: # last digit must be '0'
        return  2*binaryToNum(S[:-1]) + 0

def increment(S):
    if S == "takes in an 8 charachter string of ":
        return 1
    else:
        f = numToBinary(binaryToNum(S)+1)
        if len(f) == 8:
            return f
        else:
            return (8-len(f))*"0" + f

def count(S, n):
    if S == "":
        return "No binary number to count!"
    elif len(S) > 8:
        return count(increment(S[1:]), n-1)
    elif n == 0:
        print(S)
        return None
    else:
        print(S)
        return count(increment(S), n-1)

def numToTernary(N):
    '''the ternary representation of 59 is 2012.
    This is because we basically go 'up' (read right to left) the line in reference to
    the powers of 3 starting with 3^0 = 1. Thus, we move up until we 
    find a power of zero that is more than the number we are evaluating
    the ternary value for and we use the power of 3 below that one. This
    is because we want the most efficient sum of the powers of three to
    get to 59. In this case we use 3^3 = 27, because 3^4 is too large (3^4 = 81).
    Then, 59 is still greater than 27 = so we see if 59 is greater than 2 * 27 
    because we are allowed to use 2's in the ternary system. 59 is greater so we
    place a 2 in the 4th place because that's how many places we are away from the
    end of the '3 power' line. Then we skip the 3rd place and place a 0 there because
    (2 * 27) + (3^2) is greater than 59. We then go to the 2nd place and place a 1
    because 54 can add 3 but not 6. Now we have 57, and we need the last 2 from the 3^0
    place, so we place a 2 there. Thus, we have 2012 representing 59 in ternary.'''
    if N == 0:
        return ''
    elif N%3 == 1:
        return  numToTernary((N-1)/3) + '1'
    elif N%3 == 2:
        return  numToTernary((N-2)/3) + '2'
    else:
        return   numToTernary(N/3) + '0'

def ternaryToNum(N):
    '''Takes in a ternary number and returns it in base 10'''
    if N == '':
        return 0
    # if the last digit is a '1'...
    elif N[-1] ==  '1':
        return 3*ternaryToNum(N[:-1]) + 1
    elif N[-1] == '2':
        return 3*ternaryToNum(N[:-1]) +2
    else: # last digit must be '0'
        return  3*ternaryToNum(N[:-1]) + 0