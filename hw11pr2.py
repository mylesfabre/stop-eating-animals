# Myles Fabre
# CS5 hw11pr2.py
# AI Connect4
import random

class Board:
    '''datatype: a connect 4 board with given columns
    and rows'''
    def __init__(self, width, height):
        '''constructor for Board'''
        self.width = width
        self.height = height
        W = self.width
        H = self.height
        self.data = [[' ']*W for row in range(H)]

    def __repr__(self):
        '''returns a string representation of Board'''
        H = self.height
        W = self.width
        s = ''

        for r in range(H):
            s += '|'
            for c in range(W):
                s+= self.data[r][c] + '|'
            s += '\n'
        s += (2*W+1)*'-'

        s += '\n'
        num = 0
        s += ' '

        for e in range(W):
            s += str(num%10)
            num += 1
            s += ' '

        return s

    def addMove(self, col, ox):
        H = self.height
        for row in range(0,H):
            if self.data[row][col] != ' ':
                self.data[row-1][col] = ox
                return
        
        self.data[H-1][col] = ox

    def clear(self):
        for f in range(len(self.data)):
            for i in range(len(self.data[f])):
                if self.data[f][i] == "X" or self.data[f][i] == "O":
                    self.data[f][i] = " "
        return 

    def setBoard(self, moveString):
        """Accepts a string of columns and places
           alternating checkers in those columns,
           starting with 'X'.
           MoveString must be a string of one-digit integers.
        """
        nextChecker = 'X'   # start by playing 'X'
        for colChar in moveString:
            col = int(colChar)
            if 0 <= col <= self.width:
                self.addMove(col, nextChecker)
            if nextChecker == 'X':
                nextChecker = 'O'
            else:
                nextChecker = 'X'

    def allowsMove(self, c):
        '''True if c is inbounds and open.
        False otherwise.'''
        H = self.height
        W = self.width
        D = self.data
        if c < 0 or c >= W:
            return False
        elif D[0][c] != ' ':
            return False
        else:
            return True

    def isFull(self):
        for x in range(self.width):
            if self.allowsMove(x)==True:
                return False
        return True

    def delMove(self, c):
        for i in range(self.height):
            if self.data[i][c]!=" ":
                self.data[i][c]=" "
                return 

    def winsFor(self, ox):
        ''' checks to see if ox wins'''
        for i in range(self.height):
            for j in range(self.width):
                if inarow_Neast(ox,i,j,self.data,4) or inarow_Nnortheast(ox,i,j,self.data,4) or inarow_Nsouth(ox,i,j,self.data,4) or inarow_Nsoutheast(ox,i,j,self.data,4):
                    return True
        return False

    def hostGame(self):
        print("BOOM! You are now playing:\n**Connect 4**")
        print(self)
        print("Enter not a number to exit")
        while True:
            users_col = -69
            while self.allowsMove(users_col) == False:
                users_col = int(input("X? Where do you want to go?"))
            self.addMove(users_col, "X")
            print(self)
            if self.winsFor("X"):
                print("Player X Won HAHA")
                return
            if self.isFull():
                print("NOBODY WINS\nPLAY AGAIN")
                return
            users_col = -69
            while self.allowsMove(users_col) == False:
                print("Computer move:")
                users_col = self.aiMove("O")
                print('aasdf: {}'.format(users_col))
            self.addMove(users_col,"O")
            print(self)
            if self.winsFor("O"):
                print("The Computer WON! U stupid!! HAHA!! ")
                return
            if self.isFull():
                print("NOBODY WINS\nPLAY AGAIN")
                return
    
    def colsToWin(self,ox):
        ''' returns a list of cols where ox can move to win and
         finish the game'''
        colList = [ ]
        W = self.width
        for i in range(W):
            if self.allowsMove(i):
                self.addMove(i, ox)
                if self.winsFor(ox):
                    colList.append(i)
                self.delMove(i)
        return colList

    def aiMove(self, ox):
        '''returns a single integer, which must be a legal column
         in which to make a move'''
        if len(self.colsToWin(ox)) != 0:
             singleMove = self.colsToWin(ox)
             # self.addMove(singleMove, ox)
             return random.choice(singleMove)
        elif ox in ["o", "O", "0"]:
            if len(self.colsToWin("X")) != 0:
                singleMoveOpp = self.colsToWin("X")
                # self.addMove(singleMoveOpp, ox)z
                return random.choice(singleMoveOpp)
        elif ox in ["x", "X"]:
            if len(self.colsToWin("O")) != 0:
                singleMoveOpp2 = self.colsToWin("O")
                # self.addMove(singleMoveOpp2, ox)
                return random.choice(singleMoveOpp2)
        colNum = list(range(0,self.width))
        goodList = list(filter(lambda x: self.allowsMove(x), colNum))
        return random.choice(goodList)


def inarow_Neast( ch, r_start, c_start, A, N ):
    """ starting from (row,col) of (r_start,c_start)
        within 2d list-of-lists A (array)
        returns True if there are N ch's in a row and
        returns False otherwise
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start > H-1: return False # out of bounds row
    if c_start < 0 or c_start+(N-1) > W-1: return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start][c_start+i] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

def inarow_Nsouth( ch, r_start, c_start, A, N ):
    """ starting from (row,col) of (r_start,c_start)
        within 2d list-of-lists A (array)
        returns True if there are N ch's in a row and
        returns False otherwise
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start+(N-1) > H-1: return False # out of bounds row
    if c_start < 0 or c_start > W-1: return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start+i][c_start] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

def inarow_Nnortheast( ch, r_start, c_start, A, N ):
    """ starting from (row,col) of (r_start,c_start)
        within 2d list-of-lists A (array)
        returns True if there are N ch's in a row and
        returns False otherwise
    """
    H = len(A)
    W = len(A[0])
    if r_start-(N-1) < 0 or r_start > H-1: return False # out of bounds row
    if c_start < 0 or c_start+(N-1) > W-1: return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start-i][c_start+i] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

def inarow_Nsoutheast( ch, r_start, c_start, A, N ):
    """ starting from (row,col) of (r_start,c_start)
        within 2d list-of-lists A (array)
        returns True if there are N ch's in a row and
        returns False otherwise
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start+(N-1) > H-1: return False # out of bounds row
    if c_start < 0 or c_start+(N-1) > W-1: return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start+i][c_start+i] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True