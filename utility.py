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