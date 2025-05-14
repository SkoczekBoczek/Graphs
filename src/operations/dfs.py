def dfs(graph, startNode, visited=None, traversalOrder=None):
    if visited is None:
        visited = set()
    if traversalOrder is None:
        traversalOrder = []

    visited.add(startNode)
    traversalOrder.append(startNode)

    for neighbor in graph.get(startNode, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited, traversalOrder)

    return traversalOrder