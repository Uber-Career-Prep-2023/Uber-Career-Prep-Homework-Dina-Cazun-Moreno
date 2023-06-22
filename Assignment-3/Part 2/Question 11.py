import queue

def vacationDestinations(destinations, origin, k):
    graph = {}
    for(u, v, w) in destinations:
        if u not in graph:
            graph[u] = {}
        if v not in graph:
            graph[v] = {}
        graph[u][v] = w
        graph[v][u] = w
    q = queue.Queue()
    q.put((origin, 0))
    visited = set()
    while not q.empty():
        (u, t) = q.get()
        if t > k:
            break
        visited.add(u)
        for v in graph[u]:
            if v not in visited:
                q.put((v, t + graph[u][v] + 1))
    return sorted(list(visited - set([origin])))

destinations = [("Boston", "New York", 4), ("New York", "Philadelphia.", 2), ("Boston", "Newport", 1.5), ("Washington, D.C.", "Harper's Ferry", 1), ("Boston", "Portland", 2.5), ("Philadelphia", "Washington, D.C.", 2.5)]
origin = "New York"
k = 5

print(vacationDestinations(destinations, origin, k))
#output: ['Boston', 'Philadelphia.']

print(vacationDestinations(destinations, origin, k)) #when k = 7
#output: ['Boston', 'Philadelphia.']

print(vacationDestinations(destinations, origin, k)) #when k = 8
#output: ['Boston', 'Newport', 'Philadelphia.']

