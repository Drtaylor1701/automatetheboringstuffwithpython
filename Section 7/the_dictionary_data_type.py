#!/usr/bin/env python3

'''dictionary is a collection of many values'''
mycat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}

#access values through their keys
print(mycat["size"])

print("my cat has " + mycat['color'] + " fur.")

#you can't get things by index because the order doesn't matter.
eggs = {'name': 'zophie', 'species': 'cat'}
spam = {'species': 'cat', 'name': 'zophie'}
print(eggs == spam) #returns True

#dictionary methods
print(list(eggs.keys()))
print(list(eggs.items()))

for k in eggs.keys():
    print(k)

for v in eggs.values():
    print(v)

for k, v in eggs.items():
    print(k, v)

for i in eggs.items():
    print(i)

print('cat' in eggs.values()) #returns True

if 'color' in eggs:
    print(eggs['color'])

print(eggs.get('age', 0))#returns the value of 'age', otherwise return 0
print(eggs.get('color', 0))

picnicItems = {'apples': 5, 'cups': 2}
print("I am bringing " + str(picnicItems.get('napkins', 0)) + ' napkins to the picnic')

#setDefault() lets you set a default value for a key

if 'color' not in eggs:
    eggs['color'] = 'black'

eggs.setdefault('color', 'black') #same idea as above