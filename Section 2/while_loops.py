#!/usr/bin/python python3

'''while loop example'''
SPAM = 0
while SPAM < 5:
    print("Hello world!")
    SPAM = SPAM + 1

NAME = ''
while NAME != 'your name':
    print('Please type your name.')
    NAME = input()
print("Thank you!")

'''same as above but with break statement'''
FIRSTNAME = ''
while True:
    print('Please type your name.')
    if FIRSTNAME == 'your name':
        break
print("Thank you!")

SPAM = 0
while SPAM < 5:
    SPAM = SPAM + 1
    if SPAM == 3:
        continue
    print('spam is ' + str(SPAM))
