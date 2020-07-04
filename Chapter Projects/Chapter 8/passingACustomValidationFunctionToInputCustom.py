#! python3

#example: enter a series of digits that adds up to 10

#you can create your own function
#accepts a string argument of what the user entered
#raises an exception if it fails string validation
#returns None if inputCustom() should return the string unchanged
#returns None if inputCustom() should return a string that is other than what the user entered
#is passed as the first argument to inputCustom()
import pyinputplus as pyip

def addsUpToTen(numbers):
    numbersList = list(numbers)
    for i, digit in enumerate(numbersList):
        numbersList[i] = int(digit)
    if sum(numbersList) != 10:
        raise Exception("The digits must add up to 10, not %s." %(sum(numbersList)))
        return int(numbers) #returns an int form of numbers

addsUpToTen(123)