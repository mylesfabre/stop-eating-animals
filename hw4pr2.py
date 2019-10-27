# Myles Fabre
#CS5 Black hw4pr2.py

import binascii

def numToBaseB(N, B):
    '''Takes in a nonnegative integer N and a base B between
    2 and 10 inclusive, and returns a string representing
    N in base B'''
    if B <= 1 or B > 10:
        print("Base not in the 2 to 10 range")
        return None
    elif N < 0:
        print("N is negative and you need another program to figure that out")
        return None
    elif N == 0:
        return str(0)
    elif N == 1:
        return str(1)
    else:
        if N%B == 1:
            return numToBaseB((N-1)/B, B) +"1"
        elif N < B:
            return str(N)
        elif N == B:
            return str(10)
        elif B > 2 and (N - B) == B:
            return str(20)
        else:
            return numToBaseB((N//B), B) + str(N%B)

def baseBToNum(S, B):
    '''takes in a number in string form represented in base B and
    returns the number as an int in base 10'''
    if S == " " or "":
        return 0
    elif S == "1":
        return 1
    elif len(S)>1:
        retValue = int(S[-1]) + (B * baseBToNum(S[:-1], B))
        return int(retValue)
    else:
        if B > int(S):
            return int(S)
        else:
            print("Invalid Number and Base Combo")
            return None

def baseToBase(B1, B2, SinB1):
    '''accepts 2 bases, B1 and B2, and a number in string
     form represented in B1. It returns the number in B1
     in B2'''
    num = baseBToNum(SinB1, B1)
    finalNum = numToBaseB(num, B2)
    return finalNum

def add(S, T):
    num1 = baseBToNum(S, 2)
    num2 = baseBToNum(T, 2)
    sum = num1 + num2
    final = numToBaseB(sum, 2)
    return final

def helper(xresult):
    wordInAscii = map(binascii.b2a_uu, xresult[0:7]) + helper(xresult[7:])
    regularWord = map(ord, wordInAscii)
    return regularWord

def xorStrings(S1, S2):
    if len(S1) != len(S2):
        print("WRONG! The lengths don't match up, cannot compute.\n")
        return None
    else:
        byteS1 = bytearray(S1, 'ascii')
        binS1 = int(bin(byteS1[0]).split('b')[1])
        byteS2 = bytearray(S2, 'ascii')
        binS2 = int(bin(byteS2[0]).split('b')[1])
        # binS1 = baseBToNum(S1, 2)
        # binS2 = baseBToNum(S2, 2)
        # encryptedS1 = binS1^binS2
        xorResultInt = binS1^binS2
        xorResultString = str(xorResultInt)
        return helper(xorResultString)
        