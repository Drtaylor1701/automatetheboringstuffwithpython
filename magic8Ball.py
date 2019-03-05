#python imports the random module
import random

#defines getAnswer function
def getAnswer(answerNumber):
    #program execution selects a number based on the value of 4
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not good'
    elif answerNumber == 9:
        return 'Very doubtful'

#calls randint function from random module with two arguments
#r evaluates to a random integer between 1 and 9, including 1 and 9
#r = random.randint(1, 9)
#calls the getAnswer function with r as the argument
#returned string from getAnswer is assiged to the fortune variable.
#fortune = getAnswer(r)
#prints fortune variable
#print(fortune)

#shorten the part where you call the function and print it to one line
print(getAnswer(random.randint(1,9)))
