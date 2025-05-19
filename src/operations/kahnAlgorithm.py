def kahn(graph, representation):
    if representation == "list":
        inDegree = {node: 0 for node in range(1, len(graph))}
        for node in range(1, len(graph)):
            for neighbor in graph[node]:
                inDegree[neighbor] += 1
    elif representation == "matrix":
        inDegree = {node + 1: 0 for node in range(len(graph))}
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                if graph[i][j] == 1:
                    inDegree[j + 1] += 1
    elif representation == "table":
        inDegree = {}
        for edge in graph:
            fromNode, toNode = edge
            inDegree[toNode] = inDegree.get(toNode, 0) + 1
            if fromNode not in inDegree:
                inDegree[fromNode] = 0
    else:
        raise ValueError("Unsupported graph representation")

    queue = [node for node in inDegree if inDegree[node] == 0]
    topologicalOrder = []

    while queue:
        n = queue.pop(0)
        topologicalOrder.append(n)

        if representation == "list":
            neighbors = graph[n]
        elif representation == "matrix":
            neighbors = [j + 1 for j in range(len(graph[n - 1])) if graph[n - 1][j] == 1]
        elif representation == "table":
            neighbors = [toNode for fromNode, toNode in graph if fromNode == n]
        else:
            raise ValueError("Unsupported graph representation")

        for m in neighbors:
            inDegree[m] -= 1
            if inDegree[m] == 0:
                queue.append(m)

    if len(topologicalOrder) != len(inDegree):
        raise ValueError("Graph has at least one cycle")

    return topologicalOrder