def findEdges(fromNode, toNode, graph):
    if fromNode not in graph and toNode not in graph:
        print(f"Node {fromNode} and {toNode} does not exist.")
    elif fromNode not in graph:
        print(f"Node {fromNode} does not exist in the graph.")
        return
    elif toNode not in graph:
        print(f"Node {toNode} does not exist in the graph.")
        return
    elif toNode in graph[fromNode]:
        print(f"Edge from {fromNode} to {toNode} exists.")
    elif toNode not in graph[fromNode]:
        print(f"Edge from {fromNode} to {toNode} does not exist.")