#! python3

import pyinputplus as pyip

#specify that the number must be at least 4
response = pyip.inputNum('Enter num: ', min=4)

#specify that the number must be greater than 4
response = pyip.inputNum('Enter num: ', greaterThan=4)

#specify that the number must be less than six but a minimum of 4
response = pyip.inputNum('>', min=4, lessThan=6)