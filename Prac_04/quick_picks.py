import random

NUMBERS_PER_LINE = 6
MIN = 1
MAX = 45

quick_picks = int(input("How many quick picks? "))
for i in range(quick_picks):
    quick_pick_list = []
    for j in range(NUMBERS_PER_LINE):
        number = random.randint(MIN, MAX)
        while number in quick_pick_list:
            number = random.randint(MIN, MAX)
        quick_pick_list.append(number)
    quick_pick_list.sort()
    print(" ".join("{:2}".format(number) for number in quick_pick_list))
