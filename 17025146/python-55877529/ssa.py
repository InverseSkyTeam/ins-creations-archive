from enum import Enum
from dataclasses import dataclass
from typing import Any, Set, Optional

class Block:
    Id = 0
    def __init__(self):
        self.id = Block.Id
        Block.Id += 1
        self.phi_funcs = {}
        self.pred = set()
        self.succes = set()
        self.code = []

    def __hash__(self):
        return hash(id(self))

class OpType(Enum):
    LABEL = 1
    JMP = 2
    JZ = 3
    JNZ = 4
    ASSIGN = 5
    ADD = 6
    LE = 7

@dataclass
class Instruction:
    op: OpType
    left: Any
    right: Any = None
    res: Optional[str] = None

@dataclass
class Phi:
    var: str
    args: Set[str]

def create_cfg(code):
    labels = {}
    start = current = Block()
    block_list = [start]
    requires = {}
    for command in code:
        if command.op == OpType.LABEL:
            if current.code:
                new_block = Block()
                new_block.code.append(command)
                current.succes.add(new_block)
                new_block.pred.add(current)
                block_list.append(new_block)
                current = new_block
            else:
                current.code.append(command)
            labels[command.left] = current
            if command.left in requires:
                for block in requires[command.left]:
                    block.succes.add(current)
                    current.pred.add(block)
                del requires[command.left]
        else:
            current.code.append(command)
            if command.op == OpType.JMP:
                if command.left in labels:
                    jmp_block = labels[command.left]
                    current.succes.add(jmp_block)
                    jmp_block.pred.add(current)
                elif command.left in requires:
                    requires[command.left].add(current)
                else:
                    requires[command.left] = {current}
                current = Block()
                block_list.append(current)
            elif command.op in (OpType.JZ, OpType.JNZ):
                if command.left in labels:
                    jmp_block = labels[command.left]
                    current.succes.add(jmp_block)
                    jmp_block.pred.add(current)
                elif command.left in requires:
                    requires[command.left].add(current)
                else:
                    requires[command.left] = {current}
                new_block = Block()
                new_block.pred.add(current)
                current.succes.add(new_block)
                block_list.append(new_block)
                current = new_block
    return block_list

def calc_dom(block_list):
    dom_list = []
    for block in block_list:
        dom_list.append({block})
    changed = True
    while changed:
        changed = False
        for block in block_list:
            temp = {block}
            for pred in block.pred:
                temp |= dom_list[pred.id]
            if temp != dom_list[block.id]:
                dom_list[block.id] = temp
                changed = True
    return dom_list

def calc_idom(block_list, dom_list):
    idom_list = []
    for _ in range(len(block_list)):
        idom_list.append(None)
    for block in block_list:
        if not block.pred:
            idom_list[block.id] = None
            continue
        preds = block.pred
        nearest_dom = None
        end = False
        while not end:
            doms = dom_list[block.id] - {block}
            for dom in doms:
                # 可以证明对于任何不为开始节点的block，有且仅有一个idom。
                if dom in preds:
                    nearest_dom = dom
                    end = True
                    break
            if not end:
                new_preds = set()
                for pred in preds:
                    new_preds |= pred.pred
                preds = new_preds
        idom_list[block.id] = nearest_dom
    return idom_list

def calc_df(block_list, idom_list):
    df_list = []
    for _ in range(len(block_list)):
        df_list.append(set())
    for block in block_list:
        if len(block.pred) > 1:
            for pred in block.pred:
                runner = pred
                while runner and runner != idom_list[block.id]:
                    df_list[runner.id].add(block)
                    runner = idom_list[runner.id]
    return df_list

def calc_globals(block_list):
    global_set = set()
    var_blocks = {}
    for block in block_list:
        varkill = set()
        for com in block.code:
            if com.res is None:
                continue
            if isinstance(com.left, str) and com.left not in varkill:
                global_set.add(com.left)
            if isinstance(com.right, str) and com.right not in varkill:
                global_set.add(com.right)
            varkill.add(com.res)
            if com.res in var_blocks:
                var_blocks[com.res].add(block)
            else:
                var_blocks[com.res] = {block}
    return global_set, var_blocks

def add_phi(df_list, global_set, var_blocks):
    for var in global_set:
        worklist = list(var_blocks[var])
        for b in worklist:
            for d in df_list[b.id]:
                if var not in d.phi_funcs:
                    d.phi_funcs[var] = Phi(var, set())
                    worklist.append(d)

def calc_tree(block_list, idom_list):
    tree = []
    for _ in range(len(block_list)):
        tree.append(set())
    for block in block_list:
        if not idom_list[block.id]:
            continue
        # 对idom_list进行转置，得到支配者树
        tree[idom_list[block.id].id].add(block)
    return tree

def newname(var, counter, stack):
    if var in counter:
        i = counter[var]
        counter[var] += 1
        stack[var].append(i)
    else:
        i = 0
        counter[var] = 1
        stack[var] = [0]
    return var + str(i)

def rename(block, counter, stack, tree):
    for name, phi in block.phi_funcs.items():
        new_name = newname(name, counter, stack)
        phi.var = new_name
    for command in block.code:
        if command.op in (OpType.JMP, OpType.LABEL):
            continue
        if command.op in (OpType.JZ, OpType.JNZ):
            command.right = command.right + str(stack[command.right][-1])
            continue
        if isinstance(command.left, str):
            command.left = command.left + str(stack[command.left][-1])
        if isinstance(command.right, str):
            command.right = command.right + str(stack[command.right][-1])
        new_name = newname(command.res, counter, stack)
        command.res = new_name
    for succes in block.succes:
        for name, phi in succes.phi_funcs.items():
            phi.args.add(name + str(stack[name][-1]))
    for s in tree[block.id]:
        rename(s, counter, stack, tree)
    for command in block.code:
        if not command.res:
            continue
        stack[command.res[:-1]].pop()
    for phi in block.phi_funcs.values():
        stack[phi.var[:-1]].pop()

def rename_vars(block_list, tree, global_set):
    counter = {}
    stack = {}
    for var in global_set:
        counter[var] = 0
        stack[var] = []
    rename(block_list[0], counter, stack, tree)

def code_to_ssa(code):
    block_list = create_cfg(code) # 从IR构建CFG
    dom_list = calc_dom(block_list) # 计算每个CFG节点的Dom集合
    idom_list = calc_idom(block_list, dom_list) # 计算每个CFG节点的支配者
    df_list = calc_df(block_list, idom_list) # 计算支配边界
    global_set, var_blocks = calc_globals(block_list) # 计算全局变量集合
    add_phi(df_list, global_set, var_blocks) # 添加Phi函数
    tree = calc_tree(block_list, idom_list) # 计算支配者树
    rename_vars(block_list, tree, global_set) # 重命名变量
    return block_list