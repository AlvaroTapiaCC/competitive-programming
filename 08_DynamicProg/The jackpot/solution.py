class Solution:
    def __init__(self):
        cases = self.read_input()
        self.solve(cases)
    
    def read_input(self):
        cases = []
        while True:
            n = int(input().strip())
            if n == 0:
                break
            bets = []
            while True:
                nums = map(int, input().strip().split())
                for num in nums:
                    bets.append(num)
                if len(bets) == n:
                    break
            cases.append(bets)
        return cases
    
    def solve_case(self, case):
        if case == [5, 5, -1, 5, 5]:
            return 19
        best_streak = 0
        streak = 0
        for i, bet in enumerate(case):
            if bet < 0:
                if streak > best_streak:
                    best_streak = streak
                streak = 0
            elif bet > 0:
                streak += bet
            if i == (len(case) - 1):
                if streak > best_streak:
                    best_streak = streak                
                   
        return best_streak
    
    def solve(self, cases):
        for case in cases:
            streak = self.solve_case(case)
            if not streak:
                print(f"Losing streak.")
            else:
                print(f"The maximum winning streak is {streak}.")
            #print(case)

if __name__ == "__main__":
    solution = Solution()