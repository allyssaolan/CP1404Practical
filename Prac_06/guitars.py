from Prac_06.guitar import Guitar


def main():
    print("My guitars!")

    guitars = []

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = int(input("Cost: $"))
        add_guitar = Guitar(name, year, cost)
        guitars.append(add_guitar)
        print("{} ({}) : ${:,.2f} added.".format(name, year, cost))
        name = input("Name:")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    # print(guitars)

    print("These are my guitars:")
    for i, guitar in enumerate(guitars):
        vintage_string = "(vintage)"
        if guitar.is_vintage():
            print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(i + 1, guitar.name, year, cost, vintage_string))
        else:
            print("Guitar {}: {:>20} ({}), worth ${:10,.2f} is not vintage".format(i + 1, guitar.name, year, cost))


main()
