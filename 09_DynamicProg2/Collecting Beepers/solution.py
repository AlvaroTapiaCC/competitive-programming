import math

class Solution:
    def __init__(self):
        cases = self.readInput()
        #self.dp = self.buildDP()
        self.memo = None
        self.solve(cases)
    
    def readInput(self):
        cases = []
        t = int(input().strip())
        for _ in range(t):
            case = {}
            size = tuple(map(int, input().strip().split()))
            start = tuple(map(int, input().strip().split()))
            b = int(input().strip())
            beepers = []
            for _ in range(b):
                beepers.append(tuple(map(int, input().strip().split())))
            case['size'] = size
            case['start'] = start
            case['beepers'] = beepers
            cases.append(case)
        return cases
    
    # def buildDP(self):
    #     dp = []
    #     return dp
    
    def dist(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
    def shortPathMem(self, pos, res, start):
        if not res:
            return self.dist(pos, start)
        if (pos, res) in self.memo:
            return self.memo[(pos, res)]
        
        best = float('inf')
        
        for b in res:
            new_res = tuple(x for x in res if x != b)
            distance = self.dist(pos, b) + self.shortPathMem(b, new_res, start)
            best = min(best, distance)
            
        self.memo[(pos, res)] = best
        return best
        
    
    def solveCase(self, case):
        self.memo = {}
        start = case['start']
        beepers = case['beepers']

        return self.shortPathMem(start, tuple(beepers), start)
    
    def solve(self, cases):
        for case in cases:
            print(f"The shortest path has length {self.solveCase(case)}")
            #print(case)


if __name__ == "__main__":
    solution = Solution()