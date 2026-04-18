from sys import stdin

# Every 2 lines:
# First line -> n = initial vessels, m = containers to fill
# Second line -> capacity of each of the n initial vessels

def read_input():
    cases = []
    case = []
    n = 0
    for line in stdin:
        if not line.strip():
            break
        if n == 0:
            case.append(list(map(int, line.strip().split())))
            n = 1
        elif n == 1:
            case.append(list(map(int, line.strip().split())))
            cases.append(case)
            case = []
            n = 0
    return cases

def compute_containers(case: list):
    n, m = case[0]
    vessels = case[1]

    if m == 1:
        return sum(vessels)
    if n < m:
        return max(vessels)

    k = m - 1
    containers = [0] * m
    cuts = list(range(1, k + 1))

    while True:
        split_vessels = []
        start = 0
        for c in cuts + [n]:
            split_vessels.append(sum(vessels[start:c]))
            start = c
        if max(containers) == 0 or max(containers) > max(split_vessels):
            containers = split_vessels

        i = k - 1
        while i >= 0 and cuts[i] == (n - k + i):
            i -= 1

        if i < 0:
            break

        cuts[i] += 1
        j = i + 1
        while j < k:
            cuts[j] = cuts[j - 1] + 1
            j += 1
            
    return max(containers)


def main():
    cases = read_input()
    for case in cases:
        print(compute_containers(case))

if __name__ == "__main__":
    main()
