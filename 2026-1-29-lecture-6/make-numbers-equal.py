import random

step = 1
x = random.randint(0,100)
y = random.randint(0,100)

# while x != y:
#     sign = int((y - x) / abs(y - x))
#     x += sign * step
#     print(x, y)

for index in range(abs(y-x)):
    sign = int((y - x) / abs(y - x))
    x += sign * step
    print(x,y)