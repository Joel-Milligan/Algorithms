# Algorithms <!-- omit in toc -->
Repository of a collection of various algorithms.
- [1. Instructions for use](#1-instructions-for-use)
  - [1.0 Setting up the Program](#10-setting-up-the-program)
    - [1.0.1 Using own file to represent a graph](#101-using-own-file-to-represent-a-graph)
    - [1.0.2 Using own file to represent a list](#102-using-own-file-to-represent-a-list)
  - [1.1 Running the Program](#11-running-the-program)
- [2. Algorithms](#2-algorithms)
  - [2.1 Sorting Algorithms](#21-sorting-algorithms)
    - [2.1.1 Insertion Sort](#211-insertion-sort)
    - [2.1.2 Merge Sort](#212-merge-sort)
    - [2.1.3 Quick Sort](#213-quick-sort)
  - [2.2 Shortest Path Algorithms](#22-shortest-path-algorithms)
    - [2.2.1 Dijkstra's Algorithm](#221-dijkstras-algorithm)

## 1. Instructions for use
### 1.0 Setting up the Program
#### 1.0.1 Using own file to represent a graph
The expected file format to represent a graph (for dijkstra's algorithm for example) is an adjacency matrix represented in the file by integers seperated by spaces, where the integers represent the weight of the edge from [row index] node to [col index] node. 0 is used to represent no edge between nodes.

#### 1.0.2 Using own file to represent a list
Expected file format is a single line CSV of integers.

### 1.1 Running the Program
At first prompt, choose desired algorithm category by inputing a number, which corrosponds to the order of algorithm categories in this README (ie. enter 1 to select the first algorithm). Enter help for a help message.

Then select the specific algorithm in the same way as the category.

## 2. Algorithms
### 2.1 Sorting Algorithms
#### 2.1.1 Insertion Sort
1. Input "y" (without quotes) if using the example list provided, input anything else to specify a specific file name with an unsorted list. Reads in an unsorted list from file specified or "example-list.txt" if no file is given.
2. Printed result is the initial unsorted list of integers, and then the sorted list.

#### 2.1.2 Merge Sort
1. Input "y" (without quotes) if using the example list provided, input anything else to specify a specific file name with an unsorted list. Reads in an unsorted list from file specified or "example-list.txt" if no file is given.
2. Printed result is the initial unsorted list of integers, and then the sorted list.

#### 2.1.3 Quick Sort
1. Input "y" (without quotes) if using the example list provided, input anything else to specify a specific file name with an unsorted list. Reads in an unsorted list from file specified or "example-list.txt" if no file is given.
2. Printed result is the initial unsorted list of integers, and then the sorted list.

### 2.2 Shortest Path Algorithms
#### 2.2.1 Dijkstra's Algorithm
1. Input source node of the graph, indexed from 0 to (graph size - 1).
2. Input "y" (without quotes) if using the example graph provided, input anything else to specify a specific file name with an adjacency graph. Reads in an adjacency matrix from file specified or "example-graph.txt" if no file is given. 
3. Printed result is a list of distances from source node to all nodes in graph.