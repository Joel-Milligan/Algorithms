from utility import produce_list

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