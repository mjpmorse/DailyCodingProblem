

def string_validator(par_str: str) -> int:
    """Given an input string of "(" and ")",
    returns the number of elements which must
    be removed to make the string valid, i.e.
    every ( has a ).

    Args:
        par_str (str): parenthesis string

    Returns:
        int: number of chars which must be removed
    """
    str_list = [x for x in par_str]
    # loop through the string backwards looking for ")"
    popped = True
    while popped and len(str_list) > 0:
        for pos, char in enumerate(str_list):
            '''
            If there is a "(" pop it from the list.
            This will change the "partnership" of
            the () but will keep the relative number and
            their placement, before or after each other
            intact.
            Therefore it will solve the question without
            having to determine each pair of nested ()
            '''
            if char == "(":
                try:
                    next_cls = str_list[pos:].index(")")
                    str_list.pop(pos + next_cls)
                    str_list.pop(pos)
                    # since we are chaning the list past
                    # where we are in our iteration, out iteration
                    # index will be messed up and we have to restart.
                    popped = True
                    break
                # if no '(' is found which corresponds to our ')'
                # we are done. Break the loop and return len.
                except ValueError:
                    popped = False
                    break
            else:
                popped = False
    return len(str_list)


if __name__ == '__main__':
    assert string_validator("()())()") == 1
    assert string_validator(")(") == 2
    assert string_validator("((()))") == 0
    assert string_validator(")))()()((()())") == 4

