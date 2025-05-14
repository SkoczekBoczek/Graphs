def bfs(graph, startNode, targetNode=None):
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

            for neighbor in graph.get(currentNode, []):
                if neighbor not in visited:
                    queue.append(neighbor)

    return traversalOrder