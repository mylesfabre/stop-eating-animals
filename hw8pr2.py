# Myles Fabre
# CS5 Black hw8pr2.py
# Markov Text Generation
from random import randint
import random

def dollarify (wordList, k):
    splitWordList = wordList.split()
    if splitWordList == []:
        return []
    else:
        for i in range(k):
            splitWordList.insert(0, "$")
            i+=1
        for m in range(len(splitWordList)):
            if len(splitWordList[m]) > 1:
                for p in range(k):
                    splitWordList.insert(m+1, "$")
                    p+=1
                m+=1
            else:
                m+=1
    return splitWordList

def markov_model(wordList, k):
    markModel = {}
    key = ('$',)*k   
    orig_key = ('$',)*k
    for i in range(len(wordList)):
        word = wordList[i]  
        if key not in markModel:
            markModel[key]=[word]
        else:
            markModel[key]+=[word]
        key = key[1:]+(word,)
        if word[-1] in '.!?':
            key = orig_key
    return markModel


def gen_from_model(mmodel, numwords):
    keyList = list(mmodel.keys())
    order = len(keyList[0])
    if numwords == 0:
        print(" ")
    else:
        count = numwords
        while count>0:
            value = randint(0,(len(keyList)-1))
            print(mmodel.keys() + ":" + mmodel.values())

def markov(fileName, k ,length):
    f1 = open(fileName, "w")
    inputList = f1.readlines()
    mm1 = markov_model(inputList,k)
    gen_from_model(mm1, length)
    f1.close()

        # if len(splitWordList[i]) == 1:
        #     if splitWordList[i] in singleElements:
        #         pass
        #     else:
        #         singleElements.append(splitWordList[i])
        # else:
        #     if splitWordList[i][0] in singleElements:
        #         pass
        #     else:
        #         singleElements.append(splitWordList[i][0])
        #         singleElements.append("$")
        #         singleElements.append("$")
    # mixOfElements = mixMaker(singleElements, k, 1)
    # tupleElements = tupleMaker(mixOfElements)
    # dictElement = []
    # for u in range(len(tupleElements)):
    #     for k in range(len(tupleElements[0]-1)):
    #         if tupleElements[u][k] in wordList:
    #             #markModel{}.append(tupleElements[u][k])
    #             pass

# def mixMaker(wordList, k, num):
#     if num == 1:
        
#         pass
#     else:
#         pass
#     if wordList == [] or len(wordList) < k :
#         return mix
#     else:
#         if k == 1:
#             mix.append(wordList[0])
#             return mixMaker(wordList[1:], k, 0)
#         else:
#             mix.append([wordList[0:k-1]])
#             return mixMaker(wordList[1:], k, 0)

# def tupleMaker(meat):
#     newList =[] 
#     for y in range(len(meat)):
#         newList.append(tuple(meat[y]))
#     return newList

# def stop(tuple1):
#     return len(tuple1)