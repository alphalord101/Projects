class TargetGenerator:
    def __init__(self, ir_instructions):
        self.ir = ir_instructions

    def translate(self):
        print("\n--- MODULE 7: TARGET CODE (ASSEMBLY) ---")
        for instr in self.ir:
            parts = instr.split(' = ')
            target = parts[0]
            value = parts[1]
            
            print(f"LOAD R1, {value}")
            print(f"STORE {target}, R1")