from lexer import tokenize
from parser import Parser
from lexer import tokenize
from parser import Parser
from codegen import CodeGenerator # Import the new module
from lexer import tokenize
from parser import Parser
from optimizer import Optimizer
from codegen import CodeGenerator

code = "int x = 10 + 5;"

# 1. Lexical Analysis
tokens = list(tokenize(code))

# 2. Syntax Analysis
parser = Parser(tokens)
ast = parser.parse_assignment()

# 3. Optimization (Module 6)
# This changes '10 + 5' into '15' inside the AST
opt = Optimizer()
ast = opt.optimize(ast) 

# 4. Intermediate Code Generation
codegen = CodeGenerator()
codegen.generate(ast)
codegen.dump()
code = "int x = 10 + 5;"

# 1. Lex
tokens = list(tokenize(code))

# 2. Parse
parser = Parser(tokens)
ast = parser.parse_assignment()

# 3. Code Generation (Module 5)
codegen = CodeGenerator()
codegen.generate(ast)
codegen.dump()
# --- MODULE 3 & 4: Semantics & Symbol Table ---
# (We can keep this here or move it to semantics.py)
class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def declare(self, name, var_type):
        if name in self.symbols:
            raise Exception(f"Semantic Error: {name} already declared.")
        self.symbols[name] = {'type': var_type, 'value': None}

# --- EXECUTION PIPELINE ---

code = "int x = 10 + 5;"

# Step 1: Lexical Analysis (Module 1)
tokens = list(tokenize(code))

# Step 2: Syntax Analysis (Module 2)
parser = Parser(tokens)
ast = parser.parse_assignment()

# Step 3: Semantic Analysis (Module 3)
table = SymbolTable()
print(f"Checking semantics for variable: {ast.name}...")
table.declare(ast.name, "INT")

print("\n--- COMPILER STATUS ---")
print(f"Variable '{ast.name}' successfully registered in Symbol Table.")
print(f"Current Table: {table.symbols}")
