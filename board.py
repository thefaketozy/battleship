#a class for the users' boards
#
#0 = nothing, 2 = destroyer, 3 = cruiser, 4 = battleship, 5 = carrier

class Board:
    def __init__(self):
        self.board = {'a': [0, 0, 0, 0, 0, 0, 0, 0],
                      'b': [0, 0, 0, 0, 0, 0, 0, 0],
                      'c': [0, 0, 0, 0, 0, 0, 0, 0],
                      'd': [0, 0, 0, 0, 0, 0, 0, 0],
                      'e': [0, 0, 0, 0, 0, 0, 0, 0],
                      'f': [0, 0, 0, 0, 0, 0, 0, 0],
                      'g': [0, 0, 0, 0, 0, 0, 0, 0],
                      'h': [0, 0, 0, 0, 0, 0, 0, 0]}

    def addShip(self, firstRow, firstCol, lastRow, lastCol, size):
        firstCol = firstCol - 1 #Subtract 1 because we're counting from 0
        lastCol = lastCol - 1
        if firstRow == lastRow: #The ship is horizontal
            i = firstCol
            while i <= lastCol:
                self.board[firstRow][i] = size
                i += 1
        elif firstCol == lastCol: #The ship is vertical
            #use chr(ord(ch) + 1) to increment the rows
            i = ord(firstRow)
            while i <= ord(lastRow):
                self.board[chr(i)][firstCol] = size
                i += 1

        return
    def fire(row, col):
        if self.board[row][col] == 2 or 3 or 4 or 5:
            return True
        else:
            return False

        #return hit or miss (True or False)
    def checkSinks(): #A poorly written function that loops through board to check for sinked ships
        #Check for absence of all of 2, 3, 4 or 5
        #CALL AFTER A SUCCESSFUL HIT
        return
       
    #TODO write board printing function

    
    #TODO Come up with better symbols for these at printing

class shootBoard: 
    def __init__(self):
    #Dictionary: 0 nothing, 1 hit, 2 miss
        self.board = {'a': [0, 0, 0, 0, 0, 0, 0, 0],
                      'b': [0, 0, 0, 0, 0, 0, 0, 0],
                      'c': [0, 0, 0, 0, 0, 0, 0, 0],
                      'd': [0, 0, 0, 0, 0, 0, 0, 0],
                      'f': [0, 0, 0, 0, 0, 0, 0, 0],
                      'g': [0, 0, 0, 0, 0, 0, 0, 0],
                      'h': [0, 0, 0, 0, 0, 0, 0, 0]}
    def hit(self, row, col):
        self.board[row][col] = 1
        return
    def miss(self, row, col):
        self.board[row][col] = 2
        return

                