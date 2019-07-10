import bisect


def grade(score, breakpoints, grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]


list01 = [grade(score, [60, 70, 80, 90]) for score in [33, 99, 77, 70, 89, 90, 100]]

print(list01)
