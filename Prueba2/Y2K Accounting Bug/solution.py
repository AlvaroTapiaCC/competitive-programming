"""
each month -> surplus (s) or deficit (d)
how many s or d unknown

ene-feb-mar-abr-may-jun-jul-ago-sep-oct-nov-dec
 1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 - 9 - 10- 11- 12
"""

import sys

class Solution:
    def __init__(self):
        cases = self.read_input()
        self.solve(cases)
    
    def read_input(self):
        cases = []
        for line in sys.stdin:
            if not line.strip():
                break
            cases.append(list(map(int, line.strip().split())))
        return cases
    
    def solve_case(self, case):
        return
    
    def solve(self, cases):
        for case in cases:
            print(case)
#            print(self.solve_case(case))

if __name__ == "__main__":
    solution = Solution()