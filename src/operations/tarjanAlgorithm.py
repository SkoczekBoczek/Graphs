def tarjan(graph, representation):
    temporaryMark = set()
    permanentMark = set()
    result = []

    def visit(node):
        if node in permanentMark:
            return
        if node in temporaryMark:
            raise Exception("Graph has at least one cycle")

        temporaryMark.add(node)

        if representation == "list":
            neighbors = graph[node]
        elif representation == "matrix":
            neighbors = [j + 1 for j in range(len(graph[node - 1])) if graph[node - 1][j] == 1]
        elif representation == "table":
            neighbors = [toNode for fromNode, toNode in graph if fromNode == node]
        else:
            raise ValueError("Unsupported graph representation")

        for neighbor in neighbors:
            visit(neighbor)

        temporaryMark.remove(node)
        permanentMark.add(node)
        result.append(node)

    if representation == "list":
        nodes = range(1, len(graph))
    elif representation == "matrix":
        nodes = range(1, len(graph) + 1)
    elif representation == "table":
        nodes = set(node for edge in graph for node in edge)
    else:
        raise ValueError("Unsupported graph representation")

    for node in nodes:
        if node not in permanentMark:
            visit(node)

    result.reverse()
    return result