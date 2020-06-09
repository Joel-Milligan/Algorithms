from utility import parse_matrix, produce_adjacency_matrix
from queue import PriorityQueue

def djikstra(source_node, matrix):
    """
    Given a weighted graph represented by an adjacency matrix, 
    return an array of shortest distances from source node 0 to all nodes in the graph.
    """
    current_node = source_node
    pQueue = PriorityQueue()
    distances = []

    for i in range(len(matrix)):
        if i != source_node:
            distances.append(float('inf'))
        else:
            distances.append(0)
        pQueue.put((distances[i], i))

    while not pQueue.empty():
        current_node = pQueue.get()[1]

        for neighbour in range(len(matrix[current_node])):
            if matrix[current_node][neighbour] != 0:
                new_distance = distances[current_node] + matrix[current_node][neighbour]
                if new_distance < distances[neighbour]:
                    distances[neighbour] = new_distance
                    pQueue.put((new_distance, neighbour))

    return distances


def run_djikstra():
    """
    Runs dijkstra's algorithm with all required inputs.
    """
    source = int(input("Input source node: "))
    example = input("Are you using the example graph? ")

    if example != "y":
        graph_filename = input("Input filename of graph: ")
        matrix = produce_adjacency_matrix(graph_filename)
    else:
        matrix = produce_adjacency_matrix("./examples/example-graph.txt")

    print(djikstra(source, matrix))