import random

x = random.randint(-20, 100)
y = random.randint(-20, 100)
z = random.randint(-20, 100)

print(x, y, z)

if x % 2 == 1 and y % 2 == 1 and z % 2 == 1:                  # When all are odd
    if x > y and x > z:
        print('{} is the largest odd number.'.format(x))
    elif y > z:
        print('{} is the largest odd number.'.format(y))
    else:
        print('{} is the largest odd number.'.format(z))
elif x % 2 == 0 and y % 2 == 1 and z % 2 == 1:                # When y and z are odd
    if y > z:
        print('{} is the largest odd number.'.format(y))
    elif z > y:
        print('{} is the largest odd number.'.format(z))
elif x % 2 == 1 and y % 2 == 1 and z % 2 == 0:                # When x and y are odd
    if x > y:
        print('{} is the largest odd number.'.format(x))
    elif y > x:
        print('{} is the largest odd number.'.format(y))
elif x % 2 == 1 and y % 2 == 0 and z % 2 == 1:                # When x and z are odd
    if x > z:
        print('{} is the largest odd number.'.format(x))
    elif z > x:
        print('{} is the largest odd number.'.format(z))
elif x % 2 == 1 and y % 2 == 0 and z % 2 == 0:                # When only x is odd
    print('{} is the only odd number.'.format(x))
elif x % 2 == 0 and y % 2 == 1 and z % 2 == 0:                # When only y is odd
    print('{} is the only odd number.'.format(y))
elif x % 2 == 0 and y % 2 == 0 and z % 2 == 1:                # When only z is odd
    print('{} is the only odd number.'.format(z))
else:
    print('None are odd numbers.')
