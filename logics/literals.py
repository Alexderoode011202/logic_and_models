

class Literal:
    def __init__(self, name: str):
        self.name: str = name
        
    def __str__(self) -> str:
        
        return f"{self.name}"


    """def get_bool_value(self) -> bool:
        return self.bool_value"""

    def get_identity(self) -> str:
        """Returns what sort of object this is.
        :returns: string of the type of object"""

        return "literal"
    
    def give_value(self, value: bool) -> None:
        self.value = value

    def is_negated(self) -> bool:
        """Is used to check whether it is a normal or negated literal"""
        return False

class NegatedLiteral(Literal):
    def __init__(self, name: str):
        super().__init__(name=name)

    def is_negated(self) -> bool:
        return True
    
    def __str__(self) -> str:
        return f"-{self.name}"
    
    
print("BOOTING UP LITERALS FILE: SUCCESFULL")








