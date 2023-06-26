#Question 1: Build an Adjacency List/Set Representation of a Graph

from collections import defaultdict

def adjacencySet(edges):
    graph = defaultdict(set)

    for edge in edges:
        graph[edge[0]].add(edge[1])
    
    return graph

def dfs(target, graph):
    visited = set()
    stack = [target]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(set(graph[node]) - visited)
    return visited

def bfs(target, graph):
    visited = set()
    queue = [target]
    
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            queue.extend(set(graph[node]) - visited)
    return visited

def topologicalSort(graph):
    visited = set()
    stack = []
    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)
    for node in graph:
        if node not in visited:
            dfs(node)
    return stack[::-1]

if __name__ == '__main__':
    graph = [(1, 2), (2, 3), (1, 3), (3, 2), (2, 0)]
    print("Following is adjacency set: ")
    print(adjacencySet(graph))

    print(bfs(4, graph)) #{1, 2, 3, 4, 5}
    print(dfs(4, graph)) #{1, 2, 3, 4, 5}
    print(topologicalSort(graph)) #{list indices must be integers or slices, not tuples}
    #Perhaps missing target value when calling dfs inside topologicalSort
