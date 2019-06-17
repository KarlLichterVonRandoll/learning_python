"""
    百钱买百鸡
"""

for i in range(1, 21):
    for j in range(1, 34):
        k = 100 - i - j
        if 5 * i + 3 * i + 0.5 * k == 100:
            print(i, j, k)

