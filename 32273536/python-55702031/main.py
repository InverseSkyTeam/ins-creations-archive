from llvmlite import ir
from ctypes import CFUNCTYPE, c_double
import llvmlite.binding as llvm

llvm.initialize()
llvm.initialize_native_target()
llvm.initialize_native_asmprinter()

# Create some useful types
double = ir.DoubleType()
fnty = ir.FunctionType(double, (double, double))

# Create an empty module...
module = ir.Module(name=__file__)
# and declare a function named "fpadd" inside it
func = ir.Function(module, fnty, name="fpadd")

# Now implement the function
block = func.append_basic_block(name="entry")
builder = ir.IRBuilder(block)
a, b = func.args
result = builder.fadd(a, b, name="res")
builder.ret(result)

llvm_ir = str(module)
print(llvm_ir)

def create_execution_engine():
    # Create a target machine representing the host
    target = llvm.Target.from_default_triple()
    target_machine = target.create_target_machine()
    # And an execution engine with an empty backing module
    backing_mod = llvm.parse_assembly("")
    engine = llvm.create_mcjit_compiler(backing_mod, target_machine)
    return engine
    
engine = create_execution_engine()
mod = llvm.parse_assembly(llvm_ir)
mod.verify()
# Now add the module and make sure it is ready for execution
engine.add_module(mod)
engine.finalize_object()
engine.run_static_constructors()

func_ptr = engine.get_function_address("fpadd")
cfunc = CFUNCTYPE(c_double, c_double, c_double)(func_ptr)
res = cfunc(1.0, 3.5)
print("fpadd(...) =", res)