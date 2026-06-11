import queue

class Node:
    def __init__(self, key):
        self.key = key
        self.color = None

class Graph:
    def __init__(self):
        self.nodes = {}
        self.adjacency = {}
        self.edge_weights = {}
    
    def add_node(self, key):
        self.nodes[key] = Node(key)
    
    def add_edge(self, n1, n2, weight=1):
        if n1 not in self.adjacency:
            self.adjacency[n1] = []
        if n2 not in self.adjacency:
            self.adjacency[n2] = []
        self.adjacency[n1].append((n2, weight))
        self.adjacency[n2].append((n1, weight))
        self.edge_weights[(n1, n2)] = weight
        self.edge_weights[(n2, n1)] = weight
        
    def dijkstra(self, start, target, locked_cost):
        dist = {node: float('inf') for node in self.nodes}
        dist[start] = 0
        visited = set()
        pq = queue.PriorityQueue()
        pq.put((0, start))
        best = float('inf')

        while not pq.empty():
            cost, u = pq.get()

            if u in visited:
                continue
            visited.add(u)

            for v, weight in self.adjacency.get(u, []):
                if v in visited:
                    continue
                new_cost = cost + weight

                if v in locked_cost:
                    # entering the regular path: add the fixed remaining cost
                    best = min(best, new_cost + locked_cost[v])
                else:
                    if new_cost < dist[v]:
                        dist[v] = new_cost
                        pq.put((new_cost, v))

        return best
    

class Solution:
    def __init__(self):
        cases = self.read_input()
        self.solve(cases)
    
    def read_input(self):
        cases = []
        while True:
            case = {}
            try:
                line = tuple(map(int, input().strip().split()))
                if sum(line) == 0:
                    break
            except:
                break
            case['cities'] = line[0]
            case['target'] = line[2] - 1
            case['start'] = line[3]
            case['roads'] = []
            for _ in range(line[1]):
                case['roads'].append(tuple(map(int, input().strip().split())))
            cases.append(case)
        return cases
    
    def solve_case(self, case):
        target = case['target']
        start = case['start']
        
        case_graph = Graph()
        
        for i in range(case['cities']):
            case_graph.add_node(i)
        
        for road in case['roads']:
            case_graph.add_edge(road[0], road[1], road[2])
        
        locked_cost = {target: 0}
        for i in range(target - 1, -1, -1):
            edge = (i, i + 1)
            if edge in case_graph.edge_weights:
                locked_cost[i] = case_graph.edge_weights[edge] + locked_cost[i + 1]
            else:
                locked_cost[i] = float('inf')  # path is broken

        result = case_graph.dijkstra(start, target, locked_cost)
        return result if result < float('inf') else "NO PATH"

    
    def solve(self, cases):
        for case in cases:
            print(f"{self.solve_case(case)}")
            #print(case)
if __name__ == "__main__":
    solution = Solution()
