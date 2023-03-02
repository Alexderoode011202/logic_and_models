"""Contains all the operators needed for (boolean) logical reasoning"""
from clauses import Clause
from typing import Union
from literals import Literal


class Logical_Operator:
    """Is the parent class for all logical operators"""

    def __str__(self) -> str:
        "operator"

    def get_identity(self) -> str:
        """Returns what sort of object this is.
         :returns: string of the type of object"""
        return "operator"

    def calculate_bool_value(self, left: bool, right: bool) -> bool:
        """Calculates the truth value of the given input.
            :param left: is a boolean value and is supposed to be from a Literal
            :param right: is a boolean value is supposed to be from a Literal
            :returns: boolean value depending on the input and calculator
        """
        pass


class OR(Logical_Operator):
    def __init__(self, left_side: Union[Clause, Literal], right_side = Union[Clause, Literal]):
        super().__init__()

    def calculate_bool_value(self, left: bool, right: bool) -> bool:
        """Calculates the truth value of the given input.
            :param left: is a boolean value and is supposed to be from a Literal
            :param right: is a boolean value is supposed to be from a Literal
            :returns: boolean value depending on the input and calculator
        """

        if left and right:
            return False
        else: return True




