import sys

class Solution:
    def __init__(self):
        lines = sys.stdin.read().strip().split('\n')
        idx = 0
        
        while idx < len(lines):
            n = int(lines[idx])
            idx += 1
            
            if n == 0:
                break
            
            planets = {}
            graph = {}
            earth_planets = []
            
            for _ in range(n):
                parts = lines[idx].strip().split()
                idx += 1
                
                planet = parts[0]
                value = float(parts[1])
                routes = parts[2]
                
                planets[planet] = value
                graph[planet] = []
                
                for neighbor in routes:
                    if neighbor == '*':
                        earth_planets.append(planet)
                    else:
                        graph[planet].append(neighbor)
            
            best_planet = None
            best_value = -1
            
            for target in sorted(planets.keys()):
                value = self.get_max_effective_value(target, planets, graph, earth_planets)
                
                if value > best_value:
                    best_value = value
                    best_planet = target
            
            print(f"Import from {best_planet}")
    
    def get_max_effective_value(self, target, planets, graph, earth_planets):
        max_value = 0
        
        for earth_planet in earth_planets:
            value = self.dijkstra_max_path(earth_planet, target, planets, graph)
            max_value = max(max_value, value)
        
        return max_value
    
    def dijkstra_max_path(self, start, target, planets, graph):
        dist = {planet: 0 for planet in planets}
        dist[start] = 1.0
        visited = set()
        
        while len(visited) < len(planets):
            current = None
            max_dist = 0
            
            for planet in planets:
                if planet not in visited and dist[planet] > max_dist:
                    max_dist = dist[planet]
                    current = planet
            
            if current is None or max_dist == 0:
                break
            
            visited.add(current)
            
            for neighbor in graph.get(current, []):
                new_multiplier = dist[current] * 0.95
                if new_multiplier > dist[neighbor]:
                    dist[neighbor] = new_multiplier
        
        return planets[target] * dist[target]

if __name__ == "__main__":
    solution = Solution()
