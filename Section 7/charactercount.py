#!/usr/bin/env python3
'''following along with the character count exercise'''

from itertools import count

MESSAGE = "It was a bright cold day in April, and the clocks were striking thirteen"

count = {}

for character in MESSAGE.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)
