from dataclasses import dataclass
from typing import Dict, Any, List
from enum import Enum

class OpType(Enum):
    ASSIGN = 0
    ADD = 1
    LE = 2
    # 以及一堆运算符，懒得加了

@dataclass(frozen=True)
class Register:
    name: str

@dataclass(frozen=True)
class Constant:
    value: Any

@dataclass
class Phi:
    res: Register
    args: Dict[str, Any]

@dataclass
class Label:
    label: str

@dataclass
class Br:
    cond: Any
    then: str
    else_: str

@dataclass
class Op:
    op: str
    left: Any
    right: Any
    res: Register

@dataclass
class Call:
    func: str
    args: List[Any]
    res: Register

class CFG:
    def __init__(self, label: str):
        self.label = label
        self.phi = {}
        self.instructions = []
        self.pred = set()
        self.succes = set()
    
    def __str__(self):
        return f"CFG({self.label})"
    __repr__ = __str__
    
    def __hash__(self):
        return hash(self.label)

def build_cfg(instructions):
    cfgs = {"main": CFG("main")}
    requires = {}
    current = "main"
    for i in instructions:
        if isinstance(i, Label):
            new_cfg = CFG(i.label)
            cfgs[i.label] = new_cfg
            if i.label in requires:
                for require in requires[i.label]:
                    require.succes.add(new_cfg)
                    new_cfg.pred.add(require)
                requires.pop(i.label)
            current = i.label
        else:
            cfgs[current].instructions.append(i)
            if isinstance(i, Br):
                if i.then in cfgs:
                    cfgs[current].succes.add(cfgs[i.then])
                    cfgs[i.then].pred.add(cfgs[current])
                elif i.then in requires:
                    requires[i.then].add(cfgs[current])
                else:
                    requires[i.then] = {cfgs[current]}
                if i.else_:
                    if i.else_ in cfgs:
                        cfgs[current].succes.add(cfgs[i.else_])
                        cfgs[i.else_].pred.add(cfgs[current])
                    elif i.else_ in requires:
                        requires[i.else_].add(cfgs[current])
                    else:
                        requires[i.else_] = {cfgs[current]}
    return cfgs

def get_dominators(cfgs):
    dominators = {}
    for label, cfg in cfgs.items():
        dominators[label] = {cfg}
    changed = True
    while changed:
        changed = False
        for label, cfg in cfgs.items():
            temp = set()
            for pred in cfg.pred:
                if temp:
                    temp &= dominators[pred.label]
                else:
                    temp = set(dominators[pred.label])
            temp.add(cfg)
            if temp != dominators[label]:
                changed = True
                dominators[label] = temp
    return dominators

def get_nearest_dominator(cfgs, dominators):
    nearest_dominators = {}
    dominators_tree = {}
    for label in cfgs.keys():
        nearest_dominators[label] = None
        dominators_tree[label] = set()
    for label, cfg in cfgs.items():
        if not cfg.pred:
            continue
        preds = cfg.pred
        end = False
        while not end:
            for dominator in dominators[label] - {cfg}:
                # 可以证明对于每一个不为开始节点的CFG节点，有且仅有一个最近支配者。
                if dominator in preds:
                    nearest_dominators[label] = dominator
                    dominators_tree[dominator.label].add(cfg)
                    end = True
                    break
            else:
                new_preds = set()
                for pred in preds:
                    # 可以证明支配当前节点的CFG节点必定支配当前节点的前驱节点。
                    new_preds |= dominators[pred.label]
                preds = new_preds
    return nearest_dominators, dominators_tree

def get_dominance_frontiers(cfgs, nearest_dominators):
    dominance_frontiers = {}
    for label in cfgs.keys():
        dominance_frontiers[label] = set()
    for label, cfg in cfgs.items():
        if len(cfg.pred) <= 1:
            continue
        for pred in cfg.pred:
            runner = pred
            while runner and runner != nearest_dominators[label]:
                dominance_frontiers[runner.label].add(cfg)
                runner = nearest_dominators[runner.label]
    return dominance_frontiers

def get_global_vars(cfgs):
    global_vars = set()
    var_defs = {}
    for cfg in cfgs.values():
        varkill = set()
        for i in cfg.instructions:
            if isinstance(i, Op):
                if isinstance(i.left, Register) and i.left not in varkill:
                    global_vars.add(i.left)
                if isinstance(i.right, Register) and i.right not in varkill:
                    global_vars.add(i.right)
            elif isinstance(i, Call):
                for arg in i.args:
                    if isinstance(arg, Register) and arg not in varkill:
                        global_vars.add(arg)
            else:
                continue
            varkill.add(i.res)
            if i.res in var_defs:
                var_defs[i.res].add(cfg)
            else:
                var_defs[i.res] = {cfg}
    return global_vars, var_defs

