import math


def read_input():
    numbers = []
    while True:
        try:
            line = input().strip()
            if line == "":
                break
            numbers.append(int(line))
        except EOFError:
            break
    return numbers


def find_exponent(N):
    log2 = math.log10(2)
    digits = len(str(N))
    
    E = 1
    while True:    
        x = E * log2
        frac = x - int(x)
        first_digits = int(10 ** (frac + digits - 1))

        if first_digits == N:
            total_digits = int(x) + 1

            if total_digits > 2 * digits:
                return E

        if E > 10**7:
            return "no power of 2"
        
        E += 1


for i in read_input():
    print(find_exponent(i))


