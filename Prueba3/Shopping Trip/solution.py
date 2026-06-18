import heapq

class Node:
    def __init__(self, key):
        self.key = key

class Graph:
    def __init__(self):
        self.nodes = {}
        self.adjacency = {}

    def add_node(self, key):
        if key not in self.nodes:
            self.nodes[key] = Node(key)

    def add_edge(self, n1, n2, weight=1):
        if n1 not in self.adjacency:
            self.adjacency[n1] = []
        if n2 not in self.adjacency:
            self.adjacency[n2] = []
        self.adjacency[n1].append((n2, weight))
        self.adjacency[n2].append((n1, weight))

    def dijkstra(self, start):
        dist = {node: float('inf') for node in self.nodes}
        dist[start] = 0.0
        pq = [(0.0, start)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in self.adjacency.get(u, []):
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))
        return dist


class Solution:
    def __init__(self):
        cases = self.readInput()
        self.solve(cases)

    def readInput(self):
        cases = []
        t = int(input().strip())
        for _ in range(t):
            input()  # blank line
            case = {}
            case['roads'] = []
            params = tuple(map(int, input().strip().split()))
            for _ in range(params[1]):
                road = input().strip().split()
                case['roads'].append(road)
            p = int(input().strip())
            case['operas'] = []
            for _ in range(p):
                dvd = input().strip().split()
                case['operas'].append(dvd)
            cases.append(case)
        return cases

    def solveCase(self, case):
        # Construir grafo
        graph = Graph()
        graph.add_node(0)
        for u, v, w in case['roads']:
            u, v, w = int(u), int(v), float(w)
            graph.add_node(u)
            graph.add_node(v)
            graph.add_edge(u, v, w)

        # Agregar savings por tienda
        store_savings = {}
        for store, saving in case['operas']:
            store, saving = int(store), float(saving)
            store_savings[store] = store_savings.get(store, 0.0) + saving

        # Solo tiendas con ahorro positivo
        relevant = [s for s, sv in store_savings.items() if sv > 0]
        if not relevant:
            return "Don't leave the house"

        # Dijkstra desde casa y desde cada tienda relevante
        key_nodes = [0] + relevant
        dist = {n: graph.dijkstra(n) for n in key_nodes}

        # Bitmask DP
        k = len(relevant)
        INF = float('inf')
        dp = [[INF] * k for _ in range(1 << k)]

        for i, store in enumerate(relevant):
            dp[1 << i][i] = dist[0][store]

        for mask in range(1, 1 << k):
            for i in range(k):
                if not (mask & (1 << i)) or dp[mask][i] == INF:
                    continue
                for j in range(k):
                    if mask & (1 << j):
                        continue
                    new_mask = mask | (1 << j)
                    cost = dp[mask][i] + dist[relevant[i]][relevant[j]]
                    if cost < dp[new_mask][j]:
                        dp[new_mask][j] = cost

        # Evaluar todos los subconjuntos
        best = 0.0
        for mask in range(1, 1 << k):
            total_saving = sum(
                store_savings[relevant[i]]
                for i in range(k) if mask & (1 << i)
            )
            for i in range(k):
                if not (mask & (1 << i)) or dp[mask][i] == INF:
                    continue
                travel = dp[mask][i] + dist[relevant[i]][0]
                net = total_saving - travel
                if net > best:
                    best = net

        if best <= 0:
            return "Don't leave the house"
        return f"Daniel can save ${best:.2f}"

    def solve(self, cases):
        for case in cases:
            print(self.solveCase(case))


if __name__ == "__main__":
    solution = Solution()