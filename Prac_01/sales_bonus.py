sales = float(input("Enter sales: $"))

while sales >= 0:
    if sales < 1000:
        bonus = sales * 0.10
        print("Your bonus is $", bonus)
    else:
        bonus = sales * 0.15
    print("Your bonus is $", bonus)
    sales = float(input("Enter sales: $"))