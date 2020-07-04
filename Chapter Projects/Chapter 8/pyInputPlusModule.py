#! python3


#PyInputPlus contains input functions for different types of data
#Will prompt users to enter data in correct formats
#Will reprompt if the data is not valid

#install pyinputplus module
import pyinputplus as piyp

#inputStr()
#like input() but has general PyInputPlus features, or you can give it a custom validation function


#inputNum()
#ensures that the user enters a number and returns int or float depending on what the number is

#inputChoice()
#Ensures the user enters one of the provided choices

#inputMenu()
#Similar to inputChoice() but provides a menu of options

#inputDatetime()
#Ensures the user enters date and time

#inputYesNo()
#Ensures the user enters "yes" or "no"

#inputBool()
#Ensures the user enters True or Fales

#inputEmail()
#Ensures the user enters an email address

#inputFilepath()
#Ensures the user enters a valid file apth and filename and can check that the file exists

#inputPassword()
#like input() but displays * characters as the user types

response = piyp.inputNum()

response2 = input('Enter a number.')
