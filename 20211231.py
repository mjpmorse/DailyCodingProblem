def consecutive_ones(input: int) -> int:
    """Given an integer n, return
    the length of the longest consecutive run of 1s
    in its binary representation.

    Args:
        input (int): input number

    Returns:
        int: longest consecutive run of ones on binary rep
    """

    # we do not care about the 0b in 0bxxxxx
    binary_rep = bin(input)[2:]
    # get list of 1 split on 0
    binary_rep = binary_rep.split('0')
    lengths = [len(x) for x in binary_rep]

    return max(lengths)


if __name__ == '__main__':
    assert consecutive_ones(156) == 3
