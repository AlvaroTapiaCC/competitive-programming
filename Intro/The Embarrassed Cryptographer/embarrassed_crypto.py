import math


def read_input():
    cases = []
    while True:
        line = list(map(int, input().split()))

        if line[0] == 0 and line[1] == 0:
            break

        cases.append(line)
    return cases


def primes():
    i = 3
    prime_list = [2]
    yield 2
    while True:
        sqi = math.sqrt(i)
        is_prime = True
        for p in prime_list:
            if p > sqi:
                break
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(i)
            yield(i)
        i += 2    


def factorize(N):
    sqN = math.sqrt(N)
    for p in primes():
        if p > sqN:
            yield N
            break
        while N % p == 0:
            yield p
            N //= p
            sqN = math.sqrt(N)
        if N == 1:
            break


def analyze_key(case):
    factors = list(factorize(case[0]))
    if factors[0] < case[1]:
        return f"BAD {factors[0]}"
    elif factors[1] < case[1]:
        return f"BAD {factors[1]}"
    else:
        return "GOOD"
    
for i in read_input():
    print(analyze_key(i))