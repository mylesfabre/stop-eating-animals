# Myles Fabre
# CS5 Black Lab Week 1 Problem

def length(L):
    if L == []:
        return 0.0
    else:
        return 1 + length(L[1:])

def dot(L,K):
    if L == [] and K == []:
        return 0.0
    elif length(L) != length(K):
        print("You stupid bitch, you can't take the dot product of different sized lists")
    else:
        return L[0]*K[0] + dot(L[1:],K[1:])

def explode(S):
    if S == '':
        return []
    else: 
        return [S[0]] + explode(S[1:])

def ind(e, L):
    if L == []:
        return 0
    elif e == L[0]:
        return 0
    else:
        return 1+ ind(e, L[1:])

def removeAll(e, L):
    if e == L[0