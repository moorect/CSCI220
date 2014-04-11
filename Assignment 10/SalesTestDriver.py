# SalesTestDriver.py
# Author: Pharr

# SalesTestDriver - creates a SalesForce object and uses it
# to determine aspects of the sales force.

from SalesForce import SalesForce
from SalesPerson import SalesPerson


def main():
    
    theSalesForce = SalesForce()
    theSalesForce.addData("salesdata.txt")
    
    print ("Quota report:")
    theSalesForce.quotaReport(750)
    print ("\n************************\n")

    topSales = theSalesForce.topSalesPerson()
    print ("Top sales person:")
    print (topSales)
    print ("\n************************\n")
    
    theSalesForce.individualSales(123)
    print ()
    theSalesForce.individualSales(999)
    print ()
    theSalesForce.individualSales(456)
    print ()
    theSalesForce.individualSales(345)

main()
