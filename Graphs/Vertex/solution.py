def read_input():
    cases = []
    n = int(input().strip())
    while n > 0:
        case = []
        graph = []
        case.append(n)
        # Read lines until we find a line with 0
        while True:
            line = list(map(int, input().strip().split()))
            if line[0] == 0:
                break
            graph.append(line)
        case.append(graph)
        case.append(list(map(int, input().strip().split()))[1:])
        cases.append(case)
        n = int(input().strip())
    return cases

def build_graph(n: int, case: list):
    graph_dict = {"nodes": [], "node_neighbors": {}}
    for line in case:
        for i, vertex in enumerate(line):
            if vertex != 0:
                if vertex not in graph_dict["nodes"]:
                    graph_dict["nodes"].append(vertex)
                    graph_dict["node_neighbors"][vertex] = []
                if i + 1 < len(line) and line[i+1] != 0:
                    neighbor = line[i+1]
                    if neighbor not in graph_dict["node_neighbors"][vertex]:
                        graph_dict["node_neighbors"][vertex].append(neighbor)
                            
    if len(graph_dict["nodes"]) < n:
        for i in range(1, n + 1):
            if i not in graph_dict["nodes"]:
                graph_dict["nodes"].append(i)

    return graph_dict

def find_inaccessible(graph: dict, test: list):
    total_nodes = len(graph["nodes"])
    for vertex in test:
        visited = set()
        queue = [vertex]
        #visited.add(vertex)
        
        while queue:
            current_node = queue.pop(0)
            if current_node in graph["node_neighbors"]:
                for neighbor in graph["node_neighbors"][current_node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            else:
                break
        
        print_msg = ""
        print_msg += str(total_nodes - len(visited))
        print_msg += " "
        for node in graph["nodes"]:
            if node not in visited:
                print_msg += str(node)
                print_msg += " "
        print(print_msg)

def main():
    cases = read_input()
    for case in cases:
        case_graph = build_graph(case[0], case[1])
        find_inaccessible(case_graph, case[2])
        #print(case_graph)

if __name__ == "__main__":
    main()