class Optimizer:
    def optimize(self, node):
        # If the node is an Assignment, optimize the expression inside it
        if hasattr(node, 'value'):
            node.value = self.optimize_expression(node.value)
        return node

    def optimize_expression(self, node):
        # We only care about BinOpNodes (like 10 + 5)
        if hasattr(node, 'left') and hasattr(node, 'right'):
            # Check if both sides are numbers
            if node.left['type'] == 'NUMBER' and node.right['type'] == 'NUMBER':
                left = node.left['value']
                right = node.right['value']
                op = node.op['value']
                
                # Perform the math at compile-time!
                if op == '+': result = left + right
                elif op == '-': result = left - right
                elif op == '*': result = left * right
                elif op == '/': result = left / right
                
                print(f"Optimizer: Folding {left} {op} {right} into {result}")
                
                # Return a new simple number token instead of the operation
                return {'type': 'NUMBER', 'value': result}
        return node