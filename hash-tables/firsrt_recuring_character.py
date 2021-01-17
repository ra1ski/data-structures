from typing import List, Union

example_one = [2, 5, 1, 2, 3, 5, 1, 2, 4]  # returns 2
example_two = [2, 1, 1, 2, 3, 5, 1, 2, 4]  # returns 1
example_three = [2, 3, 4, 5]  # returns None


def first_recurring_character(a_list: List[int]) -> Union[int, None]:
    """ Hash map solution. Good time complexity. Tradeoff: memory
    Args:
        a_list: array
    Returns: first recurring character
    """
    hash_map = {}

    for i in a_list:
        if i not in hash_map:
            hash_map[i] = True
        else:
            return i

    return None


print(first_recurring_character(example_one))
print(first_recurring_character(example_two))
print(first_recurring_character(example_three))
