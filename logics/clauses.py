"""contains all the stuff regarding clauses"""

from operators import Logical_Operator
from typing import Iterable, Union
from literals import Literal
from clauses import Clause


class Clause:
    def __init(self, left_side: Union[Clause, Literal], operator: Logical_Operator, right_side: Union[Clause, Literal]):
        self.left_side = left_side
        self.operator = operator
        self.right_side = right_side

    def get_bool_value(self) -> bool:
        """Calculates the boolean value of the clause and returns it"""
        left_bool : bool
        right_bool : bool

        # first check whether the left is a sub-clause
        if self.left_side.get_identity() == "clause":
            left_bool = self.left_side.get_bool_value()

        else:
            left_bool = self.left_side.get_bool_value()

        # first check whether the left is a sub-clause
        if self.left_side.get_identity() == "clause":
            right_bool = self.right_side.get_bool_value()

        else:
            right_bool = self.right_side.get_bool_value()

        return self.operator.calculate_bool_value(left_bool, right_bool)


    def get_identity(self):
        """Returns what sort of object this is.
        :returns: string of the type of object"""

        return "clause"


