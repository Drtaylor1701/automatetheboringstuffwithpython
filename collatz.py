#/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

#collatz function
def collatz(number):
    number = int(number)
    #if the number is even
    if number % 2 == 0:
        #divide number by 2
        number = number // 2
    #if number is odd
    elif number % 2 != 0:
        #multiply number by 3 and add 1
        number = number * 3 + 1
    return number

i = input("Please enter an integer: ")

try:
    while i != 1:
        i = collatz(i)
        print(i)
except ValueError:
    print('You should enter an integer.')
