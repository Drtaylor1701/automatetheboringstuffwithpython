#! python3

while True:
    print('Enter your age')
    age = input()
    try:
        age = int(age)
    except:
        print('Please use numeric digits')
        continue
    if age < 1:
        print('Please enter a positive number.')
        continue
    break

print('Your age is ' + age + '.')