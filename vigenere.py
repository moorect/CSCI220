# Name: Christopher Moore
# vigenere.py
#
# Problem: This program uses functions and if statements to determine which button a user clicks
#          then uses the Vigenere cipher to encode or decode the input message using the input
#          key.
#
# Certification of Authenticity:
#
# I certify that this lab is entirely my own work.

from graphics import *

def code(encodeType, message, keyword):

    # Changes key to match length of message

    newKey = ""
    multiplier = int(len(message) / len(keyword))
    remainder = len(message) % len(keyword)

    newKey += keyword * multiplier + keyword[:remainder]

    # Uses newKey to encode/decode message

    output = ""
    i = 0
    if encodeType == "encode":
        for ch in message:
            newCh = chr(((ord(ch) + (ord(newKey[i]) - 65) - 65) % 26) + 65)
            i += 1
            output += newCh
        return output
    elif encodeType == "decode":
        for ch in message:
            newCh = chr(((ord(ch) - (ord(newKey[i]) - 65) - 65) % 26) + 65)
            i += 1
            output += newCh
        return output
    else:
        output = "You didn't click a button. Rerun and try again."
        return output
        
def messageConversion(message):

    # Converts message to upper case and removes spaces

    message = message.upper()
    newMessage = ""

    for ch in message:
        if ch == " ":
            newMessage += ""
        else:
            newMessage += ch

    return newMessage

def main():

    # Draws window with messages, buttons, and entry boxes

    width = 400
    height = 300
    win = GraphWin("Vigenere Cypher", width, height)
    Text(Point(70, 20), "Message to code:").draw(win)
    Text(Point(70, 50), "     Enter keyword:").draw(win)
    inputMessage = Entry(Point(270, 20), 25)
    inputMessage.draw(win)
    inputKey = Entry(Point(203, 50), 10)
    inputKey.draw(win)

    buttonEncode = Text(Point(130, 90), "Encode")
    buttonEncode.draw(win)
    buttonDecode = Text(Point(270, 90), "Decode")
    buttonDecode.draw(win)
    uX1 = 90
    uY1 = 70
    lX1 = 170
    lY1 = 110
    uX2 = 230
    uY2 = 70
    lX2 = 310
    lY2 = 110
    rectangle1 = Rectangle(Point(uX1, uY1), Point(lX1, lY1))
    rectangle1.draw(win)
    rectangle2 = Rectangle(Point(uX2, uY2), Point(lX2, lY2))
    rectangle2.draw(win)
    
    # Button selection

    click = win.getMouse()

    buttonEncode.undraw()
    buttonDecode.undraw()
    rectangle1.undraw()
    rectangle2.undraw()
    
    if click.getX() >= uX1 and click.getX() <= lX1 and click.getY() >= uY1 and click.getY() <= lY1:
        direction = "encode"
    elif click.getX() >= uX2 and click.getX() <= lX2 and click.getY() >= uY2 and click.getY() <= lY2:
        direction = "decode"
    else:
        direction = ""
            
    # Converts message and key to upper case and removes spaces

    inputMessage = inputMessage.getText()
    message = messageConversion(inputMessage)

    inputKey = inputKey.getText()
    inputKey = inputKey.upper()

    # Calls code function
    
    msg = code(direction, message, inputKey)

    Text(Point(width/2, height/2), "Resulting Message:").draw(win)
    Text(Point(width/2, height/2 + 20), msg).draw(win)
    
    closePt = Point(width/2, height-10)
    closeText = Text(closePt, "Click anywhere to close window")
    closeText.draw(win)
    win.getMouse()
    win.close()

main()
