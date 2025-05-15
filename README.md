# Graph Algorithms Project

This project implements various graph algorithms and utilities for working with directed graphs. It includes functionalities for graph creation, traversal, topological sorting, and exporting graphs to TikZ format for LaTeX.

---

## Features

### Graph Creation

- **Generate Graph (`--generate`)**: Creates a random directed acyclic graph (DAG) based on the number of vertices and saturation percentage.
- **User-Provided Graph (`--user-provided`)**: Allows the user to manually input the graph structure.

### Graph Representations

- **List Representation**: Displays the graph as an adjacency list.
- **Matrix Representation**: Displays the graph as an adjacency matrix.
- **Table Representation**: Displays the graph as a table of edges.

### Graph Traversal

- **Breadth-First Search (BFS)**: Traverses the graph in breadth-first order.
- **Depth-First Search (DFS)**: Traverses the graph in depth-first order.

### Topological Sorting

- **Kahn's Algorithm**: Performs topological sorting using Kahn's algorithm.
- **Tarjan's Algorithm**: Performs topological sorting using Tarjan's algorithm.

### Graph Export

- **TikZ Export**: Exports the graph to TikZ format for use in LaTeX documents.
