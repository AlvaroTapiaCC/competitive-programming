def read_input():
    return

def is_valid_state(state):
    return True

def get_candidates(state):
    return []

def search(state, solutions):
    if is_valid_state(state):
        solutions.append(state.copy())
        # return

    for candidate in get_candidates(state):
        state.add(candidate)
        search(state, solutions)
        state.remove(candidate)

def main():
    solutions = []
    state = set()
    search(state, solutions)
    return solutions

if __name__ == "__main__":
    main()