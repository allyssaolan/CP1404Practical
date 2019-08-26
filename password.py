min_length = 4

password = input("Enter valid password: ")
while len(password) < min_length:
    password = input("Invalid password. Please enter a valid password: " )
print((len(password) * '*'))