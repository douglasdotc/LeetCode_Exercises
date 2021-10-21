graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}

def DFS_hasPath(graph:dict, src:str, dst:str) -> bool:
    if src == dst:
        return True
    
    for neigh in graph[src]:
        if DFS_hasPath(graph, neigh, dst):
            return True
    return False

def BFS_hasPath(graph:dict, src:str, dst:str) -> bool:
    queue = [src]
    while queue:
        curr = queue.pop(0)
        if curr == dst:
            return True 
        
        for neigh in graph[curr]:
            queue.append(neigh)
    
    return False

print(DFS_hasPath(graph, 'f', 'k'))
print(BFS_hasPath(graph, 'f', 'k'))
print(DFS_hasPath(graph, 'h', 'k'))
print(BFS_hasPath(graph, 'h', 'k'))

# Directed graph
