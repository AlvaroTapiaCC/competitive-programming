import math

class Solution:
    def __init__(self):
        self.max_n = 0
        self.max_nk = 0
        cases = self.readInput()
        self.dp = self.buildDP()
        self.solve(cases)
    
    def readInput(self):
        cases = []
        t = int(input().strip())
        for _ in range(t):
            case = tuple(map(int, input().strip().split()))
            cases.append(case)
            if case[0] > self.max_n:
                self.max_n = case[0]
            if case[0] + case[1] > self.max_nk:
                self.max_nk = case[0] + case[1]
        return cases
    
    def buildDP(self):
        dp = [[0] * (self.max_nk + 1) for _ in range(self.max_n + 1)]
        
        for k in range(self.max_nk + 1):
            dp[0][k] = 0
            dp[1][k] = 0
            
        for n in range(2, self.max_n + 1):
            for k in range(self.max_nk - n + 1):
                best = float('inf')
                
                for i in range(1, n + 1):
                    cost = (n * (k + i) + dp[i - 1][k] + dp[n - i][k + i])
                    best = min(best, cost)
                    
                dp[n][k] = best
        
        return dp
        
    
    def solveCase(self, case):
        return self.dp[case[0]][case[1]]
    
    def solve(self, cases):
        for i, case in enumerate(cases):
            print(f"Case {i + 1}: {self.solveCase(case)}")
            #print(case)


if __name__ == "__main__":
    solution = Solution()