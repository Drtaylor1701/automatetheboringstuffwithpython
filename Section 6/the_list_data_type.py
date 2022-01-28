#!/usr/bin/env python3
'''
A list is a data type that contains multiple values in a sequence.
'''

spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[0]) #returns cat
print(spam[1])
print(spam[2])
print(spam[3])

print("hello " + spam[0])

print("The " + spam[1] + " ate the " + spam[0] + ".")

'''You'll get an index error if you use an index that isn't in the list:'''

#print(spam[10000])

'''You'll get a typeerror if you try to use an index that isn't an integer'''
#print(spam[1.0])

'''Lists can contain other lists'''
spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
print(spam[0][1], spam[1][4])

'''negative indexes start at the right and work toward the left'''
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[-1], spam[-3])
print('The ' + spam[-1] + ' is afraid of the ' + spam[-3] + '.')

'''you can slice a list to get a sublist'''
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[0:4], spam[1:3], spam[0:-1], spam[:2], spam[1:], spam[:])

'''get list length with len()'''
print(len(spam))

'''changing values with indexes'''
spam = ['cat', 'bat', 'rat', 'elephant']
spam[1] = 'aardvark'
print(spam)
spam[2] = spam[1]
print(spam)
spam[-1] = 12345
print(spam)

'''concatenate and replicate lists'''
l = [1, 2, 3] + ['A', 'B', 'C']
print(l)
l = ['X', 'Y', 'Z'] * 3
print(l)
spam = [1, 2, 3]
print(spam)
spam = spam + ['A', 'B', 'C']
print(spam)

'''removing values from lists with del'''
spam = ['cat', 'bat', 'rat', 'elephant']
del spam[2]
print(spam)
