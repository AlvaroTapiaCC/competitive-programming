import math

def read_input():
    cases = []
    while True:
        line = list(map(int, input().split()))
        if line == [0,0,0]:
            break
        cases.append(line)
    return cases

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * (b / gcd(a, b))


def solve_ecuation(case):
    
    
    
    
    return


for i in read_input():
    print(i)