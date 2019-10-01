# Myles Fabre
# CS5 Black hw2pr3
# Due: 09/24/2019

def LCS(S1, S2):
    """Returns the length of the longest common subsequence of S1 and S1."""
    if S1 == "" or S2 == "":
        return 0
    else:
        if S1[0] == S2[0]:
            return 1 + LCS(S1[1:], S2[1:])
        else:                               
           option1 = LCS(S1, S2[1:]) 
           option2 = LCS(S1[1:], S2)
           return max(option1, option2)

def fancyLCS(S1, S2):
    '''Takes in 2 strings and returns a list with three items: the length
    of the longest subsequence, a copy of S1 and a copy of S2'''
    if S1 == '' and S2 == '':
        return [0, "", ""]
    else:
        wantList = [LCS(S1, S2), symPlace(S1, S2), symPlace(S2, S1)]
        return wantList

def symPlace(S1, S2):
    '''takes in the two strings and sees if the first two elements
    match, if they do, we map the match function which compares elements
    and if the elements don't match, we map an # symbol into the element's
    slot in each list'''
    if S1[0]==S2[0]:
        mapList = list(map(match, S1, S2))
        return mapList
    else:
        option1 = symPlace(S1, S2[1:])   
        option2 = symPlace(S1[1:], S2)
        return max(option1, option2)

def match(ele1, ele2):
    '''checks to see if the elements match, and if not, returns a # symbol'''
    if ele1 == ele2:
        return ele1
    else:
        ele2 = "#"
        return ele2

def align(S1, S2):
    '''does the same thing as fancyLCS, but instead of hashtags, we have dashes'''
    if S1 == '':
        return [0,"-"*len(S2),S2]
    elif S2 == '':
        return [0,S1,"-"*len(S1)]
    elif S1[0] == S2[0]:
        x = align(S1[1:], S2[1:])
        return list(1+x[0],S1[0]+x[1],S2[0]+x[2])
    else:
        useIt1 = align(S1[1:], S2)
        useIt2 = align(S1, S2[1:])
        best = max(useIt1, useIt2)
        return best

'''def dashPlace(S1,S2):
    if S1[0]==S2[0]:
        mapList = list(map(dash, S1, S2))
        return mapList
    else:
        option1 = symPlace(S1, S2[1:])   
        option2 = symPlace(S1[1:], S2)
        return max(option1, option2)'''
    
'''def dash(space1, space2):
    if space1 == space2:
        return space1
    else:
        space2 = "-"
        return space2'''
