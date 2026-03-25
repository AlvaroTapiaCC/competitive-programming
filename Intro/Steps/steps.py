def read_input():
    tests = []
    num_tests = int(input())

    for test in range(num_tests):
        tests.append(list(map(int, input().split())))

    return tests

def helper(n):
    return int(n*(n+1)/2)

def solve_steps(test):
    distance_left = test[1] - test[0]
    steps = 0
    step_size = 1
    
    while distance_left > 0:
        distance_left -= step_size
        if distance_left >= helper(step_size+1):
            step_size += 1
        elif distance_left < helper(step_size):
            step_size -= 1
        steps +=1
    
    return steps



for i in read_input():
    print(solve_steps(i))
