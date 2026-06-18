class Solution:
    def __init__(self):
        cases = self.readInput()
        self.solve(cases)

    def readInput(self):
        cases = []
        t = int(input().strip())
        for _ in range(t):
            n = int(input().strip())
            route = []
            for _ in range(n - 1):
                route.append(int(input().strip()))
            cases.append(route)
        return cases

    def solveCase(self, route, r):
        n = len(route)  # número de aristas = paradas - 1

        best_sum = 0
        best_i = 0      # parada inicio (1-indexed)
        best_j = 0      # parada fin   (1-indexed)
        best_len = 0

        cur_sum = 0
        cur_start = 0   # índice de arista donde empieza el segmento actual

        for k in range(n):
            cur_sum += route[k]

            # parada inicio = cur_start + 1, parada fin = k + 2 (1-indexed)
            i = cur_start + 1
            j = k + 2
            length = j - i

            better = (
                cur_sum > best_sum or
                (cur_sum == best_sum and length > best_len) or
                (cur_sum == best_sum and length == best_len and i < best_i)
            )

            if better:
                best_sum = cur_sum
                best_i = i
                best_j = j
                best_len = length

            # Reiniciar si la suma acumulada es negativa
            if cur_sum < 0:
                cur_sum = 0
                cur_start = k + 1

        if best_sum <= 0:
            return f"Route {r} has no nice parts"
        return f"The nicest part of route {r} is between stops {best_i} and {best_j}"

    def solve(self, cases):
        for r, route in enumerate(cases, 1):
            print(self.solveCase(route, r))


if __name__ == "__main__":
    solution = Solution()