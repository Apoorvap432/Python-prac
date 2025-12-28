#using walrus operator
if(n := len([1, 2, 3, 4, 5])) > 3:
    print(f"Length is too long ({n} elements, expected <= 3)")


#types
n : int = 5
s : str = "Appu"

def sum(a: int, b:int) -> int:
    return a + b