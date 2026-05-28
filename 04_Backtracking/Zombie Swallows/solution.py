def read_input():
    zombies = []
    n = int(input().strip())
    for _ in range(n):
        zombie = []
        insects = []
        line = list(map(int, input().strip().split()))
        zombie.append(line[0])
        zombie.append(line[1])
        for i in range(line[2]):
            insects.append(line[3 + i])
        zombie.append(insects)
        zombies.append(zombie)
    return zombies


def is_valid_state(index, state, zombie: list):
    if index != len(zombie[2]):
        return False
    return True

def search(index, state: list, zombie: list, solutions: list):
    if is_valid_state(index, state, zombie):
        solutions.append(state.copy())
        return

    search(index + 1, state, zombie, solutions)

    state.append(zombie[2][index])
    search(index + 1, state, zombie, solutions)
    state.pop()

def calorie_track(zombie: list, solutions: list):
    real_solutions = []
    for solution in solutions:
        if sum(solution) >= zombie[0] and sum(solution) <= zombie[1]:
            real_solutions.append(solution)
    if len(real_solutions) > 0:
        print("Sallow swallow swallows.")
    else:
        print("Sallow swallow wallows in dust.")

def main():
    zombies = read_input()   
    solutions_by_zombie = []
    for idx, zombie in enumerate(zombies):
        solutions = []
        state = []
        search(0, state, zombie, solutions)
        solutions_by_zombie.append(solutions)
        calorie_track(zombie, solutions_by_zombie[idx])

if __name__ == "__main__":
    main()