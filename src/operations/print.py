def printGraphList(graph):
    print("\nList graph representation:")
    for node, successors in graph.items():
        print(f"{node}: {", ".join(map(str, successors))}")


def printGraphMatrix(graph):
    print("\nMatrix graph representation:")
    nodes = sorted(graph.keys())
    size = len(nodes)
    matrix = [[0] * size for _ in range(size)]
    for node, successors in graph.items():
        for successor in successors:
            matrix[node - 1][successor - 1] = 1
    print("   " + " ".join(map(str, nodes)))
    for i, row in enumerate(matrix):
        print(f"{nodes[i]}: " + " ".join(map(str, row)))

def printGraphTable(graph):
    print("\nTable graph representation:")
    print("From | To")
    print("-----|----")
    printedEdges = []
    for node, successors in graph.items():
        for successor in successors:
            usedEdge = (node, successor)
            reverseEdge = (successor, node)
            if usedEdge not in printedEdges and reverseEdge not in printedEdges:
                print(f"{node:<4} | {successor}")
                printedEdges.append(usedEdge)