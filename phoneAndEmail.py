#! python3
# phoneAndEmail.py - finds phone numbers and email addresses on the clipboard
import pyperclip, re

#creates two regexes
#one regex matches phone numbers
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)

#one regex matches email addresses
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+   #username
    @                   #@ symbol
    [a-zA-Z0-9.-]+   #domain
    (\.[a-zAZ{2,4}])    #dot-something
    )''',re.VERBOSE)

#find all matches to both regexes
text = str(pyperclip.paste())

matches = []                                                #stores the matches
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])  #string that correctly formats the phone number
    if groups != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):                     #appends the first entry in groups to each match
    matches.append(groups[0])
    

#format the matched strings into a single string to paste and 
# copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    #display a message if no matches are found
    print('No phone nummbers or email addresses found.')
