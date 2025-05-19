import sys
from graphCreation import createGraph
from operations.print import printGraphList, printGraphMatrix, printGraphTable
from operations.find import findEdges
from operations.bfs import bfs
from operations.dfs import dfs
from operations.TickzpictureExport import exportToTikz
from operations.kahnAlgorithm import kahn
from operations.tarjanAlgorithm import tarjan


def printMenu():
    print("========================================")
    print("{}        {}".format("Help", "Shows this menu"))
    print("{}        {}".format("Exit", "Exits the program (or ctrl+D)"))
    print("{}       {}".format("Print", "Prints the graph"))
    print("{}        {}".format("Find", "Finding the edges of a graph"))
    print("{}         {}".format("BFS", "Performs BFS from start node"))
    print("{}         {}".format("DFS", "Performs DFS from start node"))
    print("{}        {}".format("Kahn", "Performs topological sorting using Kahn's algorithm"))
    print("{}      {}".format("Tarjan", "Performs topological sorting using Tarjan's algorithm"))
    print("========================================")

def interactiveMode(graph, representation):
    print("\nInteractive mode (type 'help' for commands.)")
    while True:
        try:
            command = input("action> ").strip().lower()
            if not command:
                continue
            if command == "help":
                printMenu()
            elif command == "exit":
                print("\nExiting...")
                sys.exit(0)
            elif command == "print":
                if representation == "list":
                    printGraphList(graph)
                elif representation == "matrix":
                    printGraphMatrix(graph)
                elif representation == "table":
                    printGraphTable(graph)
                else:
                    print(f"Unknown representation '{representation}'")
            elif command == "find":
                try:
                    fromNode = int(input("from> "))
                    toNode = int(input("to> "))
                    findEdges(fromNode, toNode, graph, representation)
                except ValueError:
                    print("Please enter valid node numbers.")
            elif command == "bfs":
                try:
                    startNode = int(input("start> "))
                    transversalOrder = bfs(graph, startNode, representation)
                    print(f"BFS traversal order:", " -> ".join(map(str, transversalOrder)))
                except ValueError:
                    print("Please enter a valid start node.")
            elif command == "dfs":
                try:
                    startNode = int(input("start> "))
                    transversalOrder = dfs(graph, startNode, representation)
                    print(f"DFS traversal order:", " -> ".join(map(str, transversalOrder)))
                except ValueError:
                    print("Please enter a valid start node.")
            elif command == "export":
                filename = input("filename> ")
                exportToTikz(graph, representation, filename)
            elif command == "kahn":
                try:
                    order = kahn(graph, representation)
                    print("Topological order (Kahn):", " -> ".join(map(str, order)))
                except ValueError as e:
                    print("Error:", e)
            elif command == "tarjan":
                try:
                    order = tarjan(graph, representation)
                    print("Topological order (Tarjan):", " -> ".join(map(str, order)))
                except Exception as e:
                    print("Error:", e)
            else:
                print(f"Unknown command '{command}'")
        except EOFError:
            print("\nExiting...")
            sys.exit(0)
        except KeyboardInterrupt:
            print("\nExiting...")
            sys.exit(0)

if __name__ == "__main__":
    graph, representation = createGraph()
    interactiveMode(graph, representation)