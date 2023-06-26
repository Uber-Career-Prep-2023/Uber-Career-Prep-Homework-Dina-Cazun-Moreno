#Question 6: Road Networks

def roadNetworks(towns, roads):
    def dfs(node, visited, graph):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, visited, graph)
    
    graph = {town: set() for town in towns}
    for road in roads:
        graph[road[0]].add(road[1])
        graph[road[1]].add(road[0])

    visited = set()
    count = 0
    for town in towns:
        if town not in visited:
            dfs(town, visited, graph)
            count += 1

    return count

print(roadNetworks(["Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth", "Glacier Bay", "Fairbanks", "McCarthy", "Copper Center", "Healy"], 
[("Anchorage", "Homer"), ("Glacier Bay", "Gustavus"), ("Copper Center", "McCarthy"), ("Anchorage", "Copper Center"), ("Copper Center", "Fairbanks"), ("Healy", "Fairbanks"), ("Healy", "Anchorage")]))
#output: KeyError: 'Anchorage'
