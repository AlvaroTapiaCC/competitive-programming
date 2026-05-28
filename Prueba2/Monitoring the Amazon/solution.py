import sys
import queue

class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        

class Graph:
    def __init__(self):
        self.nodes = {}
        self.adjacency = {}
    
    def add_node(self, key, data):
        self.nodes[key] = Node(key, data)
    
    def add_edge(self, n1, n2):
        if n1 not in self.adjacency:
            self.adjacency[n1] = []
        if n2 not in self.adjacency[n1]:
            self.adjacency[n1].append(n2)

        
    def get_closest_nodes(self, start_node):
        distances = []
        for node in self.nodes:
            if node != start_node:
                dist = self.euclid_dist(start_node, node)
                distances.append((dist, node))
        
        distances.sort(key=lambda x: (x[0], self.nodes[x[1]].data[0], self.nodes[x[1]].data[1]))
    
        return [distances[0][1], distances[1][1]]
                
            
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

    def leftmost(self, n1, n2):
        if self.nodes[n1].data[0] == self.nodes[n2].data[0]:
            return False
        if self.nodes[n1].data[0] < self.nodes[n2].data[0]:
            return n1
        else:
            return n2

    def southmost(self, n1, n2):
        if self.nodes[n1].data[1] < self.nodes[n2].data[1]:
            return n1
        else:
            return n2
        
    def euclid_dist(self, n1, n2):
        return ((self.nodes[n1].data[0]-self.nodes[n2].data[0])**2 + (self.nodes[n1].data[1]-self.nodes[n2].data[1])**2)**0.5


class Solution:
    def __init__(self):
        cases = self.read_input()
        self.solve(cases)
    
    def read_input(self):
        cases = []
        while True:
            case = {}
            n = int(input().strip())
            if n == 0:
                break
            cords = list(map(int, input().strip().split()))
            for i in range(n):
                case[i+1] = (cords[i*2], cords[i*2 + 1])
            cases.append(case)
        return cases
    

    
    def solve_case(self, case):
        case_graph = Graph()
        for station in case:
            case_graph.add_node(station, case[station])
            
        connections = {}
        for station in case:
            closest = case_graph.get_closest_nodes(station)
            connections[station] = closest
            
        for station in case:
            case_graph.add_edge(station, connections[station][0])
            case_graph.add_edge(station, connections[station][1])

        stations = case_graph._dfs(1)

        if len(stations) == len(case):
            return True
        else:
            return False 
    
    def solve(self, cases):
        for case in cases:
            if self.solve_case(case):
                print("All stations are reachable.")
            else:
                print("There are stations that are unreachable.")

if __name__ == "__main__":
    solution = Solution()