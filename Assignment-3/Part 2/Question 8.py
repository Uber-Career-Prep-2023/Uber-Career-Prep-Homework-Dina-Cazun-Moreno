from collections import deque

def alternatingPath(graph, origin, destination):
    queue = deque([origin, 0, None])
    visited = set()
    while queue:
        node, length, color = queue.popleft()
        if node == destination:
            return length
        visited.add((node, color))
        for neighbor, edge_color in graph[node]:
            if (neighbor, edge_color) not in visited and edge_color != color:
                queue.append((neighbor, length+1, edge_color))
    return -1

graph = {
    'A': [('B', 'blue'), ('C', 'red'), ('D', 'red')],
    'B': [('D', 'blue'), ('E', 'blue')],
    'C': [('B', 'red')],
    'D': [('C', 'blue'), ('E', 'red')],
    'E': [('C', 'red')]
}

print(alternatingPath(graph, 'A', 'E'))
#output: ValueError: not enough values to unpack (expected 3, got 1)
