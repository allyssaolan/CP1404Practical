from Prac_08.taxi import Taxi
from Prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    selected_taxi = None
    print("Let's drive!")
    print(MENU)
    menu_choice = input(">>> ").lower()
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available:")
            print(list_taxis(taxis))
            choose_taxi = int(input("Choose taxi: "))
            while choose_taxi > len(taxis) - 1:
                choose_taxi = int(input("Choose taxi: "))
            selected_taxi = taxis[choose_taxi]

        elif menu_choice == "d":
            if selected_taxi is not None:
                selected_taxi.start_fare()
                distance = int(input("Drive how far? "))
                selected_taxi.drive(distance)
                cost = selected_taxi.get_fare()
                print("Your {} trip cost you ${}".format(selected_taxi.name, cost))
                bill += cost
        else:
            print("Invalid option")
        print("Bill choose to date: ${}".format(bill))
        print(MENU)
        menu_choice = input(">>> ").lower()

    print("Total trip cost: ${}".format(bill))
    print("Taxis are now:")
    list_taxis(taxis)


def list_taxis(taxis):
    for num, taxi in enumerate(taxis):
        print("{} - {}".format(num, taxi))


main()
