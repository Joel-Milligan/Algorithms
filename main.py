import queue as q

def main():
    file_obj = open("test.txt")
    adjacency_matrix = []
    source_node = 0
    current_node = 0
    pQueue = q.PriorityQueue()

    for line in file_obj.readlines():
        num_list = []
        string_list = line.split()
        for number in string_list:
            num_list.append(int(number))

        adjacency_matrix.append(num_list)

    adjacency_matrix = parse_matrix(adjacency_matrix)

    distances = []
    for i in range(len(adjacency_matrix)):
        if i != source_node:
            distances.append(float('inf'))
        else:
            distances.append(0)
        pQueue.put((distances[i], i))

    while not pQueue.empty():
        current_node = pQueue.get()[1]

        for neighbour in range(len(adjacency_matrix[current_node])):
            if adjacency_matrix[current_node][neighbour] != 0:
                new_distance = distances[current_node] + adjacency_matrix[current_node][neighbour]
                if new_distance < distances[neighbour]:
                    distances[neighbour] = new_distance
                    pQueue.put((new_distance, neighbour))

    print(distances)

def parse_matrix(matrix):
    new_matrix = matrix.copy()

    for i in range(len(matrix)):
        new_matrix[i][i] = 0
    
    return new_matrix


if __name__ == "__main__":
    main()