def read_input():
    target_sum = int(input())
    initial_digit = int(input())
    return target_sum, initial_digit


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


def build_prefix_sets(primes):
    prefixes = {k: set() for k in range(1, 6)}
    for prime in primes:
        for k in range(1, 6):
            prefixes[k].add(prime[:k])
    return prefixes


def is_valid_extension(solution, candidate_row, row_idx, prefixes):
    prefix_len = row_idx + 1

    for col in range(5):
        col_prefix = "".join(solution[i][col] for i in range(row_idx)) + candidate_row[col]
        if col_prefix not in prefixes[prefix_len]:
            return False

    diag1_prefix = "".join(solution[i][i] for i in range(row_idx)) + candidate_row[row_idx]
    if diag1_prefix not in prefixes[prefix_len]:
        return False

    diag2_prefix = "".join(solution[i][4 - i] for i in range(row_idx)) + candidate_row[4 - row_idx]
    if diag2_prefix not in prefixes[prefix_len]:
        return False

    return True


def extend_solution(solution, primes, prefixes, initial_digit):
    row_idx = len(solution)

    for prime in primes:
        if row_idx == 0 and int(prime[0]) != initial_digit:
            continue

        if not is_valid_extension(solution, prime, row_idx, prefixes):
            continue

        yield solution + [prime]


def is_solution(solution):
    return len(solution) == 5


def process_solution(solution, solutions):
    solutions.append(solution[:])


def backtracking(solution, primes, prefixes, initial_digit, solutions):
    if is_solution(solution):
        process_solution(solution, solutions)
        return

    for extended_solution in extend_solution(solution, primes, prefixes, initial_digit):
        backtracking(extended_solution, primes, prefixes, initial_digit, solutions)


def main():
    target_sum, initial_digit = read_input()
    primes = find_primes(target_sum)
    prefixes = build_prefix_sets(primes)
    solutions = []

    backtracking([], primes, prefixes, initial_digit, solutions)

    for solution in sorted(solutions):
        for line in solution:
            print(line)
        print("")


if __name__ == "__main__":
    main()