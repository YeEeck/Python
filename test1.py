import random

t = 1
random.seed()
for i in range(100000):
    r = random.randint(0, 1)
    if r == 1:
        t = t * 1.1
    else:
        t = t * 0.9

print(t)
