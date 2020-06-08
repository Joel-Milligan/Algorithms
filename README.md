# Algorithms <!-- omit in toc -->
Repository of a collection of various algorithms.
- [1. Instructions for use](#1-instructions-for-use)
  - [1.0 Setting up the Program](#10-setting-up-the-program)
    - [1.0.1 Using own file to represent a graph](#101-using-own-file-to-represent-a-graph)
  - [1.1 Running the Program](#11-running-the-program)
    - [1.1.1 Dijkstra Instructions](#111-dijkstra-instructions)
- [2. Algorithms](#2-algorithms)
  - [2.1 Dijkstra's Algorithm](#21-dijkstras-algorithm)

## 1. Instructions for use

### 1.0 Setting up the Program
#### 1.0.1 Using own file to represent a graph
The expected file format to represent a graph (for dijkstra's algorithm for example) is an adjacency matrix represented in the file by integers seperated by spaces, where the integers represent the weight of the edge from [row index] node to [col index] node. 0 is used to represent no edge between nodes.

### 1.1 Running the Program
At first prompt, choose desired algorithm by inputing a number, which corrosponds to the order of algorithms in this README (ie. enter 1 to select the first algorithm). Enter help for a help message.

#### 1.1.1 Dijkstra Instructions
1. Input source node of the graph, indexed from 0 to (graph size - 1).
2. Input "y" (without quotes) if using the example graph provided, input anything else to specify a specific file name with an adjacency graph. 
3. Printed result is a list of distances from source node to all nodes in graph.

## 2. Algorithms
### 2.1 Dijkstra's Algorithm
Reads in an adjacency matrix from file specified or "example-graph.txt" if no file is given. 
Returns an array of shortest distances using Dijkstra's algorithm, from a given source node to all nodes in the graph, with the index being the number of the node.
