# DFS print of a graph
graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

def DFS_iterative(graph:dict, source:str) -> None:
    stack = [source]

    while stack:
        curr = stack.pop()
        print(curr)

        for neigh in graph[curr]:
            stack.append(neigh)

def DFS_recurrsive(graph:dict, source:str) -> None:
    print(source)
    for neigh in graph[source]:
        DFS_recurrsive(graph, neigh)

DFS_iterative(graph, 'a') # acebdf OR abdfce
print('\n')
DFS_recurrsive(graph, 'a')

# travel through each edges --> Time complexity O(n+e)
# Space complexity O(n) if there are n nodes
# iterative approach space complexity O(1)???