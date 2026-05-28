def read_input():
    t = int(input().strip())
    cases = []
    for _ in range(t):
        cases.append(int(input().strip()))
    return cases


def write_sequence(n: int, sequence: list):
    digits_added = 0
    for i in range(1, n+1):
        if len(str(i)) > 1:
            for j in str(i):
                digits_added += 1
                sequence.append(int(j))
        else:
            digits_added += 1
            sequence.append(i)
    
    sequence[0] = sequence[0] + digits_added
    return sequence

def find_number(n:int, idx: int, sequence: list):
    while True:
        if idx <= sequence[0]:
            return sequence[idx], n
        sequence = write_sequence(n, sequence)
        n += 1

def main():
    sequence = []
    n = 1
    sequence.append(0)
    cases = read_input()
    for case in cases:
        res, n = find_number(n, case, sequence)
        print(res)


if __name__ == "__main__":
    main()