import math

class Solution:
    def __init__(self):
        cases = self.readInput()
        self.dp = None
        self.solve(cases)
    
    def readInput(self):
        cases = []
        t = int(input().strip())
        for _ in range(t):
            cases.append(list(map(int, input().strip().split())))
        return cases
    
    def buildDP(self, weights):
        target_weight = sum(weights) // 2
        
        dp = [[False] * (target_weight + 1) for _ in range(len(weights) + 1)]
        dp[0][0] = True
        
        for i in range(1, len(weights) + 1):
            curr_weight = weights[i-1]
            for s in range(target_weight + 1):
                no_weight = dp[i-1][s]
                
                with_wight = dp[i-1][s-curr_weight] if s >= curr_weight else False
                
                dp[i][s] = no_weight or with_wight

        return dp
    
    def solveCase(self, case):
        weight = sum(case)
        if weight % 2 != 0:
            return "NO"
        
        weights = sorted(case)
        
        self.dp = self.buildDP(weights)
        
        return "YES" if self.dp[len(case)][weight//2] else "NO"
    
    def solve(self, cases):
        for case in cases:
            print(f"{self.solveCase(case)}")
            #print(case)


if __name__ == "__main__":
    solution = Solution()