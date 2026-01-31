class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def declare(self, name, var_type):
        if name in self.symbols:
            raise Exception(f"Semantic Error: Variable '{name}' already declared.")
        self.symbols[name] = {'type': var_type, 'value': None}

    def lookup(self, name):
        if name not in self.symbols:
            raise Exception(f"Semantic Error: Variable '{name}' used before declaration.")
        return self.symbols[name]

# --- Integration Example ---
table = SymbolTable()

# Simulating the Semantic Analysis of 'int x = 10 + 5;'
var_name = ast.name  # From your Parser output 'x'
var_type = 'INT'     # Usually extracted from the AST

print(f"Checking semantics for: {var_name}...")
table.declare(var_name, var_type)
print(f"Symbol Table updated: {table.symbols}")