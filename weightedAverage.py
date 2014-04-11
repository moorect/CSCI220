# Name: Christopher Moore
# weightedAverage.py
#
# Problem: This program inputs a file specified by user and calculates student weighted
#          grade averages and then the class average.
#
# Certification of Authenticity:
#
# I certify that this lab is my own work, but I discussed it with: Professor Stalvey.

def main():
    infileName = input("Enter the filename of grades to open (filename.ext): ")
    infile = open(infileName, "r")
    print()

    # avgTotal = 0
    studentCount = 0
    classTotal = 0

    for line in infile:
        # print("line - " + line)
        values = line.split()
        total = 0
        gradeCount = 0
                
        for i in range(2,len(values),2):
            total = total + (float(values[i])) * (float(values[i+1]))
            gradeCount += 1
            # print(total)
            
        average = total / 100
        studentCount += 1
        classTotal = classTotal + average
        classAvg = classTotal / studentCount
        # print(total)
        # classTotal += average
        # classAvg = classTotal / studentCount
        print(values[0] + " " + values[1] + "'s Average: {0:.1f}".format(average))
        
    # print("classTotal: ", classTotal)
    # print("studentCount= ", studentCount)
    print("\nClass Average: {0:.1f}".format(classAvg))
        
    infile.close()

main()
