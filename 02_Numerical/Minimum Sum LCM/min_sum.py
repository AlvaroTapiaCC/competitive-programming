def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

data = []

while True:
    line = input().strip()
    if line == '0':
        break
    data.append(int(line))

case = 1
for num in data:
    min_sum = num + 1
    best_pair = None

    for i in range(1, num + 1):
        if num % i == 0:
            j = num // i
            if lcm(i, j) == num:
                if i + j < min_sum:
                    min_sum = i + j
                    best_pair = (i, j)
    print(f"Case {case}: {min_sum}")
    case += 1