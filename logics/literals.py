

class Literal:
    def __init__(self, name: str,):
        self.name: str = name
        self.value : bool = True
    def __str__(self) -> str:
        if self.bool_value:
            return f"{self.name}"

    """def get_bool_value(self) -> bool:
        return self.bool_value"""

    def get_identity(self) -> str:
        """Returns what sort of object this is.
        :returns: string of the type of object"""

        return "literal"
    
    def give_value(self, value: bool) -> None:
        self.value = value
    

print("BOOTING UP LITERALS FILE: SUCCESFULL")








