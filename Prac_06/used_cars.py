"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from Prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))

# class Limo:
#
#     def __init__(self, fuel=100):
#         self.fuel = fuel
#         self.odometer = 0
#
#     def add_fuel(self, amount=20):
#         self.fuel += amount
#
#     def drive(self, distance=115):
#         if distance > self.fuel:
#             distance = self.fuel
#             self.fuel = 0
#         else:
#             self.fuel -= distance
#         self.odometer += distance
#         return distance



main()