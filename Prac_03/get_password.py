MIN_LENGTH = 4


def main():
    password = enter_password(MIN_LENGTH)
    print_asterisks(password)


def get_password(MIN_LENGTH):
    password = input("Enter a valid password: ")
    while len(password) < MIN_LENGTH:
        password = input("Invalid password. Please enter a valid password (minimum of 4 characters): ")
    return password


def print_asterisks(num_of_asterisks):
    print(('*' * len(num_of_asterisks)))


main()
