def bfs(graph, startNode, representation, targetNode=None):
    visited = set()
    queue = [startNode]
    traversalOrder = []

    while queue:
        currentNode = queue.pop(0)
        if currentNode not in visited:
            visited.add(currentNode)
            traversalOrder.append(currentNode)

            if targetNode is not None and currentNode == targetNode:
                return traversalOrder

            if representation == "list":
                neighbors = graph[currentNode]
            elif representation == "matrix":
                neighbors = [i + 1 for i, val in enumerate(graph[currentNode - 1]) if val == 1]
            elif representation == "table":
                neighbors = [to for fromNode, to in graph if fromNode == currentNode]
            else:
                raise ValueError("Unsupported graph representation")

            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)

    return traversalOrder