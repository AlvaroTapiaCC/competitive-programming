import math

class Solution:
    def __init__(self):
        cases = self.readInput()
        self.dp = None
        #self.memo = None
        self.solve(cases)
    
    def readInput(self):
        cases = []
        while True:
            case = []
            while True:
                try:
                    line = list(map(int, input().strip().split()))
                    if line[-1] == -999999:
                        line.pop()
                        case.extend(line) 
                        break
                    case.append(line)
                except:
                    return cases
            cases.append(case)
    
    def buildDP(self, case):
        total_nums = len(case)
        dp = {}
        dp['max'] = [0] * total_nums
        dp['min'] = [0] * total_nums
        
        dp['max'][0]  = case[0]
        dp['min'][0] = case[0]
        
        total_nums = len(case)
        for i in range(1, total_nums):
            dp['max'][i] = max(case[i], dp['max'][i-1] * case[i], dp['min'][i-1] * case[i])
            dp['min'][i] = min(case[i], dp['max'][i-1] * case[i], dp['min'][i-1] * case[i])
            
        return dp
    
    # def shortPathMem(self):
    #     return
    
    def solveCase(self, case):
        n = len(case)
        self.dp = self.buildDP(case)
        return max(self.dp['max'])
    
    def solve(self, cases):
        for case in cases:
            print(f"{self.solveCase(case)}")
            #print(case)

if __name__ == "__main__":
    solution = Solution()