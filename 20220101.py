from typing import List


def list_product(input_list: List[int]) -> int:
    """Given a list of integers, return the largest product
    that can be made by multiplying any three integers.
    You can assume the list has at least three integers.

    Args:
        input_list (List[int]): List of integers

    Returns:
        int: largest product.
    """

    '''
    If list has >5 integers we should check if the product
    of the smallest two is greater than the product of the
    2nd and 3rd largest.
    '''
    # sort ascending so that first element is smallest,
    # -1 element is largets
    input_list.sort()
    small_product = 0

    if len(input_list) >= 4:
        smallest = input_list[0]
        second_smallest = input_list[1]
        small_product = smallest * second_smallest

    largest = input_list[-1]
    second_largest = input_list[-2]
    third_largest = input_list[-3]

    if small_product > second_largest * third_largest:
        return small_product * largest
    else:
        return largest * second_largest * third_largest


if __name__ == '__main__':
    input_list = [-10, -10, 5, 2]
    assert list_product(input_list) == 500
