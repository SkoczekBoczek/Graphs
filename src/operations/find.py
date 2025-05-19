def findEdges(fromNode, toNode, graph, representation):
    if representation == "list":
        if fromNode >= len(graph) or fromNode < 1:
            print(f"Node {fromNode} does not exist in the graph.")
            return
        if toNode >= len(graph) or toNode < 1:
            print(f"Node {toNode} does not exist in the graph.")
            return
        if toNode in graph[fromNode]:
            print(f"Edge from {fromNode} to {toNode} exists.")
        else:
            print(f"Edge from {fromNode} to {toNode} does not exist.")

    elif representation == "matrix":
        if fromNode > len(graph) or fromNode < 1:
            print(f"Node {fromNode} does not exist in the graph.")
            return
        if toNode > len(graph) or toNode < 1:
            print(f"Node {toNode} does not exist in the graph.")
            return
        if graph[fromNode - 1][toNode - 1] == 1:
            print(f"Edge from {fromNode} to {toNode} exists.")
        else:
            print(f"Edge from {fromNode} to {toNode} does not exist.")

    elif representation == "table":
        if not any(edge[0] == fromNode or edge[1] == toNode for edge in graph):
            print(f"Node {fromNode} or {toNode} does not exist in the graph.")
            return
        if (fromNode, toNode) in graph:
            print(f"Edge from {fromNode} to {toNode} exists.")
        else:
            print(f"Edge from {fromNode} to {toNode} does not exist.")

    else:
        print(f"Unsupported graph representation: {representation}")