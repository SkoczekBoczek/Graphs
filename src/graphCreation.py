import sys
import re
import random

def cleanInput(raw_data, currentNode, vertexes):
    cleanedSuccessors = []
    errors = []

    if isinstance(raw_data, list):
        input_str = ' '.join(raw_data)
    else:
        input_str = raw_data

    numbers = re.split(r'[,\s]+', input_str.replace(',', ' ').strip())

    for num in numbers:
        if num:
            try:
                x = int(num)
                if x == currentNode:
                    errors.append("Self loop detected.")
                elif x < 1 or x > vertexes:
                    errors.append(f"'{x}' is out of range.")
                elif x in cleanedSuccessors:
                    errors.append(f"'{x}' is a duplicate.")
                else:
                    cleanedSuccessors.append(x)
            except ValueError:
                errors.append(f"'{num}' is invalid.")

    if errors:
        print("Errors detected:")
        for error in set(errors):
            print(f"{error}")
        return None

    return cleanedSuccessors

def createGraph():
    if len(sys.argv) < 2 or sys.argv[1] not in ["--generate", "--user-provided"]:
        print("Usage: python3 src/main.py --generate")
        print("Or:    python3 src/main.py --user-provided")
        sys.exit(1)

    print("Choose graph representation: 'list', 'matrix', or 'table'")
    while True:
        representation = input("representation> ").strip().lower()
        if representation not in ["list", "matrix", "table"]:
            print("Invalid representation. Please choose 'list', 'matrix', or 'table'.")
        else:
            break

    print("Enter number of vertexes!")
    while True:
        try:
            vertexes = int(input("nodes> "))
            if vertexes < 1:
                print(f"'{vertexes}' is out of range")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    if sys.argv[1] == "--generate":
        while True:
            try:
                saturation = int(input("saturation> "))
                if saturation < 0 or saturation > 100:
                    print(f"'{saturation}' is out of range")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        maxEdges = vertexes * (vertexes - 1) // 2
        targetEdges = (saturation * maxEdges) // 100

        if representation == "list":
            graph = [[] for _ in range(vertexes + 1)]
            for i in range(1, vertexes):
                graph[i].append(i + 1)

            allPossibleEdges = []
            for i in range(1, vertexes + 1):
                for j in range(i + 1, vertexes + 1):
                    if j not in graph[i]:
                        allPossibleEdges.append((i, j))

            random.shuffle(allPossibleEdges)
            edgesToAdd = min(targetEdges - (vertexes - 1), len(allPossibleEdges))
            for i in range(edgesToAdd):
                u, v = allPossibleEdges[i]
                graph[u].append(v)

        elif representation == "matrix":
            graph = [[0] * vertexes for _ in range(vertexes)]
            for i in range(vertexes - 1):
                graph[i][i + 1] = 1

            allPossibleEdges = []
            for i in range(vertexes):
                for j in range(i + 1, vertexes):
                    if graph[i][j] == 0:
                        allPossibleEdges.append((i, j))

            random.shuffle(allPossibleEdges)
            edgesToAdd = min(targetEdges - (vertexes - 1), len(allPossibleEdges))
            for i in range(edgesToAdd):
                u, v = allPossibleEdges[i]
                graph[u][v] = 1

        elif representation == "table":
            graph = []
            for i in range(1, vertexes):
                graph.append((i, i + 1))

            allPossibleEdges = []
            for i in range(1, vertexes + 1):
                for j in range(i + 1, vertexes + 1):
                    if (i, j) not in graph:
                        allPossibleEdges.append((i, j))

            random.shuffle(allPossibleEdges)
            edgesToAdd = min(targetEdges - (vertexes - 1), len(allPossibleEdges))
            for i in range(edgesToAdd):
                graph.append(allPossibleEdges[i])

    elif sys.argv[1] == "--user-provided":
        if representation == "list":
            graph = [[] for _ in range(vertexes + 1)]
            for i in range(1, vertexes + 1):
                print(f"Enter successors for vertex {i}")
                while True:
                    successorsInput = input(f"{i}> ").strip()
                    successors = cleanInput(successorsInput, i, vertexes)
                    if successors is not None:
                        graph[i] = successors
                        break

        elif representation == "matrix":
            graph = [[0] * vertexes for _ in range(vertexes)]
            for i in range(vertexes):
                print(f"Enter successors for vertex {i + 1}")
                while True:
                    successorsInput = input(f"{i + 1}> ").strip()
                    successors = cleanInput(successorsInput, i + 1, vertexes)
                    if successors is not None:
                        for x in successors:
                            graph[i][x - 1] = 1
                        break

        elif representation == "table":
            graph = []
            for i in range(1, vertexes + 1):
                print(f"Enter successors for vertex {i}")
                while True:
                    successorsInput = input(f"{i}> ").strip()
                    successors = cleanInput(successorsInput, i, vertexes)
                    if successors is not None:
                        for x in successors:
                            graph.append((i, x))
                        break
    return graph, representation