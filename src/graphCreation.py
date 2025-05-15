import sys
import re
import random

def cleanInput(raw_data):
    data = []
    if isinstance(raw_data, list):
        input_str = ' '.join(raw_data)
    else:
        input_str = raw_data
    
    numbers = re.split(r'[,\s]+', input_str.replace(',', ' ').strip())
    
    for num in numbers:
        if num:
            try:
                data.append(int(num))
            except ValueError:
                print(f"'{num}' is invalid ")
    
    return data

def createGraph():
    if len(sys.argv) < 2 or sys.argv[1] not in ["--generate", "--user-provided"]:
        print("Usage: python3 src/main.py --generate")
        print("Or:    python3 src/main.py --user-provided")
        sys.exit(1)
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

    graph = {}

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
        
        maxEdges = vertexes * (vertexes - 1) // 2  # Maksymalna liczba krawędzi w DAG
        targetEdges = (saturation * maxEdges) // 100  # Docelowa liczba krawędzi

        graph = {i: [] for i in range(1, vertexes + 1)}

        for i in range(1, vertexes):
            graph[i].append(i + 1)

        # Możliwe krawędzie do dodania
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

    elif sys.argv[1] == "--user-provided":
        for i in range(1, vertexes + 1):
            print("Enter successors for vertex", i)
            while True:
                successorsInput = input(f"{i}>").strip()
                successors = cleanInput(successorsInput)

                cleanedSuccessors = []
                errorsFound = False
                for x in successors:
                    if x == i:
                        print("Self loop, try again")
                        errorsFound = True
                    elif x < 0 or x > vertexes:
                        print(f"'{x}' is out of range, try again")
                        errorsFound = True
                    elif x in cleanedSuccessors:
                        print(f"'{x}' is a duplicate, try again")
                        errorsFound = True
                    else: 
                        cleanedSuccessors.append(x)
                
                if errorsFound:
                    continue

                graph[i] = successors
                break

    return graph