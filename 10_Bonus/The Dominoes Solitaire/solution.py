class Solution:
    def __init__(self):
        cases = self.read_input()
        for case in cases:
            #print(case)
            print(f"{self.solve(case)}")

    def read_input(self):
        cases = []
        while True:
            case = {}
            n = int(input().strip())
            if n == 0:
                break
            m = int(input().strip())
            start = tuple(map(int, input().strip().split()))
            end = tuple(map(int, input().strip().split()))
            
            pieces = []
            for _ in range(m):
                pieces.append(tuple(map(int, input().strip().split())))
                
            case['spaces'] = n
            case['pieces'] = pieces
            case['start'] = start
            case['end'] = end
            
            cases.append(case)
        return cases

    def is_valid_state(self, state, n):
        if len(state) != n:
            return False
        return True

    def get_candidates(self, state, case):
        start = case['start'][1]
        end = case['end'][0]
        last = start if not state else state[-1][0][1]  # fix: [0][1]
        
        used_indices = {idx for _, idx in state}
        
        candidates = []
        is_last = len(state) == case['spaces'] - 1
        
        for i, p in enumerate(case['pieces']):
            if i in used_indices:
                continue
            for candidate in [p, (p[1], p[0])]:
                if candidate[0] == last:
                    if not is_last or candidate[1] == end:
                        candidates.append((candidate, i))
                    break  # break here: once we find the right orientation, no need to try the other
        
        return candidates

    def search(self, state, case):
        if self.is_valid_state(state, case['spaces']):
            return True

        for candidate in self.get_candidates(state, case):
            state.append(candidate)
            if self.search(state, case):
                return True
            state.pop()
        
        return False
            
    def solve(self, case):
        #solutions = []
        return "YES" if self.search([], case) else "NO"


if __name__ == "__main__":
    solution = Solution()