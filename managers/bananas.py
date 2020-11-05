from managers.heap_sort import heap_sort


def find_bananas_per_hour(piles, hours):
    """
    Returns suitable bananas per hour amount
    >>> find_bananas_per_hour([1, 1, 1, 1], 4)
    1
    >>> find_bananas_per_hour([3, 6, 7, 11], 8)
    4
    >>> find_bananas_per_hour([30, 11, 23, 4, 20], 5)
    30
    >>> find_bananas_per_hour([30, 11, 23, 4, 20], 6)
    23
    >>> find_bananas_per_hour([30, 11, 14, 4, 13], 6)
    15
    >>> find_bananas_per_hour([3, 6, 7, 11], 80)
    1
    """
    heapified_piles = heap_sort(piles)
    max_value = heapified_piles[0]
    if max_value == 1:
        return max_value
    while True:
        piles_copy = piles[:]
        elapsed_time = 0
        array_index = 0
        if max_value * len(piles_copy) < hours:
            return 1
        while piles_copy[len(piles) - 1] > 0:
            piles_copy[array_index] -= max_value
            if piles_copy[array_index] <= 0:
                array_index += 1
            elapsed_time += 1

        if elapsed_time <= hours:
            max_value -= 1
        else:
            break
    return max_value+1


def main():
    import doctest

    doctest.testmod(verbose=True)


if __name__ == '__main__':
    main()
