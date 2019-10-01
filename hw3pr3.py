# Myles Fabre
# CS5 Black hw3pr2.py

from functools import reduce

miniWordList = ["a", "am", "amp", "ample", "as", "asp", "at", "ate", "sat",
                "spa", "spam", "tea", "was", "wasp"]

def getInput():
    userInput =   input("Enter some words: ")
    print(userInput)          # prints the userInput string
    print(userInput.split())  # splits the userInput into a list of strings and prints that list

def wordBreak(string):
    scoreFunction = len          # We're setting the scoring function.  We can change that function to something else!
    wordList = miniWordList      # We're setting the list of valid words.  It can be changed to something else!
    userInput = input("Enter your best solution: ")  # Get user input
    userList = userInput.split() # Split the input string into a list of strings
    if check(userList, string, wordList):
        userScore = reduce(lambda x, y: x + y, map(scoreFunction, userList))
        print("Your score was ", userScore)
        best = showStringScore(string, scoreFunction, wordList, {})
        print("Best solution is ", best)
    else:
        print("Your solution wasn't valid!")

def check(playerList, string, wordList):
    #h = len(playerList)
    # #if (playerList[i] in string for i in range(h):
    #     return True
    # else:
    #     return False
    #TFList = map(in, playerList)
    if playerList == []:
        return True
    elif playerList[0] in string and wordList:
        '''r is the length of playerList plus the index of where it is in the string'''
        r = len(playerList[0]) + string.find(playerList[0])
        return check(playerList[1:],string[r:] , wordList)
    else:
        return False
    #else:
        #return False

    # if playerList[i]
    #     return True
    # elif playerList[i] for i in range (h) in string:
    #     return True
    # else:
    #     return False

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


def stringScore(string, scoreFunction, wordList, memo):
    if string == '':
        return 0
    elif wordList == []:
        return 0
    elif wordList[0] not in string:
        return stringScore(string, scoreFunction, wordList[1:], memo)
    else:
        r = len(wordList[0]) + string.find(wordList[0])
        useIt = scoreFunction(wordList[0]) + stringScore(string[r:],scoreFunction,wordList,memo)
        loseIt = stringScore(string[r:],scoreFunction,wordList[1:],memo)
        return max(useIt, loseIt)
        
def showStringScore(string, scoreFunction, wordList, memo):
    return [stringScore(string, scoreFunction, wordList, memo), nonAtopNmatches(wordList[0], len(wordList), string)]