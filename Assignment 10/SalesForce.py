# Christopher Moore
# SalesForce.py
#
# Problem: This program creates a class SalesForce which is a list of SalesPersons.
#
# Certification of Authenticity:
#
# I certify that this program is my own work, but I discussed it with
# Professor Stalvey.


from SalesPerson import SalesPerson

class SalesForce:

    def __init__(self):
        self.salesTeam = []

    def addData(self, fileName):
        infile = open(fileName, "r")
        count = 0
        line = infile.readline()

        while line != "":
            salesPersonList = line.split()
            #print(salesPersonList)
            idNum = salesPersonList[0]
            name = salesPersonList[1] + " " + salesPersonList[2]
            man = SalesPerson(idNum, name)

            for i in range(3, len(salesPersonList)):
##                self.sales.append(salesPersonList[i])
                man.enterSale(float(salesPersonList[i])) ##
            self.salesTeam.append(man) ##
            count += 1
            line = infile.readline()
        if count == 0:
            print("The file contains no data.")

    def quotaReport(self, quota):
        for i in range(len(self.salesTeam)):
            print(self.salesTeam[i])
            metQuota = self.salesTeam[i].metQuota(quota)
            if metQuota == True:
                print("This sales person met the quota.")
            else:
                print("This sales person did not meet the quota.")
            
    def topSalesPerson(self):
        n = len(self.salesTeam)
        for front in range(n-1):
            minPos = front
            for i in range(front + 1, n):
                if self.salesTeam[i].totalSales() > self.salesTeam[minPos].totalSales():
                    highest = i
                    minPos = i
            return self.salesTeam[highest]

    def sortDecending(self):
        n = len(self.salesTeam)
        for front in range(n-1):
            minPos = front
            for i in range(front + 1, n):
                if self.salesTeam[i].totalSales() > self.salesTeam[minPos].totalSales():
                    minPos = i
            temp = self.salesTeam[minPos]
            self.salesTeam[minPos] = self.salesTeam[front]
            self.salesTeam[front] = temp
        print("\nDatabase is now sorted in decending order.")
        #for person in self.salesTeam:
        #    print(person)
        #print("***")
        #return self.salesTeam[0]
            
    def individualSales(self, id):
        found = False
        length = len(self.salesTeam)
        i = 0
        while found == False and i < length:
            if str(self.salesTeam[i].getIDNum()) == str(id):
                found = True
                print(self.salesTeam[i])
                print("Sales Record: " + str(self.salesTeam[i].getSales()))
            i += 1
        if found == False:
            print("ID# " + str(id) + ":   ** Invalid ID. **")

    def __str__(self):
        rtnStr = "  -- Sales Team --\n"
        if len(self.salesTeam) == 0:
            rtnStr += "No sales team members."
        else:
            for i in range(len(self.salesTeam)):
                rtnStr += str(self.salesTeam[i]) + "\n"
        return rtnStr
