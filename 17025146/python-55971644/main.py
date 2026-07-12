from svm import *

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

print("这是优化以前的IR:")
for i in code:
    print(i)
print("它等价于如下代码:")
print("""a = 1
b = 2
if a < b:
    d = 3
else:
    d = 4
print(d)
""")
print("显然这是一大段废话,我们都知道最终结果一定是print(3),好在代码优化器也知道.\n")
ssa = build_ssa(code)
def_use_chain = build_def_use_chain(ssa)
optimized = optimize(ssa, def_use_chain)

print("这是优化以后的IR:")
for label, cfg in optimized.items():
    for i in cfg.instructions:
        print(i)
print("它等价于如下代码:")
print("print(3)\n")
print("Amazing!优化器成功在不改变代码原意的前提下将代码优化到最短,从而去掉了大量冗余,这正是我们想要的.")