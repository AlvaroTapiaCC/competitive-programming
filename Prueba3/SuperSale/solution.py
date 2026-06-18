class Solution:
    def __init__(self):
        cases = self.readInput()
        self.solve(cases)

    def readInput(self):
        cases = []
        t = int(input().strip())
        for _ in range(t):
            case = {}
            n = int(input().strip())
            case['objects'] = []
            for _ in range(n):
                case['objects'].append(tuple(map(int, input().strip().split())))
            g = int(input().strip())
            case['people'] = []
            for _ in range(g):
                case['people'].append(int(input().strip()))
            cases.append(case)
        return cases
    
    def solveCase(self, case):
        objects = case['objects']
        people = case['people']

        total = 0
        for cap in people:
            dp = [0] * (cap + 1)
            for price, weight in objects:
                for c in range(cap, weight - 1, -1):
                    dp[c] = max(dp[c], dp[c - weight] + price)
            total += dp[cap]
        return total
    
    def solve(self, cases):
        for case in cases:
            print(f"{self.solveCase(case)}")


if __name__ == "__main__":
    solution = Solution()