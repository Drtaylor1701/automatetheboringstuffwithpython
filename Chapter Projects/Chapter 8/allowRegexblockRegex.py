#! Python3

#use regular expressions to specify if input is allowed or not

#allowRegexes and blockRegexes take a list or regular expression strings

import pyinputplus as pyip

#now inputNum() will accept roman numerals in addition to the usual numbers
response = pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+',r'zero'])

#inputNum will not accept even numbers
response = pyip.inputNum(blockRegexes[r'[02468]$'])

#if you specify both an allowRegexes and blockRegexes argument, the allow list overrides the block list
response = pyip.inputStr(allowRegexes=[r'caterpillar','category']
                        blockRegexes=[r'cat'])

#will block cat and catastrophe but allow category and caterpillar