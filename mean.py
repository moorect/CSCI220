# Name: Christopher Moore
# mean.py
#
# Problem: This program gets a series of numbers from the user and calculates and displays the RMS Average and the Harmonic Mean.
#
# Inputs: Number of values to be entered (numValues), actual values to be entered (value).
# Outputs: Calculated RMS Average (rmsAvg), calculated Harmonic Mean (harmMean).
#
# Algorithm:
# 1. Collect number of values from user
# 2. Collect actual values in a definite loop from user
# 3. Calculate RMS Average and Harmonic Mean
# 4. Display RMS Average and Harmonic Mean
#
# Certification of Authenticity:
#
# I certify that this lab is entirely my own work.

import math

def main():
    print("This program will calculate and display the RMS Average and Harmonic Mean for the values you input.\n")
    numValues = eval(input("How many values to be entered?: "))

    squaredSum = 0
    ratioSum = 0

    for i in range(0, numValues):
        value = eval(input("\nInput value: "))
        squaredSum = squaredSum + (value ** 2)
        ratioSum = ratioSum + (1 / value)
    
    rmsAvg = math.sqrt(squaredSum / numValues)
    harmMean = numValues / ratioSum

    print("\nRMS AVERAGE = ", rmsAvg)
    print("HARMONIC MEAN = ", harmMean)
