import os

f = os.open('text.txt', r)
print(f.readlines())