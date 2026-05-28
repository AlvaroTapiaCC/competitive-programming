import math
from sys import stdin

E = 1e-6

def read_input():
    cases = []
    for line in stdin:
        if not line.strip():
            break
        cases.append(list(map(int, line.strip().split())))
    return cases

def equation(x, values):
    p, q, r, s, t, u = values
    return (p * (math.e ** -x) + (q * math.sin(x)) + (r * math.cos(x)) + (s * math.tan(x)) + (t * x**2) + u)

def bisect_solve(values):
    low = 0
    high = 1
    while high - low > E:
        mid = low + ((high - low) / 2)
        f_mid = equation(mid, values)
        if f_mid >= 0:
            low = mid
        else:
            high = mid
    return f"{mid:.4f}"



def main():
    values_list = read_input()
    for values in values_list:
        result = bisect_solve(values)
        if float(result) == 1:
            print("No solution")
        else:
            print(result)


if __name__ == "__main__":
    main()