def add_phi_function(dominators_frontiers, global_vars, var_defs):
    for var in global_vars:
        worklist = list(var_defs[var])
        for block in worklist:
            for df in dominators_frontiers[block.label]:
                if var not in df.phi:
                    df.phi[var] = Phi(var, {})
                    worklist.append(df)

def new_name(var, counter, stack):
    if var not in counter:
        counter[var] = 0
        stack[var] = []
    i = counter[var]
    counter[var] += 1
    stack[var].append(i)
    return Register(var + str(i))

def rename_variables(cfg, counter, stack, dominators_tree):
    for phi in cfg.phi.values():
        phi.res = new_name(phi.res.name, counter, stack)
    for i in cfg.instructions:
        if isinstance(i, Op):
            if isinstance(i.left, Register):
                i.left  = Register(i.left.name + str(stack[i.left.name][-1]))
            if isinstance(i.right, Register):
                i.right = Register(i.right.name + str(stack[i.right.name][-1]))
            i.res = new_name(i.res.name, counter, stack)
        elif isinstance(i, Br):
            if isinstance(i.cond, Register):
                i.cond = Register(i.cond.name + str(stack[i.cond.name][-1]))
        elif isinstance(i, Call):
            for index, arg in enumerate(i.args):
                if isinstance(arg, Register):
                    i.args[index] = Register(arg.name + str(stack[arg.name][-1]))
    for succes in cfg.succes:
        for var, phi in succes.phi.items():
            phi.args[cfg.label] = Register(var.name + str(stack[var.name][-1]))
    for succes in dominators_tree[cfg.label]:
        rename_variables(succes, counter, stack, dominators_tree)
    for i in cfg.instructions:
        if not isinstance(i, Op):
            continue
        stack[i.res.name[:-1]].pop()
    for phi in cfg.phi.values():
        stack[phi.res.name[:-1]].pop()

def build_ssa(instructions):
    cfgs = build_cfg(instructions)
    dominators = get_dominators(cfgs)
    nearest_dominators, dominators_tree = get_nearest_dominator(cfgs, dominators)
    dominators_frontiers = get_dominance_frontiers(cfgs, nearest_dominators)
    global_vars, var_defs = get_global_vars(cfgs)
    add_phi_function(dominators_frontiers, global_vars, var_defs)
    rename_variables(cfgs["main"], {}, {}, dominators_tree)
    return cfgs

def change_def_use_chain(var, instruction, def_use_chain):
    if isinstance(var, Register):
        if var not in def_use_chain:
            def_use_chain[var] = []
        def_use_chain[var].append(instruction)

def build_def_use_chain(cfgs):
    def_use_chain = {}
    for cfg in cfgs.values():
        for phi in cfg.phi.values():
            for arg in phi.args.values():
                change_def_use_chain(arg, phi, def_use_chain)
        for i in cfg.instructions:
            if isinstance(i, Op):
                change_def_use_chain(i.left, i, def_use_chain)
                change_def_use_chain(i.right, i, def_use_chain)
            elif isinstance(i, Br):
                change_def_use_chain(i.cond, i, def_use_chain)
            elif isinstance(i, Call):
                for arg in i.args:
                    change_def_use_chain(arg, i, def_use_chain)
    return def_use_chain

def constant_folding(cfg):
    res = False
    op_dict = {
        OpType.ADD: lambda x, y: x + y,
        OpType.LE: lambda x, y: x <= y
    }
    for i in cfg.instructions:
        if not isinstance(i, Op):
            continue
        if isinstance(i.left, Constant) and isinstance(i.right, Constant):
            res = True
            i.left = Constant(op_dict[i.op](i.left.value, i.right.value))
            i.right = None
            i.op = OpType.ASSIGN
    return res

def change_use(instruction, old_register, new_register):
    if isinstance(instruction, Op):
        if instruction.left == old_register:
            instruction.left = new_register
        if instruction.right == old_register:
            instruction.right = new_register
    elif isinstance(instruction, Br):
        if instruction.cond == old_register:
            instruction.cond = new_register
    elif isinstance(instruction, Call):
        for index, arg in enumerate(instruction.args):
            if arg == old_register:
                instruction.args[index] = new_register
    elif isinstance(instruction, Phi):
        new_args = {}
        for name, arg in instruction.args.items():
            if arg == old_register:
                new_args[name] = new_register
            else:
                new_args[name] = arg
        instruction.args = new_args

def replication_propagation(cfg, def_use_chain):
    res = False
    new_phi = {}
    for name, phi in cfg.phi.items():
        if len(phi.args) > 1:
            new_phi[name] = phi
            continue
        arg = list(phi.args.values())[0]
        if not isinstance(arg, Register):
            new_phi[name] = phi
            continue
        res = True
        for use in def_use_chain[phi.res]:
            change_use(use, phi.res, arg)
    cfg.phi = new_phi
    new_instructions = []
    for i in cfg.instructions:
        if not isinstance(i, Op):
            new_instructions.append(i)
            continue
        if i.op != OpType.ASSIGN:
            new_instructions.append(i)
            continue
        if not isinstance(i.left, Register):
            new_instructions.append(i)
            continue
        res = True
        for use in def_use_chain[i.res]:
            change_use(use, i.res, i.left)
    cfg.instructions = new_instructions
    return res

