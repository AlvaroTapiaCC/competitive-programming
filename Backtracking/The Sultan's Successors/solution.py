def read_input():
    k = int(input().strip())
    boards = []
    for _ in range(k):
        board = []
        for i in range(8):
            line = list(map(int, input().strip().split()))
            board.append(line)
        boards.append(board)
    return boards

def is_valid_state(state: list):          # IS_SOLUTION
    return len(state) == 8

def get_candidates(state: list):          # EXTEND_SOLUTION
    if not state:
        return range(8)
    
    position = len(state)
    candidates = set(range(8))
    for row, col in enumerate(state):
        candidates.discard(col)
        dist = position - row
        candidates.discard(col + dist)
        candidates.discard(col - dist)
    return candidates

def search(state: list, solutions: list):       # BACKTRACKING
    if is_valid_state(state):
        solutions.append(state.copy())
        # return

    for candidate in get_candidates(state):
        state.append(candidate)
        search(state, solutions)
        state.pop()

def find_best_solution(board: list, solutions: list, best_solutions: list):
    best_sum = 0
    for solution in solutions:
        sum = 0
        for r, col in enumerate(solution):
            sum += board[r][col]
        if sum > best_sum:
            best_sum = sum
    best_solutions.append(best_sum)



def main():                        # MAIN  
    boards = read_input()
    best_solutions = []
    solutions = []
    state = []
    search(state, solutions)
    for board in boards:
        find_best_solution(board, solutions, best_solutions)
    
    for solution in best_solutions:
        print(f"{solution:>5}")

if __name__ == "__main__":
    main()