import math

class Solution:
    def __init__(self):
        cases = self.readInput()
        self.primes = []
        for n in range (2, 1120):
            if self.isPrime(n):
                self.primes.append(n)
        self.dp = self.buildDP()               
        self.solve(cases)
        
    def isPrime(self, n):
        if n < 2:
            return False
        elif n == 2:
            return True
        else:
            for i in range(2, round(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True
        
    def readInput(self):
        cases = []
        while True:
            case = tuple(map(int, input().strip().split()))
            if case == (0, 0):
                break
            cases.append(case)
        return cases
    
    def buildDP(self):
        MAX_SUM = 1121
        MAX_K = len(self.primes)
        dp = [[0] * (MAX_K + 1) for _ in range(MAX_SUM)]
        dp[0][0] = 1 
        
        for prime in self.primes:
            for s in range(MAX_SUM - 1, prime - 1, -1):
                for k in range(MAX_K, 0, -1):
                    dp[s][k] += dp[s - prime][k - 1]
        return dp
    
    def solveCase(self, case):
        return self.dp[case[0]][case[1]]
    
    def solve(self, cases):
        for case in cases:
            print(f"{self.solveCase(case)}")


if __name__ == "__main__":
    solution = Solution()