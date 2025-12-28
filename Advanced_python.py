from typing import List, Tuple, Dict, Union

#using walrus operator
if(n := len([1, 2, 3, 4, 5])) > 3:
    print(f"Length is too long ({n} elements, expected <= 3)")


#types
n : int = 5
s : str = "Appu"

def sum(a: int, b:int) -> int:
    return a + b

#syntax of this is basically like this:

#list of integers
numbers: list[int] = [1, 2, 3, 4, 5]

#tuple
person : Tuple[str, int] = ("Appu", 420)

#dictionary
scores: Dict[str, int] = {"Appu": 90, "Apoorva": 99}

#union
identifier: Union[int, str] = "ID420"   #either int or str
identifier: 12345