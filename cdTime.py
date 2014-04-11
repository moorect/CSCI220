# Name: Christopher Moore
# cdTime.py
#
# Problem: This program totals track times for individual CDs and total track time for multiple CDs.
#
# Certification of Authenticity:
#
# I certify that this lab is my own work, but I discussed it with: Professor Stalvey.


def main():
    finalSeconds = 0
    numCd = eval(input("How many CDs are to be processed?: "))

    for c in range(numCd):

        numTracks = eval(input("\nEnter the number of tracks on CD: "))
        cdSeconds = 0

        for i in range(numTracks):
        
            tempMin = eval(input("\nEnter the number of minutes on the track: "))
            tempSec = eval(input("Enter the number of seconds on the track: "))

            cdSeconds = cdSeconds + tempSec + (tempMin * 60)

        finalSeconds = finalSeconds + cdSeconds
        discMinutes = cdSeconds // 60
        discSeconds = cdSeconds % 60

        print("\n\nCD#", ( c + 1 ), "Total Time: ", discMinutes, "minute(s)", discSeconds, "second(s)\n")

    minutes = finalSeconds // 60
    outputSeconds = finalSeconds % 60
    outputHours = minutes // 60
    outputMinutes = minutes % 60

    print("\nTotal time of all CDs:", outputHours, "hour(s)", outputMinutes, "minute(s)", outputSeconds, "second(s)")

main()
