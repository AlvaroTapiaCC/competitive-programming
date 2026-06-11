class Solution:
    def __init__(self):
        cases = self.readInput()
        self.dp = None
        self.solve(cases)
    
    def readInput(self):
        cases = []
        while True:
            case = []
            N = int(input().strip())
            if N == 0:
                break
            for _ in range(N):
                box = tuple(map(int, input().strip().split()))
                case.append(box)
            cases.append(case)
        return cases
    
    def buildDP(self, case):
        n = len(case)
        # best[i] = {length: min_weight} para pilas con i como base
        best = [{1: case[i][0]} for i in range(n)]
        
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                for length, weight in best[j].items():
                    if weight <= case[i][1]:
                        new_len = length + 1
                        new_weight = weight + case[i][0]
                        if new_len not in best[i] or new_weight < best[i][new_len]:
                            best[i][new_len] = new_weight
        
        result = 0
        for d in best:
            result = max(result, max(d.keys()))
        return result          
            
    def solveCase(self, case):
        return self.buildDP(case)

        
    def solve(self, cases):
        for case in cases:
            print(f"{self.solveCase(case)}")
            #print(case)

if __name__ == "__main__":
    solution = Solution()