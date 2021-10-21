edges = [
    ['w', 'x'],
    ['x', 'y'],
    ['z', 'y'],
    ['z', 'v'],
    ['w', 'v']
]

def shortestPath(edges:list[list[str]], src:str, dst:str) -> int:
    visited = set()
    graph = generateGraph(edges)
    return BFS_explorePath(graph, src, dst, visited)

def BFS_explorePath(graph, src, dst, visited:set) -> int:
    queue = [[src, 0]]
    while queue:
        q_0 = queue.pop(0)
        curr, dist = q_0
        if curr == dst:
            return dist

        for neigh in graph[curr]:
            if neigh not in visited:
                queue.append([neigh, dist + 1])
                visited.add(neigh)

    return -1

def generateGraph(edges:list[list[str]]) -> dict:
    graph = {}
    for edge in edges:
        a, b = edge
        if a not in graph:
            graph[a] = []
        
        if b not in graph:
            graph[b] = []
        
        graph[a].append(b)
        graph[b].append(a)
    return graph

print(shortestPath(edges, 'w', 'z'))

# Time Complexity:
# n = number of nodes
# e = number of edges

# Space Complexity:
# O(n), n nodes