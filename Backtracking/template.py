class Solution:
    def __init__(self):
        cases = self.read_input()
        for case in cases:
            self.solve(case)

    def read_input():
        return

    def is_valid_state(state):
        return True

    def get_candidates(state):
        return []

    def search(self, state, solutions):
        if self.is_valid_state(state):
            solutions.append(state.copy())
            # return

        for candidate in self.get_candidates(state):
            state.add(candidate)
            self.search(state, solutions)
            state.remove(candidate)
            
    def solve(self, case):
        solutions = []
        state = set()
        self.search(state, solutions)
        return solutions


if __name__ == "__main__":
    solution = Solution()