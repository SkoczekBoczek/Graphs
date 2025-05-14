import sys
from graphCreation import createGraph
from operations.print import printGraphList, printGraphMatrix, printGraphTable
from operations.find import findEdges
from operations.bfs import bfs
from operations.dfs import dfs
from operations.TickzpictureExport import exportToTikz

def printMenu():
    print("========================================")
    print("{}        {}".format("Help", "Shows this menu"))
    print("{}        {}".format("Exit", "Exits the program (or ctrl+D)"))
    print("{}       {}".format("Print", "Prints the graph"))
    print("{}        {}".format("Find", "Finding the edges of a graph"))
    print("{}         {}".format("BFS", "Performs BFS from start node"))
    print("{}         {}".format("DFS", "Performs DFS from start node"))
    print("========================================")

def interactiveMode(graph):
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
                print("Choose representation: 'matrix', 'list', or 'table'")
                representation = input("type> ").strip().lower()
                if representation == "matrix":
                    printGraphMatrix(graph)
                elif representation == "list":
                    printGraphList(graph)
                elif representation == "table":
                    printGraphTable(graph)
                else:
                    print(f"Unknown representation '{representation}'")
            elif command == "find":
                try:
                    fromNode = int(input("from> "))
                    toNode = int(input("to> "))
                    findEdges(fromNode, toNode, graph)
                except ValueError:
                    print("Please enter valid node numbers")
            elif command == "bfs":
                try:
                    startNode = int(input("start> "))
                    transversalOrder = bfs(graph, startNode)
                    print(f"BFS traversal order:", " -> ".join(map(str, transversalOrder)))
                except ValueError:
                    print("Please enter a valid start node.")
            elif command == "dfs":
                try:
                    startNode = int(input("start> "))
                    transversalOrder = dfs(graph, startNode)
                    print(f"DFS traversal order:", " -> ".join(map(str, transversalOrder)))
                except ValueError:
                    print("Please enter a valid start node.")
            elif command == "export":
                filename = input("filename> ")
                exportToTikz(graph, filename)
            else:
                print(f"Unknown command '{command}'")
        except EOFError:
            print("\nExiting...")
            sys.exit(0)
        except KeyboardInterrupt:
            print("\nExiting...")
            sys.exit(0)

if __name__ == "__main__":
    graph = createGraph()
    interactiveMode(graph)