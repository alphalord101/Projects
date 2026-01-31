import re

# 1. Define your Token types using Regular Expressions
TOKEN_SPEC = [
    ('NUMBER',   r'\d+(\.\d+)?'),  # Integer or decimal number
    ('ASSIGN',   r'='),            # Assignment operator
    ('END',      r';'),            # Statement terminator
    ('ID',       r'[A-Za-z_]\w*'), # Identifiers (variables)
    ('OP',       r'[+\-*/]'),      # Arithmetic operators
    ('LPAREN',   r'\('),           # (
    ('RPAREN',   r'\)'),           # )
    ('LBRACE',   r'\{'),           # {
    ('RBRACE',   r'\}'),           # }
    ('SKIP',     r'[ \t]+'),       # Skip over spaces and tabs
    ('NEWLINE',  r'\n'),           # Line endings
    ('MISMATCH', r'.'),            # Any other character (error)
]

def tokenize(code):
    # Combine all patterns into one master regex
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in TOKEN_SPEC)
    line_num = 1
    line_start = 0
    
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        column = mo.start() - line_start
        
        if kind == 'NUMBER':
            value = float(value) if '.' in value else int(value)
        elif kind == 'ID':
            # Check for Keywords
            if value in {'if', 'else', 'while', 'print', 'int', 'bool'}:
                kind = value.upper()
        elif kind == 'NEWLINE':
            line_start = mo.end()
            line_num += 1
            continue
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'{value!r} unexpected on line {line_num}')
        
        yield {'type': kind, 'value': value, 'line': line_num, 'column': column}

# --- Test the Lexer ---
example_code = "int x = 10 + 5;"
tokens = list(tokenize(example_code))

for t in tokens:
    print(t)