# Christopher Moore
# SalesPerson.py
#
# Problem: This program creates a class SalesPerson.
#
# Certification of Authenticity:
#
# I certify that this program is my own work, but I discussed it with
# Professor Stalvey.

class SalesPerson:

    def __init__(self, idNum, name):
        self.idNum = idNum
        self.name = name
        self.sales = []

    def getIDNum(self):
        return self.idNum

    def getName(self):
        return self.name

    def enterSale(self, aSale):
        self.sales.append(aSale)

    def totalSales(self):
        sumSales = 0
        for i in range(len(self.sales)):
            sumSales += self.sales[i]
        sumSales = round(sumSales, 2)
        return sumSales

    def getSales(self):
        return self.sales

    def metQuota(self, quota):
        quotaSum = self.totalSales()
        if quotaSum >= quota:
            return True
        else:
            return False

    def compareTo(self, otherPerson):
        selfQuotaSum = self.totalSales()
        otherQuotaSum = otherPerson.totalSales()
        if selfQuotaSum < otherQuotaSum:
            rtnVal = -1
        elif selfQuotaSum == otherQuotaSum:
            rtnVal = 0
        else:
            rtnVal = 1
        return rtnVal

    def __str__(self):
        rtnStr = "\nID Number: " + str(self.idNum) 
        rtnStr += "\nName: " + self.name
        rtnStr += "\nTotal Sales: " + str(self.totalSales())
        return rtnStr
