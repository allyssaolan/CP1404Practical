# name = "name.txt"
#
# user_name = open(name, 'w')
# ask_name = input("What is your name? ")
# print("Your name is {}".format(ask_name), file=user_name)
# user_name.close()


# numbers = open("numbers.txt", 'r')
# int_one = int(numbers.readline())
# int_two = int(numbers.readline())
# print("The total of the two integers given is", int_one + int_two)
# numbers.close()

# user_name = open("name.txt", 'r')
# name = user_name.read().strip()
# print("Your name is {}".format(name))
# user_name.close()

numbers = open("numbers.txt", 'r')
total = 0
for line in numbers:
    count = int(line)
    total += count
print(total)
numbers.close()


# TODO: part b and d