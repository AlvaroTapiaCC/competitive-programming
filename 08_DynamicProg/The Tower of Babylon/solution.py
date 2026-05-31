import math

class Solution:
    def __init__(self):
        self.dp = None
        
        cases = self.readInput()
        self.solve(cases)
    
    def readInput(self):
        cases = []
        while True:
            case = []

            n = int(input().strip())
            if n == 0:
                break
            for _ in range(n):
                block = tuple(map(int, input().strip().split()))
                case.append(block)
            cases.append(case)
        return cases
    
    def solveCase(self, case):
 
        blocks = self.getBlockCombinations(case)

        self.dp = [0] * len(blocks)
        
        for i in range(len(blocks)):
            self.dp[i] = blocks[i][2]
            
        for i in range(len(blocks)):
            lenght_i = blocks[i][0]
            width_i = blocks[i][1]
            height_i = blocks[i][2]
            
            for j in range(i):
                lenght_j = blocks[j][0]
                width_j = blocks[j][1]
                if (lenght_i < lenght_j and width_i < width_j) or (lenght_i < width_j and width_i < lenght_j):
                    self.dp[i] = max(self.dp[i], self.dp[j] + height_i)
                
        return max(self.dp)

    
    def getBlockCombinations(self, case):
        combinations = set()
        for block in case:
            for i in range(3):
                height = block[i]
                base = [block[j] for j in range(3) if j != i]
                block_tuple = (max(base[0], base[1]), min(base[0], base[1]), height)
                if block_tuple not in combinations:
                    combinations.add(block_tuple)
        return sorted(combinations, reverse=True)
    
    def solve(self, cases):
        for i, case in enumerate(cases):
            #self.solveCase(case)
            print(f"Case {i+1}: maximum height = {self.solveCase(case)}")


if __name__ == "__main__":
    solution = Solution()