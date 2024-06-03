import regex
from typing import Pattern
from Terms import BinaryOperator, Context, Constant, BinaryOperation, UnaryOperation, UnaryOperator

ARITHMIC_EXPRESSION = regex.compile(r"(\((?P<left>\d+(?:\.\d+)?|(?R))\s?(?P<operator>[+\-\/*])\s?(?P<right>\d+(?:\.\d+)?|(?R))\))")
FLOAT_NUMBER = regex.compile(r"\d+(?:\.\d+)?")

class TermsParser:
    BINARY_OPERATOR_MAP = {"+": BinaryOperator.ADD, "-": BinaryOperator.SUB, "*": BinaryOperator.MUL, "/": BinaryOperator.DIV}

    def parse(self, expression: str) -> BinaryOperation:
        def is_float_number(number: str) -> bool:
            return FLOAT_NUMBER.fullmatch(number) is not None


        match = ARITHMIC_EXPRESSION.search(expression)
        if not match:
            return None
        left = match.group('left')
        operator = match.group('operator')
        right = match.group('right')
        return BinaryOperation(
            Constant(float(left)) if is_float_number(left) else self.parse(left),
            Constant(float(right)) if is_float_number(right) else self.parse(right),
            self.BINARY_OPERATOR_MAP[operator]
        )
    
if __name__ == "__main__":
    parser = TermsParser()
    result = parser.parse("((3.25*4)+(9-(2*2)))").eval(Context())
    print(result)
    # print(parser.parse("((3.5 + 6.35 / 3) + ((18 - 0.25) / 3))")).eval(Context())
    