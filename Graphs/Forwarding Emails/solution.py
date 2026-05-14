import queue

class Node:
    def __init__(self, key):
        self.key = key
        #self.color = None

class Graph:
    def __init__(self):
        self.nodes = {}
        self.adjacency = {}
    
    def add_node(self, key):
        self.nodes[key] = Node(key)
    
    def add_edge(self, n1, n2):
        if n1 not in self.adjacency:
            self.adjacency[n1] = []
        self.adjacency[n1].append(n2)
    
    def get_connected_components(self):
        for node in self.nodes:
            if node not in self.adjacency:
                self.adjacency[node] = []
        components = []
        for node in self.nodes:
            component = self._dfs(node, visited=None)
            components.append(component)
        return components
    
    def _dfs(self, start_node, visited=None):
        if visited is None:
            visited = set()
        
        component = []
        if start_node not in visited:
            component.append(start_node)
            visited.add(start_node)
            for node in self.adjacency.get(start_node, []):
                if node not in visited:
                    component.extend(self._dfs(node, visited))
        return component
    
    def _bfs(self, start_node):
        visited = set()
        q = queue.Queue()
        q.put(start_node)
        
        component = []
        while not q.empty():
            node = q.get()
            if node not in visited:
                component.append(node)
                visited.add(node) 
            for neighbor in self.adjacency.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.put(neighbor)    
        return component
    

class Solution:
    def __init__(self):
        cases = self.read_input()
        self.solve(cases)
    
    def read_input(self):
        cases = []
        num_cases = int(input())
        for i in range(num_cases):
            case = {}
            num_martians = int(input())
            for j in range(num_martians):
                u, v = input().strip().split()
                case[int(u)] = int(v)
            cases.append(case)
        return cases
    
    def solve_case(self, case):
        case_graph = Graph()
        for martian in case:
            case_graph.add_node(martian)
            
        for martian in case:
            case_graph.add_edge(martian, case[martian])
                    
        components = case_graph.get_connected_components()
                    
        best_martian = None
        best_num = None
        for component in components:
            if best_num is None or len(component) > best_num:
                best_num = len(component)
                best_martian = component[0]
            elif len(component) == best_num:
                if component[0] < best_martian:
                    best_num = len(component)
                    best_martian = component[0]
        
        return best_martian                    
    
    def solve(self, cases):
        for i, case in enumerate(cases):
            print(f"Case {i+1}: {self.solve_case(case)}")

if __name__ == "__main__":
    solution = Solution()