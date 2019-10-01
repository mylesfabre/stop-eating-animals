# Myles Fabre
# CS5 Black hw2pr4
# Due: 09/24/2019

def explode(S):
    """Separates the string into a list so we can access elements""" 
    if S == '':
        return []
    else: 
        return [S[0]] + explode(S[1:])

def complement(base1, base2):
    """Returns boolean indicating whether two RNA bases are complementary."""
    if base1=="A" and base2=="U":
        return True
    elif base1=="U" and base2=="A":
        return True
    elif base1=="C" and base2=="G":
        return True
    elif base1=="G" and base2=="C":
        return True
    else:
        return False

'''def fold(RNA):
    nukeTides = explode(RNA)
    total = 0
    if nukeTides == []:
        return "0"
    elif not complement(nukeTides[0], nukeTides[1:]):
        return "0"
    else:
        if complement(nukeTides[0], nukeTides[1:]):
            total += 1
            fold(RNA)
        else:
            return total'''

def countX(lyst, x): 
    count = 0
    if x not in lyst: 
        return count
    else:
        count +=1
        return countX(lyst[1:],x)

def one(lystElement):
    if lystElement == True:
        return True
    else:
        return False

# def fold(RNA):
#    nukeTides = RNA
#     #yesNo = list(filter(complement, nukeTides))
#     #if True in yesNo:
#     if nukeTides == []:
#         return "No RNA fold matches"
#     else:
#         return countX(list(filter(complement, fold(nukeTides)[1:])), True)
#     '''if len(yesNo)>=1:
#         return countX(yesNo, True)
#     else:
#         print("No RNA fold matc hes")
#         return 0'''


#To Prof Dodds: THANK YOU
def fold(R):
    if R == '' or len(R) == 1:
        return 0
    else:
        RR = range(1, len(R))
        f = lambda x: complement(R[x], R[0])
        LI = list(filter(f, RR))
        if LI == []:
            return fold(R[1:])
        else:
            return 1 + max(map(lambda x: fold(R[1:x])+fold(R[x+1:]), LI))