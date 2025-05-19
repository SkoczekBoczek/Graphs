import math

def exportToTikz(graph, representation, filename="graph.tex"):
    header = [
        "\\begin{tikzpicture}[",
        "    >={Stealth[black]},",
        "    node distance=2cm,",
        "    every node/.style={fill=red!50,circle,draw=black,minimum size=8mm},",
        "    every edge/.style={draw=black,thick},",
        "    scale=0.8, transform shape",
        "]"
    ]
    
    footer = [
        "\\end{tikzpicture}"
    ]

    try:
        with open(filename, "w") as file:
            file.write("\n".join(header) + "\n\n")
            
            if representation == "list":
                numNodes = len(graph) - 1
                nodes = range(1, len(graph))
            elif representation == "matrix":
                numNodes = len(graph)
                nodes = range(1, len(graph) + 1)
            elif representation == "table":
                nodes = set(node for edge in graph for node in edge)
                numNodes = len(nodes)
            else:
                raise ValueError("Unsupported graph representation")

            if numNodes == 0:
                raise ValueError("Graph is empty")
                
            radius = max(4, math.sqrt(numNodes) * 1.5)
            center = (radius, radius)
            angleStep = 360 / numNodes
            
            positions = {}
            for i, node in enumerate(sorted(nodes)):
                angle = math.radians(i * angleStep)
                x = center[0] + radius * math.cos(angle)
                y = center[1] + radius * math.sin(angle)
                positions[node] = (x, y)
                file.write(f"    \\node ({node}) at ({x:.2f},{y:.2f}) {{{node}}};\n")
            
            file.write("\n")
            
            if representation == "list":
                for node, successors in enumerate(graph):
                    if node == 0:
                        continue
                    for successor in successors:
                        file.write(f"    \\path [->] ({node}) edge ({successor});\n")
            elif representation == "matrix":
                for i in range(len(graph)):
                    for j in range(len(graph[i])):
                        if graph[i][j] == 1:
                            file.write(f"    \\path [->] ({i + 1}) edge ({j + 1});\n")
            elif representation == "table":
                for fromNode, toNode in graph:
                    file.write(f"    \\path [->] ({fromNode}) edge ({toNode});\n")
            else:
                raise ValueError("Unsupported graph representation")
            
            file.write("\n" + "\n".join(footer) + "\n")
            
        print(f"Successfully exported to {filename}")
        return True
        
    except Exception as e:
        print(f"Export error: {str(e)}")
        return False