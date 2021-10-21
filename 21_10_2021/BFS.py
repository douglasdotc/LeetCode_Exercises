# BFS print of a graph, first in first out
graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

def BFS_iterative(graph:dict, source:str) -> None:
    queue = [source]
    while queue:
       curr = queue.pop(0)
       print(curr) 
       for neigh in graph[curr]:
           queue.append(neigh)

BFS_iterative(graph, 'a')
print('\n')

# travel through each edges --> Time complexity O(n+e)
# Space complexity O(n) if there are n nodes
# BFS can only be done iteratively