#!/usr/bin/env python3
import random

print("Hello. What is your name?")
name = input()

print("Well, " + name + ", I am thinking of a number between 1 and 20. ")
print("Take a guess.")
secretNumber = random.randint(1, 20)

for guessesTaken in range(1, 7):
    print('Take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break

if guess == secretNumber:
    print('Good job ' + name + '! You guessed the number!')
else:
    print("Nope, you did not guess the number")