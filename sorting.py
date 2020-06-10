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


def merge_sort(array):
    """
    Returns a sorted version of array, using insertion sort.
    """
    if len(array) == 1:
        return array
    else:
        halfway_index = len(array) //2        
        small = merge_sort(array[:halfway_index])
        large = merge_sort(array[halfway_index:])
        sorted = merge(large, small)
        return sorted


def merge(large_array, small_array):
    """
    Merges 2 given arrays (large and small indicate length) by 
    combining them in ascending order and returning the one big array.
    """
    merged = []
    small_index = 0
    large_index = 0
    merging = True

    while merging:
        if large_index + 1 > len(large_array):
            merged += small_array[small_index:]
            merging = False
        elif small_index + 1 > len(small_array):
            merged += large_array[large_index:]
            merging = False
        elif large_array[large_index] > small_array[small_index]:
            merged.append(small_array[small_index])
            small_index += 1
        else:
            merged.append(large_array[large_index])
            large_index += 1

    return merged


def quick_sort(array, low, high):
    """
    Returns a sorted version of array, using quick sort.
    """
    if low < high:
        partition_index = partition(array, low, high)
        quick_sort(array, low, partition_index - 1)
        quick_sort(array, partition_index + 1, high)

    return array


def partition(array, low, high):
    """
    Returns the index of the sorted pivot (which is the array indexed at the high index), 
    with everything prior in the list being less then pivot and everything after being greater then pivot.
    """
    pivot = array[high]

    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1

            temp = array[j]
            array[j] = array[i]
            array[i] = temp

    temp = array[high]
    array[high] = array[i + 1]
    array[i + 1] = temp
    return i + 1


def run_sort(algorithm):
    """
    Runs specified sort with all required inputs.
    """
    example = input("Are you using the example list? ")

    if example != "y":
        list_filename = input("Input filename of list: ")
        unsorted_list = produce_list(list_filename)
    else:
        unsorted_list = produce_list("./examples/example-list.txt")

    print(f"Unsorted: {unsorted_list}")

    if algorithm == "insertion":
        print(f"Sorted: {insertion_sort(unsorted_list)}")
    elif algorithm == "merge":
        print(f"Sorted: {merge_sort(unsorted_list)}")
    elif algorithm == "quick":
        print(f"Sorted: {quick_sort(unsorted_list, 0, len(unsorted_list) - 1)}")