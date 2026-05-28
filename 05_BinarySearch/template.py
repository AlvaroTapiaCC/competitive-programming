from bisect import bisect_left, bisect_right

class BinarySearch:
    """Generic binary search implementations"""
    
    @staticmethod
    def search_array(arr, predicate):
        """
        General binary search on sorted array.
        Find first element where predicate(x) is True.
        """
        a = 0
        b = len(arr) - 1
        
        while a < b:
            c = a + (b - a) // 2
            if predicate(arr[c]):
                b = c
            else:
                a = c + 1
        
        if not predicate(arr[a]):
            return None
        return arr[a]
    
    @staticmethod
    def search_continuous(f, lo, hi, eps=1e-6):
        """Binary search on continuous domain"""
        while hi - lo > eps:
            mid = lo + (hi - lo) / 2
            if f(mid):
                hi = mid
            else:
                lo = mid
        return lo
    
    @staticmethod
    def search_on_answer(predicate, lo, hi):
        """Binary search on the answer"""
        result = None
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if predicate(mid):
                result = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return result
    
    @staticmethod
    def bisect_find_position(arr, value):
        """Find position in sorted array using bisect library"""
        left = bisect_left(arr, value)
        right = bisect_right(arr, value)
        return left, right  # (first_position, last_position + 1)
    
    @staticmethod
    def bisect_find_first(arr, predicate):
        """Find first element where predicate is True using bisect with key"""
        # Note: requires custom key function
        idx = bisect_left(arr, True, key=predicate)
        if idx < len(arr) and predicate(arr[idx]):
            return arr[idx]
        return None

class Solution:
    def __init__(self):
        cases = self.read_input()
        self.solve(cases)
    
    def read_input(self):
        cases = []
        return cases
    
    def solve_case(self, case):
        return
    
    def solve(self, cases):
        for case in cases:
            print(self.solve_case(case))

if __name__ == "__main__":
    solution = Solution()
