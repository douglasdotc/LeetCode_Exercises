# Find the number of subgraphs in a given graph

graph = {
    1: [2],
    2: [1],
    3: [ ],
    4: [6],
    5: [6],
    6: [4,5,7,8],
    7: [6],
    8: [6]
}

def connectedComponent(graph:dict) -> int:
    count = 0
    visited = set()
    for node in graph:
        if explore(graph, node, visited):
            count += 1
    
    return count

def explore(graph:dict, node:int, visited:set) -> bool:
    if node in visited:
        return False
    
    visited.add(node)

    for neigh in graph[node]:
        explore(graph, neigh, visited)
    
    return True

print(connectedComponent(graph))

# Time Complexity:
# n = number of nodes
# e = number of edges
# explore(): at most n nodes, every node at most n - 1 neighbours --> O(n^2), searching if node in visited needs O(n) time at most. O(n^2 + n) --> O(n^2)
# connectedComponent(): loop for n nodes --> O(n)
# Overall O(n^3)

# structy said it is O(e)???

# Space Complexity:
# visited nodes: at most n nodes --> O(n)