# Myles Fabre
# CS5 Black Scrabble HW

scrabbleScores = [ ["a", 1], ["b", 3], ["c", 3], ["d", 2], ["e", 1], 
                   ["f", 4], ["g", 2], ["h", 4], ["i", 1], ["j", 8], 
                   ["k", 5], ["l", 1], ["m", 3], ["n", 1], ["o", 1], 
                   ["p", 3], ["q", 10], ["r", 1], ["s", 1], ["t", 1], 
                   ["u", 1], ["v", 4], ["w", 4], ["x", 8], ["y", 4], 
                   ["z", 10] ]


nanoDictionary = ["a", "am", "at", "apple", "bat", "bar", "babble", 
                  "can", "foo", "spam", "spammy", "zzyzva"]

def possibleWords(rack, word):
    myList = list(filter(lambda x: x in rack, word))
    if len(word) == len(myList):
        return True
    return False

def oneWord(letters, w):
    if w == "": return True
    if w[0] not in letters: return False
    letterscopy = letters[:]
    letterscopy.remove(w[0])
    return oneWord( letterscopy  , w[1:] )

def allWords(letters, dictionary):
    # if letters == []:
    #     return [['', 0]]
    # loseIt = allWords(letters[1:])
    # currentScore = list(filter(lambda x: x[0]==letters[0],scrabbleScores))[0][1]
    # useIt = list(map(lambda x: [letters[0]+x[0], currentScore+x[1]], loseIt))
    # return useIt + loseIt
    if letters == []:
        return [[0, '']]
    elif dictionary == []:
        return []
    else:
        if possibleWords(letters, dictionary[0]) == True:
            return getScore(dictionary[0], letters) + allWords(letters, dictionary[1:])
        else:
            return allWords(letters, dictionary[1:])
            
def add(x,y):
    return x+y

#rack is a list of lower case numbers
#dictionary is a list of words
#returns a list of lists

#takes in list of strings (LoS), the dictionary
#def firstLetter(LoS):
 #   if LoS == []:
    #    return 0
 #   else:
  #      return list(filter())
        
def wordsInNano(words, dictionary):
    # if words == []:
    #     return []
    # rest = wordsInNano(words[1:], dictionary)
    # if words[0][0] in dictionary:
    #     return [words[0]] + rest
    # else:
    #     return rest
    filteredList = list(filter(lambda pair: pair[0] in dictionary,words))
    return filteredList

'''def scoreList(rack, dictionary):
    if rack == []:
        print("You can't make words without letters")
        return []
    else:
        words = allWords(rack)
        return wordsInNano(words, dictionary)'''

def letScore( let, SS ):
    if SS==[]: return 0
    if SS[0][0] == let: return SS[0][1]
    return letScore(let, SS[1:])
        
def getScore(word, rack):
    if word == "":
        return 0
    else:
        if word[0] in rack:
            return list(rack[word[0]] + getScore(word[1]), word[0])
    
def getMax(scoreWords):
    if scoreWords == []:
        return ["",0]
    else:
        head = scoreWords[0]
        rest = getMax(scoreWords[1:])
        if head[1]>=rest[1]:
            return head
        else:
            return rest

def bestWord(rack, dictionary):
    if rack == []:
        return []
    else:
        return getMax(scoreList(rack, dictionary))