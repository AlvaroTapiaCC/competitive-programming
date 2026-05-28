import math

class Solution:
    def __init__(self):
        self.coins = [i**3 for i in range(1, 22)]

        cases = self.read_input()
        max_value = max(cases)

        self.dp = [0] * (max_value + 1)
        self.dp[0] = 1

        for coin in self.coins:
            for x in range(coin, max_value + 1):
                self.dp[x] += self.dp[x - coin]

        self.solve(cases)
    
    def read_input(self):
        cases = []
        while True:
            try:
                cases.append(int(input().strip()))
            except:
                break
        return cases
    
    def solve_case(self, case):
        return self.dp[case]
    
    def solve(self, cases):
        for case in cases:
            print(self.solve_case(case))

if __name__ == "__main__":
    solution = Solution()