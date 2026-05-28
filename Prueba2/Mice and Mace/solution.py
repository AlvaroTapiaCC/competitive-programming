class Node:
    def __init__(self, key):
        self.key = key
        self.dist = float('inf')

class Graph:
    def __init__(self, vars):
        self.cells = vars[0]
        self.exit = vars[1]
        self.timer = vars[2]
        self.nodes = {}
        self.adjacency = {}  # {node: [(neighbor, weight), ...]}
    
    def add_node(self, key):
        if key not in self.nodes:
            self.nodes[key] = Node(key)
    
    def add_edge(self, n1, n2, weight):
        if n1 not in self.adjacency:
            self.adjacency[n1] = []
        self.adjacency[n1].append((n2, weight))
    
    def dijkstra(self):

        self.nodes[self.exit].dist = 0
        
        unvisited = set(self.nodes.keys())
        
        while unvisited:
            # Find unvisited node with minimum distance
            u = min(unvisited, key=lambda x: self.nodes[x].dist)
            
            if self.nodes[u].dist == float('inf'):
                break

            for neighbor, weight in self.adjacency.get(u, []):
                if neighbor in unvisited:
                    if self.nodes[u].dist + weight < self.nodes[neighbor].dist:
                        self.nodes[neighbor].dist = self.nodes[u].dist + weight
            
            unvisited.remove(u)
        
        return len([m for m in self.nodes if self.nodes[m].dist <= self.timer])

    



class Solution:
    def __init__(self):
        cases = self.read_input()
        self.solve(cases)
    
    def read_input(self):
        cases = []
        num_cases = int(input().strip())
        for _ in range(num_cases):
            case = {}
            case = {}
            case['vars'] = []
            case['connections'] = []
            blank = input()
            for _ in range(3):
                case['vars'].append(int(input().strip()))
            m = int(input().strip())
            for c in range(m):
                case['connections'].append(tuple(map(int, input().strip().split())))
            cases.append(case)
        return cases
    
    def solve_case(self, case):
        case_graph = Graph(case['vars'])
        for connection in case['connections']:
            case_graph.add_node(connection[0])
            case_graph.add_node(connection[1])
            case_graph.add_edge(connection[0], connection[1], connection[2])
            
        return  case_graph.dijkstra()
    
    def solve(self, cases):
        for case in cases:
            print(self.solve_case(case))

if __name__ == "__main__":
    solution = Solution()
