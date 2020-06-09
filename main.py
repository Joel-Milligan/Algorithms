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


def insertion_sort(array):
    """
    Returns a sorted version of array, using insertion sort.
    """
    sorted_array = array.copy()

    # Start after first element, as the first element is trivially sorted.
    for i in range(1, len(sorted_array)):
        for j in range(i, 0, -1):
            current_compare = sorted_array[j - 1]
            
            while current_compare > sorted_array[j]:
                temp = current_compare
                sorted_array[j - 1] = sorted_array[j]
                sorted_array[j] = temp

    return sorted_array


def run_insertion_sort():
    """
    Runs insertion sort with all required inputs.
    """
    example = input("Are you using the example list? ")

    if example != "y":
        list_filename = input("Input filename of list: ")
        unsorted_list = produce_list(list_filename)
    else:
        unsorted_list = produce_list("./examples/example-list.txt")

    print(f"Unsorted: {unsorted_list}")
    print(f"Sorted: {insertion_sort(unsorted_list)}")


def parse_matrix(matrix):
    """
    Takes an adjacency matrix representing a graph and 
    returns a matrix where all edges from a node to itself are 0.
    """
    new_matrix = matrix.copy()

    for i in range(len(matrix)):
        new_matrix[i][i] = 0
    
    return new_matrix


def produce_adjacency_matrix(filename):
    """
    Returns an adjacency matrix of a graph from given filename/path.
    """
    file_obj = open(filename)
    adjacency_matrix = []

    for line in file_obj.readlines():
        num_list = []
        string_list = line.split()
        for number in string_list:
            num_list.append(int(number))

        adjacency_matrix.append(num_list)

    return parse_matrix(adjacency_matrix)


def produce_list(filename):
    """
    Returns a list from given filename/path, in the format of CSV on a single line.
    """
    obj = open(filename)
    string_list = obj.readline().split(',')
    
    num_list = []
    for num in string_list:
        num_list.append(int(num))

    return num_list


def main():
    chosen = False
    while not chosen:
        algorithm = input("Which algorithm would you like to use? (help): ")
        
        if algorithm == "help":
            print("Enter 1 to run Djikstra's Algorithm.")
            print("Enter 2 to run Insertion Sort.")
            print("Enter help to get this message.")
        elif algorithm == "1":
            run_djikstra()
            chosen = True
        elif algorithm == "2":
            run_insertion_sort()
            chosen = True


if __name__ == "__main__":
    main()