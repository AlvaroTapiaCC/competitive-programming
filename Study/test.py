from bisect import bisect_right

def grade(score):
    breakpoints = [60, 70, 80, 90]
    grades = 'FDCBA'
    i = bisect_right(breakpoints, score)
    print(i)
    return grades[i]


print(grade(95))