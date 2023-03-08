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

    # step 0. Acquire all the data
    left: Union[Clause, Literal, NegatedLiteral] = clause.get_left()
    right: Union[Clause, Literal, NegatedLiteral] = clause.get_right()
    literals: Iterable[Iterable] = clause.get_literals()

    # step 1: Generate the left side of the TT (aka, the truth values)
    truth_combinations : List[Tuple[bool, bool, bool]] = gtt(len(literals))
    print(truth_combinations)

    # step 2: Create the columns for the literals (for pandas)
    literal_columns: List[List[bool]] = []
    for combination in truth_combinations:
        for num, value in enumerate(combination):
            # get the column
            current_row: list 
            try:
                current_row = literal_columns[num]
            except IndexError:
                current_row = []
            
            #add the value to the column and put the list back
            current_row.append(value)
            literal_columns.insert(num, current_row)
            # print(f"columns_test: {literal_columns}")
            try:
                literal_columns.pop(num + 1)
            except IndexError:
                continue
    # Now we have the columns for the literals, we can proceed to step 3
    # step 3: Prep. the dictionary for calculating truth values
    truth_dict: List[Dict[Literal: bool]] = []
    for comb in truth_combinations:
        sub_dict: dict = {}
        for literal, value in zip(literals, comb):
            # {A: True}
            sub_dict.update({literal: value})
            # [{A: True, ...}, {A: False, ...}]
        truth_dict.append(sub_dict)

    # step 4: With our dictionaries ready, we can calculate the truth values we need
    truth_values: List[bool] = []
    for values in truth_dict:
        truth_values.append(clause.get_bool_value(values))
        
    # step 5: Now we have the truth values, set up the Dataframe
    print(truth_values)

"""
Testing, more testing, and some more testing!
"""

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

answer = parent_clause.get_bool_value({A: True, C: True, not_B: True, not_C: True})

print(f"parent clause: {parent_clause} is {answer}.")


generate_TT(parent_clause)