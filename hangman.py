# Christopher Moore
# hangman.py
# Problem: This program plays a game of Hangman using a text file containing secret
#          words.
# Certification of Authenticity:
#
# I certify that this lab is my own work, but I discussed it with Professor Stalvey
# many, many times (sorry).

from random import *
from graphics import *

# Opens, reads, and closes text file containing secret words
def getFile():
    infile = open("wordlist.txt", "r")
    for line in infile:
        dataList = line.split()
        # print("Data List: " + dataList)
    infile.close()
    return dataList


# Chooses a random secret word from the list of words
def wordPick(dataList):
    i = randint(0,len(dataList)-1)
    wordChoice = dataList[i]
    return wordChoice


# Draws and plays the entire game of Hangman
def game(word):
    word = list(word)
    blanksWord = ['_', '_', '_', '_']
    previousGuesses = []
    badGuesses = []
    incorrectGuesses = 0
    hasWon = False

    width = 600
    height = 600
    win = GraphWin("Hangman", width, height)

    # GALLOWS
    Line(Point(200, 50), Point(200, 20)).draw(win)
    Line(Point(200, 20), Point(400, 20)).draw(win)
    Line(Point(400, 20), Point(400, 400)).draw(win)
    Line(Point(380, 400), Point(420, 400)).draw(win)

    # Creates body parts and stores into list
    head = Circle(Point(200, 80), 20)               #HEAD
    uBody = Line(Point(200, 100), Point(200, 185))  #UPPER BODY
    lArm = Line(Point(200, 170), Point(170, 150))   #LEFT ARM
    rArm = Line(Point(200, 170), Point(230, 150))   #RIGHT ARM
    lBody = Line(Point(200, 185), Point(200, 300))  #LOWER BODY
    lLeg = Line(Point(200, 300), Point(170, 320))   #LEFT LEG
    rLeg = Line(Point(200, 300), Point(230, 320))   #RIGHT LEG
    bodyParts = [head, uBody, lArm, rArm, lBody, lLeg, rLeg]

    # Draws blanks
    outputBlanks = Text(Point(300, 500), "")
    outputBlanks.draw(win)
    outputBlanks.setText(blanksWord)

    # Draws Remaining Guesses
    Text(Point(500, 100), "Guesses Remaining:").draw(win)
    outputGuesses = Text(Point(500, 130), "")
    outputGuesses.draw(win)
    outputGuesses.setText(7-incorrectGuesses)

    # Draws Guessed Letters
    Text(Point(width/2-50, height-20), "Letters Used:").draw(win)
    outputLetters = Text(Point(350, 580), "X")
    outputLetters.draw(win)
    outputLetters.setText(previousGuesses)

    # Sets response area
    response = Text(Point(300, 430), "")
    response.draw(win)

    # Inputs the user's guess
    Text(Point(width/2-50, height-50), "Guess a letter:").draw(win)
    inputGuess = Entry(Point(width/2+50, height-50), 5)
    inputGuess.draw(win)
    
    while (incorrectGuesses < 7 and hasWon == False):
        outputBlanks.setText(blanksWord)
        outputGuesses.setText(7-incorrectGuesses)
        outputLetters.setText(previousGuesses)

        win.getMouse()
        guess = inputGuess.getText()
        
        if previousGuesses.count(guess) > 0:
            # Duplicate guess
            response.setText("You've already guessed that letter")
        elif word.count(guess) > 0:
            # Correct Guess
            response.setText("That letter IS in the word!")
            updateBlank(blanksWord, guess, word)
        else:
            # Incorrect Guess
            bodyParts[incorrectGuesses].draw(win)
            incorrectGuesses += 1
            previousGuesses.append(guess)
            response.setText("That letter is NOT in the word")
            
        hasWon = gameDone(blanksWord)

    if hasWon == True:
        response.setText("******  YOU WIN!  ******")
        outputBlanks.setText(word)
    else:
        response.setText("YOU LOSE!  :(")
        outputBlanks.setText(word)

# Makes buttons and asks player for another game
    outputAgain = Text(Point(275, 470), "Play again?")
    outputAgain.draw(win)
    buttonYes = Text(Point(330, 470), "Yes")
    buttonYes.draw(win)
    buttonNo = Text(Point(360, 470), "No")
    buttonNo.draw(win)
    uX1 = 315
    uY1 = 460
    lX1 = 345
    lY1 = 480
    uX2 = 345
    uY2 = 460
    lX2 = 375
    lY2 = 480
    rectangle1 = Rectangle(Point(uX1, uY1), Point(lX1, lY1))
    rectangle1.draw(win)
    rectangle2 = Rectangle(Point(uX2, uY2), Point(lX2, lY2))
    rectangle2.draw(win)

    click = win.getMouse()

    if click.getX() >= uX1 and click.getX() <= lX1 and click.getY() >= uY1 and click.getY() <= lY1:
        playAgain = "yes"
        win.close()
    else:
        playAgain = "no"
        win.close()
    return playAgain


# Updates the blanked out word if a correct guess is made
def updateBlank(blanksWord, guess, word):

    for i in range(len(word)):
        if word[i] == guess:
            blanksWord[i] = guess


# Determines if the game has been won or not
def gameDone(blanksWord):

    if blanksWord.count("_") > 0:
        hasWon = False
    else:
        hasWon = True
            
    return hasWon


def main():

    playAgain = "yes"
    while playAgain != "no":
        wordList = getFile()
        word = wordPick(wordList)
        playAgain = game(word)

main()
