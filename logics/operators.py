"""Contains all the operators needed for (boolean) logical reasoning"""
from clauses import Clause
from typing import Union
from literals import Literal


class Logical_Operator:
    """Is the parent class for all logical operators"""
    def __init__(self):
        return None
    def __str__(self) -> str:
        "TYPE OF OPERATOR"

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

    def __str__(self) -> str:
        pass


class OR(Logical_Operator):
    def __init__(self):
        super().__init__()
        return None

    def calculate_bool_value(self, left: bool, right: bool) -> bool:
        """Calculates the truth value of the given input.
            :param left: is a boolean value and is supposed to be from a Literal
            :param right: is a boolean value is supposed to be from a Literal
            :returns: boolean value depending on the input and calculator
        """
        print(f"test 2: left = {left}, right = {right}")
        if not left and not right:
            return False
        else:
            True
    def __str__(self) -> str:
        return "OR"
    
class AND(Logical_Operator):
    def __init__(self):
        super().__init__()
        return None
    
    def calculate_bool_value(self, left: bool, right: bool) -> bool:
        if left and right:
            return True
        else:
            return False
        
    def __str__(self) -> str:
        return "AND"
        
class IMPLIES(Logical_Operator):
    def __init__(self):
        super().__init__()
        return None
    
    def __str__(self):
        return "->"
    
    def calculate_bool_value(self, left: bool, right: bool) -> bool:
        if not left:
            return True
        elif right:
            return True
        else:
            return False
        
class XOR (Logical_Operator):
    def __init__(self):
        super().__init__()
        return None
    
    def calculate_bool_value(self, left: bool, right: bool) -> bool:
        if left == right:
            return False
        else:
            return True
        
    def __str__(self) -> str:
        return "XOR"


print("BOOTING UP OPERATORS FILE: SUCCESFULL")
