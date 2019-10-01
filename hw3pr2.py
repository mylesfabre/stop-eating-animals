# Myles Fabre
# hw3pr2 CS5 Black

import time

def ED(first, second):
   '''Returns the edit distance between the strings first and second.'''

   if first == '': 
      return len(second)
   elif second == '':
      return len(first)
   elif first[0] == second[0]:
      return ED(first[1:], second[1:])
   else:
      substitution = 1 + ED(first[1:], second[1:])
      deletion = 1 + ED(first[1:], second)
      insertion = 1 + ED(first, second[1:])
      return min(substitution, deletion, insertion)

def fastED(S1, S2, memo):
    '''Returns the edit distance between the strings first and second... FAST'''
    if (S1,S2) in memo:
        return memo[(S1, S2)]
    elif S1 == S2:
        return 0
    elif S1 == "":
        return len(S2)
    elif S2 == "":
        return len(S1)
    else:
        substitution = 1 + fastED(S1[1:], S2[1:],memo)
        deletion = 1 + fastED(S1[1:], S2, memo)
        insertion = 1 + fastED(S1, S2[1:], memo)
        x = min(substitution, deletion, insertion)
        memo[(S1, S2)] = x
        return x

def topNmatches(word, nummatches, ListOfWords):
    '''Takes in a word, and int n >= 0, and a list of words.
    Returns a list of n words that are alphabetically sorted from lowest edit
    distance to highest'''
    if nummatches == 0:
        return []
    elif ListOfWords == []:
        print("No words to compare to")
        return []
    else:
        n = len(ListOfWords)
        distances = [fastED(word, ListOfWords[i], {}) for i in range(n)]
        distancesAndWords = [[distances[i], ListOfWords[i]] for i in range(n)]
        distancesAndWords.sort()
        topN = distancesAndWords[0:nummatches]
        #alphatop3 = min( top3[0][1] , top3[1][1], top3[2][1])
        #alphatop3 = [top3[0][1] , top3[1][1], top3[2][1]]
        topWords = [topN[i][1] for i in range(nummatches)]
        topWords.sort()
        return topWords

def nonAtopNmatches(word, nummatches, ListOfWords):
    '''Takes in a word, and int n >= 0, and a list of words.
    Returns a list of n words that are sorted from lowest edit
    distance to highest'''
    if nummatches == 0:
        return []
    elif ListOfWords == []:
        print("No words to compare to")
        return []
    else:
        n = len(ListOfWords)
        distances = [fastED(word, ListOfWords[i], {}) for i in range(n)]
        distancesAndWords = [[distances[i], ListOfWords[i]] for i in range(n)]
        distancesAndWords.sort()
        topN = distancesAndWords[0:nummatches]
        return topN

def spam():
    """loads in a largeMasterFile and checks to see if the word is in the file
    otherwise, it runs a non alphabetical version of topMatches and returns a 
    list of the 10 closest words"""
    f = open("3esl.txt")
    contents = f.read()
    words = contents.split("\n")
    userInput = input("spell check> ")
    if userInput in words:
        return True
    else:
        startTime = time.time()
        result = nonAtopNmatches(userInput, 10, words)
        endTime = time.time()
        print("Time elapsed executing nonAtopMatches ", endTime - startTime)
        return result