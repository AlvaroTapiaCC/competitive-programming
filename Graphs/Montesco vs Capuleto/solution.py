
class Node:
    def __init__(self, key):
        self.key = key
        self.color = None
        self.visited = False
        
class Graph:
    def __init__(self):
        self.nodes = {}
        self.adjacency = {}
        
    
    def add_node(self, key):
        self.nodes[key] = Node(key)
        
    def get_node(self, key):
        return self.nodes[key]
    
    def add_edge(self, n1, n2):
        if n1 not in self.adjacency:
            self.adjacency[n1] = []
        self.adjacency[n1].append(n2)
        
    def component_dfs(self, start_node, visited=None):
        if visited is None:
            visited = set()
            
        component = []
        
        if start_node not in visited:
            component.append(start_node)
            visited.add(start_node)
            for node in self.adjacency.get(start_node, []):
                if node not in visited:
                    component.extend(self.component_dfs(node, visited))
                    
        return component
        
    def get_connected_components(self):
        for node in self.nodes:
            if node not in self.adjacency:
                self.adjacency[node] = []
        components = []
        visited = set()
        for node in self.nodes:
            if node not in visited:
                component = self.component_dfs(node, visited)
                components.append(component)
        return components
    
    def color_dfs(self, start_node, curr_color):
        self.nodes[start_node].color = curr_color
        for neigh in self.adjacency.get(start_node, []):
            if self.nodes[neigh].color == None:
                if not self.color_dfs(neigh, 1 - curr_color):
                    return False
            elif self.nodes[neigh].color == curr_color:
                return False
        return True
    
    def is_bipartite(self, component):
        for node in component:
            if self.nodes[node].color is None:
                if not self.color_dfs(node, 0):
                    return False
        return True        

    def get_max_guests(self, component):
        cero_count = 0
        one_count = 0
        for node in component:
            if self.nodes[node].color == 0:
                cero_count += 1
            else:
                one_count += 1
        return max(cero_count, one_count)
            
        
class Solution:
    def __init__(self):
        cases = self.read_input()
        self.solve(cases)
    
    def read_input(self):
        cases = []
        num_cases = int(input())
        for c in range(num_cases):
            case = {}
            blank = input()
            num_people = int(input())       # <= 200
            for i in range(1, num_people + 1):
                enemies = list(map(int, input().strip().split()))
                enemies.pop(0)
                case[i] = enemies
            cases.append(case)
        return cases
 
    def solve_case(self, case):
        case_graph = Graph()
        for person in case:
            case_graph.add_node(person)
            
        for person in case:
            for enemy in case[person]:
                if enemy in case:
                    case_graph.add_edge(person, enemy)
                    case_graph.add_edge(enemy, person)

        components = case_graph.get_connected_components()
        
        total_guests = 0
        for component in components:
            if case_graph.is_bipartite(component):
                total_guests += case_graph.get_max_guests(component)
        
        return total_guests
                
                
    def solve(self, cases):
        for case in cases:
            print(self.solve_case(case))
        
        
solution = Solution()