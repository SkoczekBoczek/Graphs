def printGraphList(graph):
    print("\nList graph representation:")
    for node, successors in enumerate(graph):
        if node == 0:
            continue
        print(f"{node}: {', '.join(map(str, successors))}")


def printGraphMatrix(graph):
    print("\nMatrix graph representation:")
    size = len(graph)
    print("   " + " ".join(map(str, range(1, size + 1))))
    for i, row in enumerate(graph):
        print(f"{i + 1}: " + " ".join(map(str, row)))


def printGraphTable(graph):
    print("\nTable graph representation:")
    print("From | To")
    print("-----|----")
    for edge in graph:
        print(f"{edge[0]:<4} | {edge[1]}")