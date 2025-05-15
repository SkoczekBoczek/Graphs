def kahn(graph):
    inDegree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            inDegree[neighbor] += 1

    queue = [node for node in graph if inDegree[node] == 0]
    topologicalOrder = []

    while queue:
        n = queue.pop(0)
        topologicalOrder.append(n)

        for m in graph.get(n, []):
            inDegree[m] -= 1
            if inDegree[m] == 0:
                queue.append(m)

    if len(topologicalOrder) != len(graph):
        raise ValueError("Graph has at least one cycle")
    return topologicalOrder