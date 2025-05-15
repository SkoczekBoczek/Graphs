def tarjan(graph):
    temporaryMark = set()
    permanentMark = set()
    result = []

    def visit(node):
        if node in permanentMark:
            return
        if node in temporaryMark:
            raise Exception("Graph has at least one cycle")

        temporaryMark.add(node)

        for neighbor in graph.get(node, []):
            visit(neighbor)

        temporaryMark.remove(node)
        permanentMark.add(node)
        result.append(node)

    for node in graph:
        if node not in permanentMark:
            visit(node)

    result.reverse()
    return result
