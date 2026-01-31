import re
# Import the tokenize function from your previous file
from lexer import tokenize 

class ASTNode:
    pass

class AssignmentNode(ASTNode):
    def __init__(self, name, value):
        self.name = name
        self.value = value

class BinOpNode(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Parser:
    def __init__(self, tokens):
        self.tokens = list(tokens) # Ensure it's a list we can index
        self.pos = 0

    def consume(self, expected_type=None):
        if self.pos >= len(self.tokens):
            raise Exception("Unexpected end of input")
        
        token = self.tokens[self.pos]
        if expected_type and token['type'] != expected_type:
            raise Exception(f"Expected {expected_type}, got {token['type']} at line {token['line']}")
        
        self.pos += 1
        return token

    def parse_expression(self):
        left = self.consume('NUMBER')
        op = self.consume('OP')
        right = self.consume('NUMBER')
        return BinOpNode(left, op, right)

    def parse_assignment(self):
        self.consume('INT')
        name = self.consume('ID')
        self.consume('ASSIGN')
        expr = self.parse_expression()
        self.consume('END')
        return AssignmentNode(name['value'], expr)

# --- This is the part that was missing ---
example_code = "int x = 10 + 5;"
tokens = tokenize(example_code) # Generate the tokens first!

parser = Parser(tokens)
ast = parser.parse_assignment()

print(f"Success! Parsed Assignment to: {ast.name}")
print(f"AST structure: {ast.name} = ({ast.value.left['value']} {ast.value.op['value']} {ast.value.right['value']})")