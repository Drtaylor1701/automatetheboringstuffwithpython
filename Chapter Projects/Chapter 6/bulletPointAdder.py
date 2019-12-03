#! /usr/bin/env python3

#gets text from the clipboard, adds a star and space to the beginning
#of each line, and then pastes it to the clipboard.

import pyperclip
text = pyperclip.paste()

#Separate lines and add stars
lines = text.split('\n')
for i in range(len(lines)):    #loop through all indexes in the 'lines' list
    lines[i] = '* ' + lines[i] # add star to each string in 'lines'
text = '\n'.join(lines)

pyperclip.copy(text)


