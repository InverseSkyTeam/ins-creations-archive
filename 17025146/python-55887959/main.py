from ssa import *

op_dict = {
    OpType.ADD: lambda x, y: x + y,
    OpType.SUB: lambda x, y: x - y,
    OpType.MUL: lambda x, y: x * y,
    OpType.DIV: lambda x, y: x / y,
    OpType.MOD: lambda x, y: x % y,
    OpType.EQ: lambda x, y: x == y,
    OpType.NE: lambda x, y: x!= y,
    OpType.LT: lambda x, y: x < y,
    OpType.LE: lambda x, y: x <= y,
    OpType.GT: lambda x, y: x > y,
    OpType.GE: lambda x, y: x >= y,
    OpType.AND: lambda x, y: x & y,
    OpType.OR: lambda x, y: x | y,
    OpType.XOR: lambda x, y: x ^ y,
    OpType.SHL: lambda x, y: x << y,
    OpType.SHR: lambda x, y: x >> y,
    OpType.NEG: lambda x: -x,
}

def def_use_chain(block_list):
    def_use = {}
    for block in block_list:
        for phi in block.phi_funcs.values():
            for arg in phi.args:
                if arg not in def_use:
                    def_use[arg] = []
                def_use[arg].append(phi)
            if phi.var not in def_use:
                def_use[phi.var] = []
        for command in block.code:
            if command.op in (OpType.JMP, OpType.LABEL):
                continue
            if command.op in (OpType.JZ, OpType.JNZ):
                if isinstance(command.right, str):
                    if command.right not in def_use:
                        def_use[command.right] = []
                    def_use[command.right].append(command)
                continue
            if isinstance(command.left, str):
                if command.left not in def_use:
                    def_use[command.left] = []
                def_use[command.left].append(command)
            if isinstance(command.right, str):
                if command.right not in def_use:
                    def_use[command.right] = []
                def_use[command.right].append(command)
            if command.res not in def_use:
                def_use[command.res] = []
    return def_use

def remove_dead_code(command, def_use):
    if isinstance(command, Instruction):
        if not command.res:
            return False
        if not def_use.get(command.res):
            if isinstance(command.left, str):
                def_use[command.left].remove(command)
            if isinstance(command.right, str):
                def_use[command.right].remove(command)
            return True
        return False
    if isinstance(command, Phi):
        if not def_use.get(command.var):
            for arg in command.args:
                if isinstance(arg, str):
                    def_use[arg].remove(command)
            return True
        return False

def constant_folding(command):
    if not command.res:
        return False
    if isinstance(command.left, int) and isinstance(command.right, int):
        if command.op in op_dict:
            command.left = op_dict[command.op](command.left, command.right)
            command.right = None
            command.op = OpType.ASSIGN
            return True
    return False

def replication_propagation(command, def_use):
    if isinstance(command, Instruction):
        if command.op != OpType.ASSIGN:
            return False
        if command.right is None:
            for use in def_use.get(command.res, []):
                if isinstance(use, Instruction):
                    if use.left == command.res:
                        use.left = command.left
                    if use.right == command.res:
                        use.right = command.left
                if isinstance(use, Phi):
                    use.args.remove(command.res)
                    use.args.add(command.left)
            return True
        return False
    if isinstance(command, Phi):
        if len(command.args) > 1:
            return False
        for use in def_use.get(command.var, []):
            if isinstance(use, Instruction):
                if use.left == command.var:
                    use.left = command.args[0]
                if use.right == command.var:
                    use.right = command.args[0]
            if isinstance(use, Phi):
                use.args.remove(command.var)
                use.args.append(command.args[0])
        return True
    
def optimize(block_list, def_use):
    changed = True
    while changed:
        changed = False
        for block in block_list:
            new_phi = {}
            for name, phi in block.phi_funcs.items():
                if remove_dead_code(phi, def_use):
                    changed = True
                elif replication_propagation(phi, def_use):
                    changed = True
                else:
                    new_phi[name] = phi
            block.phi_funcs = new_phi
            for command in block.code:
                if remove_dead_code(command, def_use):
                    changed = True
                    block.code.remove(command)
                else:
                    folded = constant_folding(command)
                    if replication_propagation(command, def_use):
                        changed = True
                        block.code.remove(command)
                    else:
                        changed = folded
    return block_list

def print_cfg(block_list):
    for block in block_list:
        print(f"Block: {block.id}")
        for phi in block.phi_funcs.values():
            print(f"{phi.var} := phi({', '.join([str(arg) for arg in phi.args])})")
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

I = Instruction
code = [
    I(OpType.ASSIGN, 1, None, "a"),
    I(OpType.ASSIGN, 5, None, "e"),
    I(OpType.LE, "a", 2, "b"),
    I(OpType.JZ, "else", "b"),
    I(OpType.ASSIGN, 3, None, "c"),
    I(OpType.JMP, "endif"),
    I(OpType.LABEL, "else"),
    I(OpType.ASSIGN, 4, None, "c"),
    I(OpType.LABEL, "endif"),
    I(OpType.ASSIGN, "c", None, "d"),
    I(OpType.PRINT, "d")
]
ssa_block = code_to_ssa(code)
def_use = def_use_chain(ssa_block)
blocks = optimize(ssa_block, def_use)
print_cfg(blocks)