def constant_propagation(cfg, def_use_chain):
    res = False
    new_phi = {}
    for name, phi in cfg.phi.items():
        if len(phi.args.keys()) > 1:
            new_phi[name] = phi
            continue
        arg = list(phi.args.values())[0]
        if not isinstance(arg, Constant):
            new_phi[name] = phi
            continue
        res = True
        for use in def_use_chain[phi.res]:
            change_use(use, phi.res, arg)
    cfg.phi = new_phi
    new_instructions = []
    for i in cfg.instructions:
        if not isinstance(i, Op):
            new_instructions.append(i)
            continue
        if i.op != OpType.ASSIGN:
            new_instructions.append(i)
            continue
        if not isinstance(i.left, Constant):
            new_instructions.append(i)
            continue
        res = True
        for use in def_use_chain[i.res]:
            change_use(use, i.res, i.left)
    cfg.instructions = new_instructions
    return res

def remove_dead_assignment(cfg, def_use_chain):
    res = False
    for i in cfg.instructions:
        if not isinstance(i, Op):
            continue
        if not def_use_chain.get(i.res, []):
            res = True
            cfg.instructions.remove(i)
    return res

def remove_unreachable_cfg(cfgs):
    new_cfgs = {}
    for label, cfg in cfgs.items():
        if not cfg.pred and cfg.label != "main":
            for succes in cfg.succes:
                succes.pred.remove(cfg)
            continue
        if cfg.instructions:
            new_cfgs[label] = cfg
        else:
            for succes in cfg.succes:
                succes.pred.remove(cfg)
                for pred in cfg.pred:
                    pred.succes.remove(cfg)
                    pred.succes.add(succes)
                    succes.pred.add(pred)
    return new_cfgs

def remove_edge(cfg, then_cfg):
    cfg.succes.remove(then_cfg)
    then_cfg.pred.remove(cfg)
    for succes in then_cfg.succes:
        for phi in succes.phi.values():
            new_args = {}
            for label, value in phi.args.items():
                if label == then_cfg.label:
                    continue
                else:
                    new_args[label] = value
            phi.args = new_args

def constant_condition(cfg, cfgs):
    res = False
    for i in cfg.instructions:
        if not isinstance(i, Br):
            continue
        if isinstance(i.cond, Constant):
            res = True
            if i.cond.value and i.else_ in cfgs:
                remove_edge(cfg, cfgs[i.else_])
            elif i.then in cfgs:
                remove_edge(cfg, cfgs[i.then])
            i.cond = None
    return res

def remove_jump_cfg(cfgs):
    new_cfgs = {}
    for label, cfg in cfgs.items():
        if len(cfg.instructions) == 1 and len(cfgs) > 1:
            i = cfg.instructions[0]
            if isinstance(i, Br) and not i.cond:
                if i.then in cfgs:
                    cfgs[i.then].pred.remove(cfg)
                    for pred in cfg.pred:
                        pred.succes.remove(cfg)
                        pred.succes.add(cfgs[i.then])
                        cfgs[i.then].pred.add(pred)
                else:
                    for pred in cfg.pred:
                        pred.succes.remove(cfg)
                continue
        new_cfgs[label] = cfg
    return new_cfgs

def optimize(cfgs, def_use_chain):
    changed = True
    while changed:
        changed = False
        cfgs = remove_unreachable_cfg(cfgs)
        for cfg in cfgs.values():
            cond1 = constant_folding(cfg)
            cond2 = replication_propagation(cfg, def_use_chain)
            cond3 = constant_propagation(cfg, def_use_chain)
            cond4 = remove_dead_assignment(cfg, def_use_chain)
            cond5 = constant_condition(cfg, cfgs)
            cond = cond1 | cond2 | cond3 | cond4 | cond5
            changed |= cond
    cfgs = remove_jump_cfg(cfgs)
    return cfgs

code = [
    Label("main"),
    Op(OpType.ASSIGN, Constant(1), None, Register("a")),
    Op(OpType.ASSIGN, Constant(2), None, Register("b")),
    Op(OpType.LE, Register("a"), Register("b"), Register("c")),
    Br(Register("c"), "then", "else"),
    Label("then"),
    Op(OpType.ASSIGN, Constant(3), None, Register("d")),
    Br(None, "endif", None),
    Label("else"),
    Op(OpType.ASSIGN, Constant(4), None, Register("d")),
    Br(None, "endif", None),
    Label("endif"),
    Call("print", [Register("d")], None)
]