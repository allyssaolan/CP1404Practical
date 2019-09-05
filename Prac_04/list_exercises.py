numbers = []
for number in range(5):
    get_number = int(input("Enter a number: "))
    numbers.append(get_number)
print("The first number is: {}".format(numbers[0]))
print("The last number is: {}".format(numbers[4]))
numbers.sort()
print("The smallest number is: {}".format(min(numbers)))
print("The largest number is: {}".format(max(numbers)))

total = sum(numbers)
average = total / 5
print("The average of the numbers is: {}".format(average))

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Enter a name: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")
