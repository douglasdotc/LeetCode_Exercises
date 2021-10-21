edges = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
]

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

def undirectedPath(edges:list[list[str]], src:str, dst:str) -> bool:
    graph = generateGraph(edges)
    return DFS_hasPath(graph, src, dst, set())

def DFS_hasPath(graph:dict, src:str, dst:str, N_visited:set) -> bool:
    if src == dst:
        return True

    if src in N_visited: # To exit infinite loop because of undirected graph structure
        return False
    
    N_visited.add(src)

    for neigh in graph[src]:
        
        if DFS_hasPath(graph, neigh, dst, N_visited):
            return True
    
    return False

print(undirectedPath(edges, 'i', 'l'))

# Time Complexity:
# n = number of nodes
# e = number of edges
# generateGraph: O(en), loop over each edge and search through graph hashmap
# DFS_hasPath: at most go through all e paths --> O(e)
# Overall: O(en + e) --> O(en)

# Space Complexity:
# generateGraph: return graph constructed: O(n), n nodes
# DFS_hasPath: N_visited at most n nodes --> O(n)

# x = set()
# y = set()
# x.union(y)
# z = 'a'
# x.add(z)
# if 'a' in x