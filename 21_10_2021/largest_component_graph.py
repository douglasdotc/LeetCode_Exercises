graph = {
    0: [8,1,5],
    1: [0],
    2: [3,4],
    3: [2,4],
    4: [3,2],
    5: [0,8],
    8: [0,5]
}

def largestComponent(graph:dict) -> int:
    largest_graph = 0
    visited = set()
    for node in graph:
        size = exploreSize(graph, node, visited)
        if size > largest_graph:
            largest_graph = size
    
    return largest_graph

def exploreSize(graph:dict, node:int, visited:set) -> int:
    if node in visited:
        return 0
    
    visited.add(node)
    size = 1
    for neigh in graph[node]:
        size += exploreSize(graph, neigh, visited)
    
    return size

print(largestComponent(graph))

# Time Complexity:
# n = number of nodes
# e = number of edges
# O(e) again?? or O(n^3)

# Space Complexity:
# visited nodes: at most n nodes --> O(n)