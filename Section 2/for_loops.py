#!/usr/bin/python python3

'''for loop examples'''
for i in range(5):
    print('Jimmy Five Times' + str(i))

#gauss problem
TOTAL = 0
for num in range(101):
    TOTAL = TOTAL + num
print(TOTAL)

#while equivalent of for loops
print('my name is')
I = 0
while I < 5:
    print('Jimmy Five Times' + str(I))
    I = I + 1

#goes up to and does not include second number
for i in range(12, 16):
    print('Jimmy Five Times' + str(i))

#increase by 2
for i in range(0, 10, 2):
    print('Jimmy Five Times' + str(i))
