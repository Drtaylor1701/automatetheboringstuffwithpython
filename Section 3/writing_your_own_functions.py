#!/usr/bin/env python3

'''writing your own functions examples'''

def hello():
    '''example of writing a function'''
    print('Howdy')
    print('Howdy!!!')
    print('Hello there')

hello()
hello()
hello()

def howdy(name):
    '''example of writing a function with an argument/parameter'''
    print('Hello ' + name)

howdy('Alice')
howdy('Bob')


def plus_one(number):
    '''using a return statement'''
    return number + 1

NEWNUMBER = plus_one(5)
print(NEWNUMBER)

'''prints hello world on one line'''
print('hello', end='')
print(' world')

#changes separation between words
print('cat', 'dog', 'mouse', sep='ABC')