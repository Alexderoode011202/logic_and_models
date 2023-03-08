"""Contains all the main functions that are supposed to be used for performing logical calculations"""

from clauses import Clause
from literals import Literal, NegatedLiteral
from operators import OR, Logical_Operator, BI_IMPLIES, IMPLIES, AND, XOR

from typing import Optional, Iterable, Union, List, Tuple, Dict

from helpers import generate_left_side_TT as gtt

def generate_TT(clause: Clause):
    """Generates a truth table based on the clause given to the function
    :param clause: contains the clause that we want the truth table from
    :returns: Dataframe containing the Truth Table"""

    # Step 1. Get the all the iterables


ANd = AND()

Or = OR()

XOr = XOR()
Bi_Imp = BI_IMPLIES()
IMP = IMPLIES()

A = Literal("A")
not_A = NegatedLiteral("A")

B = Literal("B")
not_B = NegatedLiteral("B")

C = Literal("C")
not_C = NegatedLiteral("C")

subclause_1: Clause = Clause(A, IMP, not_C)
subclause_2: Clause = Clause(not_B, Bi_Imp, C)

parent_clause: Clause = Clause(subclause_1, ANd, subclause_2)

answer = parent_clause.get_bool_value({A: True, C: True, not_B: True, not_C: True, A: True})

print(f"parent clause: {parent_clause} is {answer}")
