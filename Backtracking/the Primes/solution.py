def read_input():
    digit_sum = int(input().strip())
    digit_ini = int(input().strip())
    return digit_sum, digit_ini

def is_valid_state(state, primes):
    if len(state) != 5:
        return False
    
    diag2 = state[0][4] + state[1][3] + state[2][2] + state[3][1] + state[4][0]
    if diag2 not in primes:
        return False
    return True

def check_partials(partials: list[str], candidates: set[str], prefixes_by_len: dict[int, set[str]]):
    next_len = len(partials[0]) + 1
    valid_prefixes = prefixes_by_len[next_len] 

    filtered = set()
    for cand in candidates:
        ok = True
        for i, partial in enumerate(partials):
            if partial + cand[i] not in valid_prefixes:
                ok = False
                break
        if ok:
            filtered.add(cand)

    return filtered
            

def get_candidates(state: list[str], digit_ini: int, primes: set[str], prefixes: dict[int, set[str]]):
    if not state:
        return {p for p in primes if int(p[0]) == digit_ini}
    
    r = len(state)
    partials = []
    for c in range(5):
        partials.append("".join(state[i][c] for i in range(r)))

    diag1_part = "".join(state[i][i] for i in range(r))

    candidates = set(primes)
    candidates = check_partials(partials, candidates, prefixes)

    next_len = r + 1
    valid_prefixes = prefixes[next_len]
    candidates = {cand for cand in candidates if (diag1_part + cand[r]) in valid_prefixes}

    return candidates


def search(state: list, solutions: list, digit_ini: int, primes: set[str], prefixes: dict[int, set[str]]):
    if len(state) == 5:
        if is_valid_state(state, primes):
            solutions.append(state.copy())
        return

    for candidate in get_candidates(state, digit_ini, primes, prefixes):
        state.append(candidate)
        search(state, solutions, digit_ini, primes, prefixes)
        state.pop()

def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, round(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
def digit_sum(n):
    total = 0
    for d in str(n):
        total += int(d)
    return total

def find_primes(target_sum):
    primes = []
    for n in range(10000, 100000):
        if is_prime(n) and digit_sum(n) == target_sum:
            primes.append(str(n))
    return primes

def build_prefixes(primes: set[str]):
    prefixes = {}
    for i in range(1, 6):
        prefix = set()
        for prime in primes:
            prefix.add(prime[:(i)])
        prefixes[i] = prefix
    return prefixes

def main():
    digit_sum, digit_ini = read_input()
    primes = set(find_primes(digit_sum))
    prefixes = build_prefixes(primes)
    solutions = []
    state = []

    search(state, solutions, digit_ini, primes, prefixes)
    for solution in sorted(solutions):
        for num in solution:
            print(num)
        print("")

if __name__ == "__main__":
    main()