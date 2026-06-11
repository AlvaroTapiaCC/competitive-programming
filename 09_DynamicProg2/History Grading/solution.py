import math

class Solution:
    def __init__(self):
        cases = self.readInput()
        self.dp = self.buildDP()
        self.solve(cases)
    
    def readInput(self):
        cases = []
        case = []
        first = True
        while True: 
            try:
                line = list(map(int, input().strip().split()))
                if len(line) > 1:
                    case.append(line)
                elif len(line) == 1:
                    if first:
                        first = False                
                        continue
                    else:
                        cases.append(case)
                        case = []
            except:
                return cases
            

    
    def buildDP(self):
        dp = []
        return dp
    
    def solveCase(self, case):
        return 
    
    def solve(self, cases):
        for case in cases:
            #print(f"{self.solveCase(case)}")
            print(case)

if __name__ == "__main__":
    solution = Solution()   