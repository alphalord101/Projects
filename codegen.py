class CodeGenerator:
    def __init__(self):
        self.instructions = []
        self.temp_count = 0

    def new_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"

    def generate(self, node):
        # Handle the case where the optimizer turned the math into a single number
        if isinstance(node, dict) and node['type'] == 'NUMBER':
            return node['value']

        if hasattr(node, 'left'):  # BinOpNode
            left = node.left['value']
            right = node.right['value']
            op = node.op['value']
            temp = self.new_temp()
            self.instructions.append(f"{temp} = {left} {op} {right}")
            return temp

        elif hasattr(node, 'name'):  # AssignmentNode
            rhs_val = self.generate(node.value)
            self.instructions.append(f"{node.name} = {rhs_val}")
            return node.name
        
    def dump(self):
        print("\n--- GENERATED INTERMEDIATE CODE ---")
        for instr in self.instructions:
            print(instr)
# --- Integration Example ---
