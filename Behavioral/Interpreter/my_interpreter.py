from enum import Enum, auto

class Type(Enum):
    PLUS = auto()
    MINUS = auto()
    DIGIT = auto()
    VARIABLE = auto()

class Token:
    def __init__(self, type, text):
        self.type = type
        self.text = text

class Expression:
    def __init__(self) -> None:
        self.left_side = None
        self.right_side = None
        self.operator = None

class ExpressionProcessor:
    def __init__(self):
        self.variables = {}

    def lex(self, expression):
        tokens = []
        i = 0

        while i < len(expression):
            if expression[i] == "+":
                tokens.append(Token(Type.PLUS, expression[i]))
            elif expression[i] == "-":
                tokens.append(Token(Type.MINUS, expression[i]))
            elif expression[i].isdigit():
                j = i + 1
                digit = expression[i]

                while next_val := expression[j].isdigit():
                    digit = f'{digit}{next_val}'
                    j += 1

                tokens.append(Token(Type.DIGIT, int(digit)))
                i = j
            elif expression[i].isalpha():
                if expression[i+1].isalpha():
                    return None
                else:
                    tokens.append(Token(Type.VARIABLE, expression[i]))
            else:
                return None

    def parse(self, tokens):
        expression = Expression()
        i = 0
        
        while i < len(tokens):
            if tokens[i].type == Type.PLUS or tokens[i].type == Type.MINUS:
                expression.operator = tokens[i].text
            elif tokens[i].type == Type.DIGIT:
                self.execute_expression(tokens[i].text)
            elif tokens[i].type == Type.VARIABLE:
                num = self.variables[tokens[i].text]
                self.execute_expression(num)

        return expression.left_side if expression.left_side is not None else 0
    
    def execute_expression(self, expression, num):
        if expression.left_side is None:
            expression.left_side = num
        else:
            expression.right_side = num
            if expression.operator == "+":
                expression.left_side += expression.right_side
            else:
                expression.left_side -= expression.right_side
                

    def calculate(self, expression):
        tokens = self.lex(expression)

        if tokens is None:
            return 0

        return self.parse(tokens)
