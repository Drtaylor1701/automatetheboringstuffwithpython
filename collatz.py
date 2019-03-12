#/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

#collatz function
def collatz(number):
    #if the number is even
    if number % 2 == 0:
        #divide number by 2
        number = number // 2
    #if number is odd
    else:
        #multiply number by 3 and add 1
        number = number * 3 + 1
    return number

i = input("Please enter an integer: ")
print(collatz())
