import math


def read_input():
    cases = []
    n = int(input())

    for i in range(n):
        case = []
        blank = input()
        m = int(input())
        for j in range(m):
            line = list(map(int, input().split()))
            case.append(line)
        cases.append(case)
    
    return cases


def sum_by_digits(case):
    d = len(case)
    res = 0
    for i in range(d):
        res += ((case[i][0] + case[i][1]) * (10 ** (d - i - 1)))
    return res


for i in read_input():
    print(f"{sum_by_digits(i)}\n")