from dataclasses import dataclass

def func1(a:int, b:int) -> int:
    return a + b

PI:float = 3.1415926

@dataclass
class Student:
    name:str
    chinese:int
    math:int
    english:int