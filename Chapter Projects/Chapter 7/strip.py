#! python3
import sys

#check for arguments
def argsCheck():
    if len(sys.argv) >= 1:
        return True
    else:
        return False

#if no arguments, strip whitespace characters from beginning and end of string
def stripWhitespace():
    if argsCheck() == 0:
        #something regex find whitespace at the beginning and end and strip it
    else:
        #make the arguments into a list
        args = []
        for item in sys.argv:
            args.append(item)
        #find the list item in the string
            if item in args:
        #delete it
                line.replace(char,'')
