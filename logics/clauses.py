"""contains all the stuff regarding clauses"""


from typing import Iterable, Union, List, Dict



class CorrespondenceError(Exception):
    def __init__(self) -> None:
        super().__init__()

class Clause:
    def __init__(self, left_side, operator, right_side):
        self.left_side = left_side
        self.operator = operator
        self.right_side = right_side

    def get_bool_value(self, literal_values: dict) -> bool:
        """Calculates the boolean value of the clause and returns it"""
        left_bool : bool
        right_bool : bool
        literals: list= self.get_literals()
        print(f"literals = {literals}")
        print(f"values: {literal_values}")
        # check whether the iterable_values has the same length as the amount of literals in the clause
        if len(literals) != len(literal_values):
            raise IndexError("literal_values length does not match with the amount of literals")
        
        # LEFT CHECK
        if self.left_side.get_identity() == "literal":
            left_bool = literal_values[self.left_side]
        else:
            # If a side is a clause, we first need its literals
            left_literals = self.left_side.get_literals()
            literal_value_dict: dict = {}
            for literal in left_literals:
                literal_value_dict.update({literal: literal_values[literal]})
            left_bool = self.left_side.get_bool_value(literal_value_dict)
            
        # RIGHT CHECK
        if self.right_side.get_identity() == "literal":
            right_bool = literal_values[self.right_side]

        else:
            right_literals = self.right_side.get_literals()
            literal_value_dict: dict = {}
            for literal in right_literals:
                literal_value_dict.update({literal: literal_values[literal]})
            right_bool = self.left_side.get_bool_value(literal_value_dict)

        # confirmation 1
        print(f"left = {left_bool}, right = {right_bool}")



        # CALCULATE RESULT WITH BOOL VALUES
        return self.operator.calculate_bool_value(left_bool, right_bool)
            
    def get_identity(self):
        """Returns what sort of object this is.
        :returns: string of the type of object"""

        return "clause"
    
    def get_literals(self) -> list:
        """NEEDS TO BE WORKED OUT MORE"""
        literals: list = []

        # left side
        if self.left_side.get_identity() == "literal":
            literals.append(self.left_side)
            
        elif self.left_side.get_identity() == "clause":
            
            literals.extend(self.left_side.get_literals())

        # right side
        if self.right_side.get_identity() == "literal":
            literals.append(self.right_side)
            
        elif self.right_side.get_identity() == "clause":
            literals.extend(self.right_side.literals())
            

        return list(set(literals))
    
    def get_left(self):
        return self.left_side
    
    def get_right(self):
        return self.left_side
    
    def get_operator(self):
        return self.operator
    
    def __str__(self)-> str:
        left: str
        right: str
        if self.left_side == "literal":
            left = str(self.left_side)
        else: 
            left = "(" + str(self.right_side) + ")"

        if self.left_side == "literal":
            left = str(self.left_side)
        else: 
            left = "(" + str(self.right_side) + ")"

    def get_subclauses(self):
            """returns all the subclauses a clause has
            :returns: list of all found subclauses"""
            subclauses: list = []
            if self.left_side.get_identity() == "clause":
                subclauses.append(self.left_side)
            if self.right_side.get_identity() == "clause":
                subclauses.append(self.right_side)

            return subclauses
    
    def __str__(self) -> str:
        return f"({self.left_side} {self.operator} {self.right_side})"
    
print("BOOTING UP CLAUSES FILE: SUCCESFULL")