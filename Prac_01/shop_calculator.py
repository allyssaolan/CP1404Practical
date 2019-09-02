number_of_items = int(input("Number of items: "))
total = 0

for i in range(number_of_items):
    price_of_item = int(input("Price of item: "))
    total += price_of_item
print("Total price for {} items is $ {}".format(number_of_items, total))
if total > 100:
    discount = total * 0.10
    discounted_price = total - discount
print("Total discounted price is $", discounted_price)
