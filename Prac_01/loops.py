for i in range(1, 21, 2):
    print(i, end=' ')
print()

for x in range(0, 110, 10):
    print(x, end=' ')
print()

for y in range(20, 0, -1):
    print(y, end=' ')
print()

stars = int(input("\nEnter a number: "))
for i in range(stars):
    print('*', end='')
print()

for z in range(1, stars + 1):
    print('*' * z)
print()