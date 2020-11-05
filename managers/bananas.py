from managers.utilities import bananas_per_hour_check


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
    higher_limit = max(piles)
    lower_limit = min(piles)
    if higher_limit * len(piles) < hours or higher_limit == 1:
        return 1
    while lower_limit < higher_limit:
        bananas_per_hour = (lower_limit + higher_limit) // 2
        if bananas_per_hour_check(piles, hours, bananas_per_hour):
            higher_limit = bananas_per_hour
        else:
            lower_limit = bananas_per_hour + 1
    return higher_limit


def main():
    import doctest

    doctest.testmod(verbose=True)


if __name__ == '__main__':
    main()
