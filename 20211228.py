from typing import List


def justify_txt(str_list: List[str], k: int) -> List[str]:
    """ Given a sequence of words and an integer line length k,
    return a list of strings which represents each line,
    fully justified. More specifically,
    you should have as many words as possible in each line.
    There should be at least one space between each word.
    Pad extra spaces when necessary so that each line has
    exactly length k.
    Spaces should be distributed as equally as possible,
    with the extra spaces, if any, distributed starting from the left.

    Args:
        str_list (List[str]): List of words to be justified
        k (int): number of characters in each line of return

    Returns:
        List[str]: List of words strings each of length k.
    """

    # first solution is easy
    return_list = [f'{str_list[0]}']
    word_index = [len(return_list[-1])]
    for n, word in enumerate(str_list[1:]):
        linetmp = return_list[-1]
        if len(return_list[-1]) + len(word) + 1 == k:
            return_list[-1] = f'{return_list[-1]} {word}'
            return_list.append(f'{word}')
            word_index = [len(return_list[-1])]
            continue
        elif len(return_list[-1]) + len(word) + 1 < k:
            if return_list[-1] == '':
                return_list[-1] = f'{word}'
            else:
                return_list[-1] = f'{return_list[-1]} {word}'
            word_index.append(len(return_list[-1]))
        if len(linetmp) + len(word) + 1 > k or n == len(str_list) - 2:
            while len(return_list[-1]) < k:
                offset = 0
                for pos in word_index:
                    if (pos + offset < len(return_list[-1])
                            or len(word_index) == 1):
                        offset += 1
                        return_list[-1] =\
                            (f'{return_list[-1][:pos + offset]} '
                             f'{return_list[-1][pos + offset:]}')

                    if len(return_list[-1]) == k:
                        break
            if len(linetmp) + len(word) + 1 > k:
                return_list.append(f'{word}')
                word_index = [len(return_list[-1])]
                if n == len(str_list) - 2:
                    return_list[-1] = return_list[-1].ljust(k)
            continue
    return return_list


if __name__ == '__main__':
    input = ["the", "quick", "brown", "fox",
             "jumps", "over", "the", "lazy", "dog"]
    test1 = justify_txt(
        input,
        16
    )
    assert len(test1) == 3
    assert test1[0] == "the  quick brown"
    assert test1[1] == "fox  jumps  over"
    assert test1[2] == "the   lazy   dog"
    test2 = justify_txt(
        input,
        5
    )
    assert len(test2) == 9
    for row in test2:
        assert len(row) == 5
        assert row == row.ljust(5)
