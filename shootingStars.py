# Name: Christopher Moore
# shootingStars.py
#
# Problem: This program creates a greeting card displaying a house and shooting stars.
#
# Certification of Authenticity:
#
# I certify that this lab is entirely my own work.

from graphics import *
from time import *

def main():

    ## Creates window and background
    width = 800
    height = 800
    win = GraphWin("Shooting Stars",width,height)
    win.setBackground("green")

    message = Text(Point(width/2, height-10), "")
    message.draw(win)

    ## Creates blue sky (rectangle called sky)
    sky = Rectangle(Point(0,0), Point(800,600))
    sky.draw(win)
    sky.setFill("blue")

    ## Creates white house (rectangle called house)
    house = Rectangle(Point(300,400), Point(500,600))
    house.draw(win)
    house.setFill("white")

    ## Creates brown roof (polygon called roof)

    roof = Polygon(Point(300,400), Point(400,300), Point(500,400))
    roof.draw(win)
    roof.setFill("brown")

    ## Creates red door (rectangle called door)

    door = Rectangle(Point(380,550), Point(420,600))
    door.draw(win)
    door.setFill("red")

    ## Creates black window (rectangle called window1)

    window1 = Rectangle(Point(340,440), Point(360,460))
    window1.draw(win)
    window1.setFill("black")

    ## Creates clone of window1 and shifts 100 pixels to the right (window2)

    window2 = window1.clone()
    window2.move(100,0)
    window2.draw(win)

    sleep(2)  ## Short pause

    ## Creates star and clones (star1, star2, star3, star4, star5)

    star1 = Polygon(Point(10,0), Point(12.5,7.5), Point(20,10), Point(12.5,12.5), Point(10,20), Point(7.5,12.5), Point(0,10), Point(7.5,7.5))
    star1.draw(win)
    star1.setFill("yellow")

    star2 = star1.clone()
    star3 = star1.clone()
    star4 = star1.clone()
    star5 = star1.clone()

    ## Animates first star
        
    for i in range(25):
        star1.move(20,3)
        sleep(0.05)

    star1.undraw()  ## Removes star

    sleep(1)  ## Short pause

    ## Draws next star clone and animates

    star2.move(50,0)
    star2.draw(win)

    for i in range(25):
        star2.move(20,6)
        sleep(0.03)

    star2.undraw()  ## Removes star

    sleep(1)  ## Short pause

    ## Draws next star clone and animates

    star3.move(100,0)
    star3.draw(win)

    for i in range(25):
        star3.move(20,3)
        sleep(0.05)

    star3.undraw()  ## Removes star

    sleep(1)  ## Short pause

    ## Draws next star clone and animates

    star4.move(150,0)
    star4.draw(win)

    for i in range(25):
        star4.move(20,9)
        sleep(0.02)

    star4.undraw()  ## Removes star

    sleep(1)  ## Short pause

    ## Draws next star clone and animates

    star5.move(200,0)
    star5.draw(win)

    for i in range(25):
        star5.move(20,3)
        sleep(0.05)

    star5.undraw()  ## Removes star

    ## Prints greeting

    message.setSize(28)
    message.setFace("arial")
    message.setTextColor("white")
    message.setText("HAPPY SPRING!")

    sleep(3)  ## Short pause
    
    ## Closing instructions

    message.setSize(12)
    message.setFace("times roman")
    message.setTextColor("black")
    message.setText("Click to Quit")
    win.getMouse()
    win.close()

main()
