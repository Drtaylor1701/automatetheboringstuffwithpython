#this program says hello and asks for my name

#print() displays the string value inside its parentheses on the screen
print("Hello, world!")
print("What is your name?") #ask for their name

#input() waits for the user to type some text ont he keyboard and press Enter
myName = input()

print("It is good to meet you" + myName)
print("The length of your name is:" )

#evaluates to the integer value of the number of characters in the string
print(len(myName))
print("What is your age?") #ask for their age
myAge = input()
print("you will be " + str(int(myAge) + 1 + ' in a year')
