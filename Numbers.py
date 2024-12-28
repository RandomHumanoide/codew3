x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))

a = 35e3
b = 12E4
c = -87.7e100

print(type(a))
print(a)
print(type(b))
print(b)
print(type(c))
print(c)

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)
#convert from float to int:
b = int(y)
#convert from int to complex:
c = complex(x)
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

import random

print(random.randrange(1, 100))