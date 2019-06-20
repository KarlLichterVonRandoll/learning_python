import time

while True:
    for i in range(100):
        print("|" * (100 - i), end="")
        print("\\" * i)
        time.sleep(0.08)
    for i in range(100):
        print("|" * i, end="")
        print("\\" * (100 - i))
        time.sleep(0.08)
