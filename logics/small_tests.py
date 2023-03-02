from typing import Tuple, List
def generate_left_side_TT(amount_of_literals: int) -> List[bool]:
    from itertools import permutations
    truths = amount_of_literals * [True]
    falses = amount_of_literals * [False]
    truths.extend(falses)
    full_list = list(set(permutations(truths, amount_of_literals)))
    full_list.sort(key= lambda x: x.count(True), reverse=True)
    return full_list


print(generate_left_side_TT(3))

test_list = []