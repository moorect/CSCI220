# Name: Christopher Moore
# triangle.py
#
# Problem: This program uses functions to calculate the Euclidean distance between three
#          user-input points of a triangle as well as the triangle's area and perimeter.
#
# Certification of Authenticity:
#
# I certify that this lab is my own work, but I discussed it with: Professor Stalvey.


from graphics import *
from math import *

def makeTriangle(p1, p2, p3):

    triangle = Polygon(p1, p2, p3)
    triangle.setFill("blue")
    triangle.setOutline("red")
    return triangle

def distance(p1, p2):
    # FORMULA : d = sqrt( (x1-x2)^2 + (y1-y2)^2 )
    distance = sqrt(( (p1.getX() - p2.getX()) ** 2 + (p1.getY() - p2.getY()) ** 2 ))
    return distance

def perimeter(tri):
    # FORMULA : p = a + b + c
    points = tri.getPoints()
    side1 = distance(points[0], points[1])
    side2 = distance(points[1], points[2])
    side3 = distance(points[0], points[2])
    totalP = side1 + side2 + side3
    return totalP
    
def area(tri):
    # FORMULA : p = 1/2 perimeter
    # FORMULA : a = sqrt( p (p-a)(p-b)(p-c) )
    points = tri.getPoints()
    side1 = distance(points[0], points[1])
    side2 = distance(points[1], points[2])
    side3 = distance(points[0], points[2])
    totalP = side1 + side2 + side3
    p = totalP / 2
    totalA = sqrt( p * (p - side1) * (p - side2) * (p - side3) )
    return totalA

def main():
    
    width = 400
    height = 400
    win = GraphWin("Draw a Triangle", width, height)
    message = Text(Point(width/2, height-10), "Click on three points")
    message.draw(win)

    # Get and draw three vertices of triangle

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    triangle = makeTriangle(p1, p2, p3)

    triangle.draw(win)

    perim = perimeter(triangle)
    
    perim = round(perim, 2)
    messageP = Text(Point(width/3, height-25), "Perimeter: " + str(perim))
    messageP.draw(win)

    ar = area(triangle)
    
    ar = round(ar, 2)
    messageA = Text(Point(width*2/3, height-25), "Area: " + str(ar))
    messageA.draw(win)

    # Wait for another click to exit

    message.setText("Click anywhere to quit.")
    win.getMouse()
    win.close()

main()
