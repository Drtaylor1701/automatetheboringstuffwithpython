#!/usr/bin/env python3

'''built-in functions examples'''

#standard library
import random
import sys # system modules
import math # math modules
from random import * #imports all modules from a module
import pyperclip # third-party module

random.randint(1, 10)

#now you don't have to type random.randint()
randint(1, 10)

print('Hello')
sys.exit()
print('Goodbye')

#third party modules installed w/ pip, pyperclip, for example
pyperclip.copy('Hello world')
pyperclip.paste()