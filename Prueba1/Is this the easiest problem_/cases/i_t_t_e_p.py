import math

EPS = 1E-8

def read_input():
    cases = []
    k = int(input())
    for i in range(k):
        line = list(map(int, input().split()))
        cases.append(line)
    return cases


def identify_triangle(i, case):

    if (case[0] == 0) or (case[1] == 0) or (case[2] == 0):
        return f"Case {i+1}: Invalid"

    a_calc = ((case[1]**2 + case[2]**2 - case[0]**2) / (2 * case[1] * case[2]))
    b_calc = ((case[0]**2 + case[2]**2 - case[1]**2) / (2 * case[0] * case[2]))
    c_calc = ((case[0]**2 + case[1]**2 - case[2]**2) / (2 * case[0] * case[1]))

    try:
        A = math.acos(a_calc)
        B = math.acos(b_calc)
        C = math.acos(c_calc)
    except:
        return f"Case {i+1}: Invalid"
    
    type = ""
    
    if A == B and B == C:
        type = "Equilateral"
    elif (A == B and C != A) or (A == C and B != C) or (B == C and A != B):
        type = "Isosceles" 
    else:
        type = "Scalene"


    return f"Case {i+1}: {type}"



for i, case in enumerate(read_input()):
    print(identify_triangle(i, case))


