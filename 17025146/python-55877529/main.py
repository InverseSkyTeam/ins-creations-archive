from ssa import *

def print_cfg(block_list):
    for block in block_list:
        print(f"Block: {block.id}")
        for phi in block.phi_funcs.values():
            print(f"{phi.var} := phi({', '.join(phi.args)})")
        for command in block.code:
            if command.res:
                if command.op == OpType.ASSIGN:
                    print(f"{command.res} := {command.left}")
                else:
                    if command.right:
                        print(f"{command.res} := {command.left} {command.op.name.lower()} {command.right}")
                    else:
                        print(f"{command.res} := {command.op.name.lower()} {command.left}")
            else:
                if command.right:
                    print(f"{command.op.name.lower()} {command.left} {command.right}")
                else:
                    print(f"{command.op.name.lower()} {command.left}")
        print("--------------")

"""
a := 1
if a <= 2 then
    c := 3
else
    c := 4
endif
d := c
"""
I = Instruction
code = [
    I(OpType.ASSIGN, 1, None, "a"),
    I(OpType.LE, "a", 2, "b"),
    I(OpType.JZ, "else", "b"),
    I(OpType.ASSIGN, 3, None, "c"),
    I(OpType.JMP, "endif"),
    I(OpType.LABEL, "else"),
    I(OpType.ASSIGN, 4, None, "c"),
    I(OpType.LABEL, "endif"),
    I(OpType.ASSIGN, "c", None, "d")
]
ssa = code_to_ssa(code)
print_cfg(ssa)