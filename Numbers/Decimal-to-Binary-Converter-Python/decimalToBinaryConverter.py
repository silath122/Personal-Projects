
# Decimal to Binary Converter
# About: Asks the user for a decimal that can either be positive or negative. Once the user inputs a decimal,
# the number is then converted into it's binary sequence. The range of numbers the user can select are between
# -512 and 511(inclusive). This is due to the fact that the binary sequence can only be 10 bits long.
#
# This project is still a WIP!!
#
# Author: Siah Thomas
# Date: 01/13/2023

def binaryConverter(n, maxBin, numString):
    if n > 0:
        if n == 0 and maxBin == 0:
            return numString
        elif n - maxBin < 0:
            numString = numString + "0"
            binaryConverter(n, maxBin/2, numString)
        elif n - maxBin > 0:
            numString = numString + "1"
            binaryConverter(n - maxBin, maxBin/2, numString)
    return numString


def main():
    print("Binary to Decimal Converter\n")
    userInput = eval(input("Please enter a number you would like to convert to binary that ranges from 0 to 511: "))

    if userInput == 0:
        binNum = "0000000000"
    elif 0 < userInput <= 511:
        binNum = binaryConverter(userInput, 312, "")
    else:
        binNum = "Error! Invalid value!"

    print("The binary sequence of decimal " + str(userInput) + " is: " + binNum)





main()