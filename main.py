def sorting_algs():
    """
    Function to run all sorting algorithms from.
    """
    chosen = False
    while not chosen:
        algorithm = input("Which algorithm would you like to use? (help): ")
        
        if algorithm == "help":
            print("Enter 1 to run an insertion sort.")
            print("Enter help to get this message.")
        elif algorithm == "1":
            from sorting import run_insertion_sort, insertion_sort
            run_insertion_sort()
            chosen = True


def shortest_path_algs():
    """
    Function to run all shortest path algorithms from.
    """
    chosen = False
    while not chosen:
        algorithm = input("Which algorithm would you like to use? (help): ")
        
        if algorithm == "help":
            print("Enter 1 to run djikstra's algorithm.")
            print("Enter help to get this message.")
        elif algorithm == "1":
            from shortest_path import run_djikstra, djikstra
            run_djikstra()
            chosen = True


def main():
    chosen = False
    while not chosen:
        category = input("Which category of algorithm would you like to use? (help): ")
        
        if category == "help":
            print("Enter 1 to run a sorting algorithm.")
            print("Enter 2 to run a shortest path algorithm.")
            print("Enter help to get this message.")
        elif category == "1":
            sorting_algs()
            chosen = True
        elif category == "2":
            shortest_path_algs()
            chosen = True


if __name__ == "__main__":
    main()