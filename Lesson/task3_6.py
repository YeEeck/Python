import time

for i in range(50):
    print("\rStarting " + "." * i, end="")
    time.sleep(0.3)

print(" Done!")
