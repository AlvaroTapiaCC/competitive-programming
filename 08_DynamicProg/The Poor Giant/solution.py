import functools

class Solution:
    def __init__(self):
        cases = self.read_input()
        self.solve(cases)
    
    def read_input(self):
        cases = []
        t = int(input().strip())
        for _ in range(t):
          case = tuple(map(int, input().strip().split()))
          case_dict = {}
          for i in range(case[0]):
              case_dict[i+1] = i+1+case[1]
          cases.append(case_dict)
        return cases
    
    def solve_case(self, case):
        weights = [case[i] for i in sorted(case.keys())]
        return self.minWeight(0, len(weights) - 1, tuple(weights))
    
    def solve(self, cases):
        for i, case in enumerate(cases):
            print(f"Case {i+1}: {self.solve_case(case)}")
            #print(case)
    
    @functools.lru_cache(None)
    def minWeight(self, left, right, weights):
        if left > right:
            return 0
        min_weight = float('inf')
        
        for i in range(left, right + 1):
            left_cost = self.minWeight(left, i - 1, weights)
            right_cost = self.minWeight(i + 1, right, weights)
            
            cost = ((right - left + 1) * weights[i] + left_cost + right_cost)
            min_weight = min(min_weight, cost)
        
        return min_weight

if __name__ == "__main__":
    solution = Solution()