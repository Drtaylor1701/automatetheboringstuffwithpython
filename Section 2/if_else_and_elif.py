'''examples of if/else/elif statements'''
NAME = 'Alice'
if NAME == 'Alice':
    print('Hi, Alice')

NAME = 'Bob'
if NAME == 'Alice':
    print('Hi, Alice')

PASSWORD = 'swordfish'
if PASSWORD == 'swordfish':
    print("Access granted")
else:
    print('Wrong password')

PASSWORD = 'rosebud'
if PASSWORD == 'swordfish':
    print("Access granted")
else:
    print('Wrong password')

'''examples w/ elif'''
NAME = 'Bob'
AGE = 3000
if NAME == 'Alice':
    print('Hi Alice')
elif AGE < 12:
    print('You are not Alice, kiddo')
elif AGE > 2000:
    print("Unlike you, Alice is not an undead, immortal vampire.")
elif AGE > 100:
    print('You are not Alice, grannie')

'''truthy and falsy values'''
print('Enter a name')
NAME = input()
if NAME:
    print('Thank you for entering a name')
else:
    print('You did not enter a name')
