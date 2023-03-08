"""Contains all the main functions that are supposed to be used for performing logical calculations"""

from clauses import Clause
from literals import Literal
from operators import OR, Logical_Operator

from typing import Optional, Iterable, Union, List, Tuple

from helpers import generate_left_side_TT as gtt

print("CORE BOOTING UP...")

def generate_TT(clause: Clause, literals: Optional[Iterable[Literal]] = None):
    """Generates a truth table based on the clause given to the function
    :param clause: contains the clause that we want the truth table from
    :returns: Dataframe containing the Truth Table"""

    left: Union[Clause, Literal] = clause.get_left()
    right: Union[Clause, Literal] = clause.get_right()
    # step 1: Get the iterables
    literals = clause.get_iterables()

    # step 2. Generate the left side values
    left_values: List[Tuple[bool, bool, bool]] = gtt(len(literals))

    # step 3. Calculate the truth value for the clause in each case
    models: List[bool] = []
    for row in left_values:
        pass



first_literal: Literal = Literal("A")
second_literal: Literal = Literal("B")

operator_or: Logical_Operator = OR()



first_clause: Clause = Clause(left_side= first_literal, operator=operator_or, right_side=first_literal)
second_clause : Clause = Clause(left_side = first_clause, operator= operator_or, right_side=second_literal)

test = second_clause.get_bool_value({first_literal: True, second_literal: False})
print(test)

