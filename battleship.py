"""Battleship
Basic battleship game between two players
Written by Seth Schroeder"""
from board import * #handles the board displays
#import ships

#declare 4 boards for each user, one is their view of their opponent, the other their own

playerOneBoard() = Board() #Player 1's view of their own board & ships
playerTwoBoard() = Board() #Player 2's view of their own board & ships


#Instantiate each user's ships



def enterShips (): #Function for entering ships
    print("This is a battle of wits. Enter your ship's positions!\n")
    print("Player 1 first\n")
    print("Carrier, 5 studs\n")
    print("Enter coordinates like this: \"h1,h5\" (no spaces!)")
    #break into column and row variables and init carrier ship
    
    #TODO: catch all exceptions and rerun
    

