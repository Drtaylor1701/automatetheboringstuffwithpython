#! python3

import pyinputplus as pyip

#limits the number of times pyinputplus will ask for input
response = pyip.inputNum(limit=2)

#if the user fails to enter valid input, the function will rais a RetryLimitException or TimeoutException

#function returns the default vaule instead of raising an exception
response = pyip.inputNum(limit=2, default='N/A')
