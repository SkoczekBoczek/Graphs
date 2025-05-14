def printGraph(graph):
    print("\nGraph representation:")
    for node, successors in graph.items():
        print(f"{node} -> {successors}")