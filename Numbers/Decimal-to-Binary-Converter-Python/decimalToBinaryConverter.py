
# Decimal to Binary Converter
# About: Asks the user for a decimal that can either be positive or negative. Once the user inputs a decimal,
# the number is then converted into it's binary sequence. The range of numbers the user can select are between
# -512 and 511(inclusive). This is due to the fact that the binary sequence can only be 10 bits long.
#
# Author: Siah Thomas
# Date: 01/13/2023


def main():
    print("Binary to Decimal Converter\n")
    print("Please enter a number you would like to convert to binary that ranges from -512 to 511: ")
    userInput = eval(input())
