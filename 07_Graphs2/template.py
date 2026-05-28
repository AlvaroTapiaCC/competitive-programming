class Node:
    def __init__(self, key):
        self.key = key
        self.dist = float('inf')
        self.parent = None

class Graph:
    def __init__(self):
        self.nodes = {}
        self.adjacency = {}  # {node: [(neighbor, weight), ...]}
    
    def add_node(self, key):
        self.nodes[key] = Node(key)
    
    def add_edge(self, n1, n2, weight=1):
        if n1 not in self.adjacency:
            self.adjacency[n1] = []
        self.adjacency[n1].append((n2, weight))
    
    def dijkstra(self, start):
        """Find shortest path from start to all nodes"""
        for node in self.nodes:
            self.nodes[node].dist = float('inf')
        
        self.nodes[start].dist = 0
        unvisited = set(self.nodes.keys())
        
        while unvisited:
            # Find unvisited node with minimum distance
            u = min(unvisited, key=lambda x: self.nodes[x].dist)
            
            if self.nodes[u].dist == float('inf'):
                break
            
            for v, weight in self.adjacency.get(u, []):
                if self.nodes[u].dist + weight < self.nodes[v].dist:
                    self.nodes[v].dist = self.nodes[u].dist + weight
                    self.nodes[v].parent = u
            
            unvisited.remove(u)
        
        return {node: self.nodes[node].dist for node in self.nodes}
    
    def floyd_warshall(self):
        """Find shortest paths between all pairs"""
        # Initialize distance matrix
        nodes_list = list(self.nodes.keys())
        n = len(nodes_list)
        
        # Create distance matrix
        dist = {}
        for i in nodes_list:
            dist[i] = {}
            for j in nodes_list:
                if i == j:
                    dist[i][j] = 0
                else:
                    dist[i][j] = float('inf')
        
        # Add edges
        for u in self.adjacency:
            for v, weight in self.adjacency[u]:
                dist[u][v] = weight
        
        # Floyd-Warshall
        for k in nodes_list:
            for i in nodes_list:
                for j in nodes_list:
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        return dist

class DisjointSet:
    """Union-Find data structure for connected components"""
    def __init__(self):
        self.parent = {}
        self.rank = {}
    
    def make_set(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False
        
        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        
        return True
    
    def is_same(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def __init__(self):
        cases = self.read_input()
        self.solve(cases)
    
    def read_input(self):
        cases = []
        return cases
    
    def solve_case(self, case):
        case_graph = Graph()
        return
    
    def solve(self, cases):
        for case in cases:
            print(self.solve_case(case))

if __name__ == "__main__":
    solution = Solution()
