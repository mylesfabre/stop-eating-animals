# coding: utf-8

#
# Myles Fabre
#

def createDictionary(filename):
    d = {}
    f = open(filename)
    text = f.read()
    f.close()
    split = text.split()
    go = True
    for i in range(len(split)) :
        if go:
            d.setdefault("$", []).append(split[i])
        else :
            d.setdefault(split[i-1], []).append(split[i])
        last = split[i][-1]
        if last == '.' or last == '!' or last == '?' :
            go = True
        else :
            go = False
    return d 


def generateText(d, N):
    """take in a dictionary of word transitions d (generated in your createDictionary 
    function, above) and a positive integer, n. Then, generateText should print a 
    string of n words
    """
    keyList = list(mmodel.keys())
    order = len(keyList[0])
    if numwords == 0:
        print(" ")
    else:
        count = numwords
        while count>0:
            value = randint(0,(len(keyList)-1))
            print(mmodel.keys() + ":" + mmodel.values())


#
# Your 500-or-so-word CS essay (paste into these triple-quoted strings below):
#
"""



"""
#
#
