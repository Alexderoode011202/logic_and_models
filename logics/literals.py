

class Literal:
    def __init__(self, name: str):
        self.name: str = name
        self.bool_value = True

    def __str__(self) -> str:
        if not self.bool_value:
            return f"-{self.bool_value}"

    def get_bool_value(self) -> bool:
        """Returns the boolean value of the literal"""
        return self.bool_value

    def get_identity(self) -> str:
        """Returns what sort of object this is.
        :returns: string of the type of object"""

        return "literal"

    def make_negative(self) -> None:
        self.bool_value = False
        return None

    def make_positive(self) -> None:
        self.bool_value = True
        return None







