class Solution:
    def __init__(self):
        cases = self.readInput()
        self.solve(cases)
    
    def readInput(self):
        cases = []
        n = int(input().strip())
        for _ in range(n):
            blank = input()
            case = {}
            case['params'] = tuple(map(int, input().strip().split()))
            case['e_coins'] = []
            for _ in range(case['params'][0]):
                case['e_coins'].append(tuple(map(int, input().strip().split())))
            cases.append(case)
        return cases
    
    def solveCase(self, case):
        m, S = case['params']
        coins = case['e_coins']
        S2 = S * S

        INF = float('inf')
        # dp[c][it] = mínimo de monedas para tener suma_c=c, suma_it=it
        dp = [[INF] * (S + 1) for _ in range(S + 1)]
        dp[0][0] = 0

        # Coin change ilimitado (unbounded) en 2D
        for c in range(S + 1):
            for it in range(S + 1):
                if dp[c][it] == INF:
                    continue
                for cc, ci in coins:
                    nc, nit = c + cc, it + ci
                    if nc <= S and nit <= S:
                        if dp[nc][nit] > dp[c][it] + 1:
                            dp[nc][nit] = dp[c][it] + 1

        # Buscar mínimo entre todos los (c, it) con c² + it² = S²
        best = INF
        for c in range(S + 1):
            for it in range(S + 1):
                if c * c + it * it == S2:
                    best = min(best, dp[c][it])

        return best if best < INF else "not possible"
    
    def solve(self, cases):
        for case in cases:
            print(f"{self.solveCase(case)}")
            #print(case)


if __name__ == "__main__":
    solution = Solution()