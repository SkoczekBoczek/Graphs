def dfs(graph, startNode, representation, visited=None, traversalOrder=None):
    if visited is None:
        visited = set()
    if traversalOrder is None:
        traversalOrder = []

    visited.add(startNode)
    traversalOrder.append(startNode)

    if representation == "list":
        neighbors = graph[startNode]
    elif representation == "matrix":
        neighbors = [i + 1 for i, val in enumerate(graph[startNode - 1]) if val == 1]
    elif representation == "table":
        neighbors = [to for fromNode, to in graph if fromNode == startNode]
    else:
        raise ValueError("Unsupported graph representation")

    for neighbor in neighbors:
        if neighbor not in visited:
            dfs(graph, neighbor, representation, visited, traversalOrder)

    return traversalOrder