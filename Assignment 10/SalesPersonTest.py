# Test for SalesPerson

from SalesPerson import SalesPerson

def main():

    man1 = SalesPerson(1, "Chris Moore")
    man2 = SalesPerson(2, "RoxAnn Stalvey")

    chrisTeam = []
    chrisTeam.append(man1)
    chrisTeam.append(man2)

##    salesTeam = [] (handled in constructor)
##    in addData():
##    loop through a file
##    for each line of the file
##       get the id number
##       get the name
##       build a person
##       get the list of sales
##       for each sale:
##            add that sale to the person
##       add person to the salesTeam
       
    

    print("Constructors, Getters:")
    print("man1 name =", man1.getName())
    print("man1 ID num =", man1.getIDNum())
    print("man1 sales =", man1.getSales())
    print("man2 name =", man2.getName())
    print("man2 ID num =", man2.getIDNum())
    print("man2 sales =", man2.getSales())

# Input Test

    man1.enterSale(54.99)
    man2.enterSale(7.99)
    man1.enterSale(2.99)
    man2.enterSale(44.99)

    

    print()
    print("\nSales added to list:")
    print("man1 name =", man1.getName())
    print("man1 ID num =", man1.getIDNum())
    print("man1 sales =", man1.getSales())
    print("man2 name =", man2.getName())
    print("man2 ID num =", man2.getIDNum())
    print("man2 sales =", man2.getSales())

# __str__ test

    print()
    print("__str__:")
    print(man1)
    print(man2)

# compareTo test

    print()
    print("Compare To:")
    print("man1 is less than man2:", man1.compareTo(man2) < 0)
    print("man1 equals man2:", man1.compareTo(man2) == 0)
    print("man1 is greater than man2:", man1.compareTo(man2) > 0)

# metQuota test

    print()
    print("Met Quota:")
    print("man1 vs quota of 20:", man1.metQuota(20))
    print("man1 vs quota of 100:", man1.metQuota(100))


main()
