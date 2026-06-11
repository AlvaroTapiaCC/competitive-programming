


class Solution:
    def __init__(self):
        cases = self.readInput()
        self.solve(cases)
    
    def readInput(self):
        cases = []
        while True:
            case = []
            n = int(input().strip())
            if n == 0:
                break
            for _ in range(n + 1):
                case.append(tuple(map(int, input().strip().split())))
            cases.append(case)
        return cases
    
    def isInside(self, polygon, px, py):
        n = len(polygon)
        crossings = 0
        for i in range(n):
            x1, y1 = polygon[i]
            x2, y2 = polygon[(i + 1) % n]
            if x1 == x2:  # vertical edge
                if min(y1, y2) < py <= max(y1, y2):
                    if x1 > px:
                        crossings += 1
        return crossings % 2 == 1
    
    def solveCase(self, case): 
        p = case[len(case) - 1]
        case.pop()
        
        return "T" if self.isInside(case, p[0], p[1]) else "F"
    
    def solve(self, cases):
        for case in cases:
            print(f"{self.solveCase(case)}")
            #print(case)

if __name__ == "__main__":
    solution = Solution()