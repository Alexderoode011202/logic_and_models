"""Contains all the main functions that are supposed to be used for performing logical calculations"""

from clauses import Clause
from literals import Literal, NegatedLiteral
from operators import OR, Logical_Operator

from typing import Optional, Iterable, Union, List, Tuple, Dict

from helpers import generate_left_side_TT as gtt

print("CORE BOOTING UP...")

def generate_TT(clause: Clause):
    """Generates a truth table based on the clause given to the function
    :param clause: contains the clause that we want the truth table from
    :returns: Dataframe containing the Truth Table"""

    # Step 1. Get the all the iterables




first_literal: Literal = NegatedLiteral("A")
second_literal: Literal = Literal("B")

operator_or: Logical_Operator = OR()



first_clause: Clause = Clause(left_side= first_literal, operator=operator_or, right_side=second_literal)
second_clause : Clause = Clause(left_side = first_clause, operator= operator_or, right_side=second_literal)
print(f"clause = {first_clause}")
test = first_clause.get_bool_value({first_literal: True, second_literal: False})
# print(second_clause.get_literals())
print(f"result: {test}")

print("TEST OVER")
