from operators import Logical_Operator, OR
from clauses import Clause
from literals import Literal
from typing import Iterable, List
from small_tests import generate_left_side_TT
import pandas as pd

def create_TT(self, literals: List[Literal], clauses: List[Clause]):
    amout_of_literals: int = len(literals)

    # length = literals**2
    left_side = generate_left_side_TT(amout_of_literals)

    df = pd.DataFrame(columns = literals.extend(clauses))