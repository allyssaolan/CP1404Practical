from Prac_08.unreliable_car import UnreliableCar


def main():
    car_one = UnreliableCar("Good", 100, 70)
    car_two = UnreliableCar("Bad", 100, 21)
    for i in range(1, 12):
        print("{:12} drove {:2}km".format(car_one.name, car_one.drive(i)))
        print("{:12} drove {:2}km".format(car_two.name, car_two.drive(i)))

    print(car_one)
    print(car_two)
