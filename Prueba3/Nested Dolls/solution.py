class Solution:
    def __init__(self):
        cases = self.readInput()
        self.solve(cases)
    
    def readInput(self):
        cases = []
        t = int(input().strip())
        for _ in range(t):
            m = int(input().strip())
            dolls = list(map(int, input().strip().split()))
            dolls = [(dolls[2*i], dolls[2*i + 1]) for i in range(m)]
            cases.append(dolls)
        return cases
    
    def solveCase(self, dolls):
        n = len(dolls)

        def fits(a, b):
            return a[0] < b[0] and a[1] < b[1]

        match_r = [-1] * n

        def dfs(u, visited):
            for v in range(n):
                if fits(dolls[u], dolls[v]) and not visited[v]:
                    visited[v] = True
                    if match_r[v] == -1 or dfs(match_r[v], visited):
                        match_r[v] = u
                        return True
            return False

        matching = 0
        for u in range(n):
            visited = [False] * n
            if dfs(u, visited):
                matching += 1

        return n - matching
    
    def solve(self, cases):
        for case in cases:
            print(f"{self.solveCase(case)}")

if __name__ == "__main__":
    solution = Solution()