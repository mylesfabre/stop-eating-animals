# Myles Fabre
# CS5 Black Making Change HW

from math import *

def add(x,y):
    return x+y

#makes a useful list of coins that are valued below money
    def numCoins(money, coinType):
        usefulList = list(filter(lambda money: money <= coinType[0:], coinType))
        counterList = []
        counterList.append(money)
        #need to try multiples of coins
    if money == usefulList[-1]:
        return 1
    else:
        moneySum = reduce(add, usefulList[-1:-1])
       if moneySum == money:
           return len.usefulList
        elif moneySum > money:
            #subtract 

def moneyCount(money, coinType):
    

def change(money, coinType):
    if money == 0:
        print("0")
        return 0
    elif coinType[0] != 1:
        print("inf")
        return 0
    else:
        
        return 