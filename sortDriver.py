## sortDriver.py

from sort import *

def main():
    list1 = [18,12,1,24,6,30,8,3,15,22]
    print ("Unsorted list:")
    print (list1)

    selSort(list1)

    print ("\nSorted list:")
    print (list1)

    l2 = ["ban", "home", "apple", "cow", "doe", "zoo"]
    print ("Unsorted list:")
    print (l2)

    selSort(l2)

    print ("\nSorted list:")
    print (l2)

##    listOfLs = [l1, l2, range(0,1)]
##    print (listOfLs)
##    selSort(listOfLs)
##    print (listOfLs)

main()
