from abc import abstractmethod, ABC
from enum import Enum
from typing import Union

class Context:
    
    lookup_table: dict

    def __init__(self, lookup_table: Union[dict, None] = None):
        self.lookup_table = {} if not lookup_table else lookup_table

    def bind(self, name: str, value: float):
        self.lookup_table[name] = value

    def getValue(self, name: str) -> float:
        return self.lookup_table[name]

class Term(ABC):
    @abstractmethod
    def eval(self, context: Context) -> float:
        pass

class Constant(Term):
    value: float

    def __init__(self, value: float):
        self.value = value
    
    def eval(self, context: Context) -> float:
        return self.value

class Variable(Term):
    name: str

    def __init__(self, name: str, value: float, context: Context):
        self.name = name
        context.bind(self.name, value)


    def eval(self, context: Context) -> float:
        return context.getValue(self.name)
    
class BinaryOperator(Enum):
    ADD = lambda x, y: float(x + y)
    SUB = lambda x, y: float(x - y)
    MUL = lambda x, y: float(x * y)
    DIV = lambda x, y: float(x / y)
    
class BinaryOperation(Term):
    left: Term
    right: Term
    binary_operator: BinaryOperator

    def __init__(self, left: Term, right: Term, binary_operator: BinaryOperator):
        self.left = left
        self.right = right
        self.binary_operator = binary_operator

    def eval(self, context: Context) -> float:
        return self.binary_operator(
            self.left.eval(context), 
            self.right.eval(context)
        )

class UnaryOperator(Enum):
    NEG = lambda x: float(-x)
    POS = lambda x: float(x)

class UnaryOperation(Term):
    term: Term
    unariy_operator: UnaryOperator

    def __init__(self, term: Term, unariy_operator: UnaryOperator):
        self.term = term
        self.unariy_operator = unariy_operator

    def eval(self, context: Context) -> float:
        return self.unariy_operator(
            self.term.eval(context)
        )
    

if __name__ == "__main__":
    c = Context()
    d = Variable("d", 7, c)
    print(BinaryOperation((BinaryOperation(Constant(3), UnaryOperation(d, UnaryOperator.NEG), Binary_operator.ADD)), Constant(5), Binary_operator.MUL).eval(c))

    