import queue

class Node:
    def __init__(self, key):
        self.key = key
        self.color = None

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
        visited = set()
        for node in self.nodes:
            if node not in visited:
                component = self._dfs(node, visited)
                #component = self._bfs(node)
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
    
    def color_dfs(self, start_node, curr_color):
        """DFS with coloring for bipartite checking"""
        self.nodes[start_node].color = curr_color
        for neigh in self.adjacency.get(start_node, []):
            if self.nodes[neigh].color is None:
                if not self.color_dfs(neigh, 1 - curr_color):
                    return False
            elif self.nodes[neigh].color == curr_color:
                return False
        return True
    
    def is_bipartite(self, component):
        """Check if a component is bipartite (2-colorable)"""
        for node in component:
            if self.nodes[node].color is None:
                if not self.color_dfs(node, 0):
                    return False
        return True
    
    def get_max_(self, component):
        """Count nodes by color in a bipartite component"""
        color_0 = sum(1 for node in component if self.nodes[node].color == 0)
        color_1 = len(component) - color_0
        return max(color_0, color_1)
    
    def topological_sort_dfs(self, node, visited, topo_order):
        """Helper DFS for topological sort"""
        visited.add(node)
        for neighbor in self.adjacency.get(node, []):
            if neighbor not in visited:
                self.topological_sort_dfs(neighbor, visited, topo_order)
        topo_order.insert(0, node)
    
    def topological_sort(self):
        """Returns topological ordering of nodes (for DAG)"""
        visited = set()
        topo_order = []
        
        for node in self.nodes:
            if node not in visited:
                self.topological_sort_dfs(node, visited, topo_order)
        
        return topo_order

class Solution:
    def __init__(self):
        cases = self.read_input()
        self.solve(cases)
    
    def read_input(self):
        cases = []
        return cases
    
    def solve_case(self, case):
        case_graph = Graph()
        for var_name in case:
            case_graph.add_node(var_name)
        return 
    
    def solve(self, cases):
        for case in cases:
            print(f"{self.solve_case(case)}")

if __name__ == "__main__":
    solution = Solution()
