"""
    Heapifies given list

    >>> heap_sort([3, 6, 7, 11])[0]
    11
    >>> heap_sort([30, 11, 23, 4, 20])[0]
    30
    >>> heap_sort([13, 16, 17, 45])[0]
    45

"""


def heapify(given_list, heap_size, root_index):
    largest_element = root_index
    left_element = 2 * root_index + 1
    right_element = 2 * root_index + 2

    if left_element < heap_size and given_list[largest_element] < given_list[left_element]:
        largest_element = left_element

    if right_element < heap_size and given_list[largest_element] < given_list[right_element]:
        largest_element = right_element

    if largest_element != root_index:
        given_list[root_index], given_list[largest_element] = given_list[largest_element], given_list[root_index]
        heapify(given_list, heap_size, largest_element)


def heap_sort(given_list):
    heap_size = len(given_list)

    for i in range(heap_size // 2, -1, -1):
        heapify(given_list, heap_size, i)
    return given_list


def main():
    import doctest

    doctest.testmod(verbose=True)


if __name__ == '__main__':
    main()
