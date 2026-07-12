import os
import sys


comment = (";","%")
code = []
stack = []
var_table = {}
label_table = {}
func_table = {}
eip = 0
printout = []

class Do():
    def do_var(arg):
        if arg == "":return
        for var in arg.split(","):
            var = var.strip()
            if not is_var_name(var) or var in var_table:
                run_error("Wrong var name")
            var_table[var] = len(stack)
            var_table[len(stack)] = var
            stack.append("/")
    def do_push(arg):
        if arg.isdigit():
            arg = int(arg)
        else:
            if arg in var_table:
                arg = stack[var_table[arg]]
            else:
                run_error("Undefined variable")
            if not isinstance(arg,int):
                run_error("Cannot push uninitialed value")
        stack.append(arg)
    def do_pop(arg):
        value = stack.pop()
        if arg == "":return
        if not isinstance(value,int):
            run_error("Cannot pop non-number value to variable")
        if arg in var_table:
            stack[var_table[arg]] = value
        else:
            run_error("Undefined variable")
    def do_exit(arg):
        global going,exit_code
        going = False
        if arg == "~":
            exit_code = stack[-1]
        elif arg:
            if arg.isdigit():
                exit_code = int(arg)
            else:
                if arg in var_table:
                    exit_code = stack[var_table[arg]]
                else:
                    run_error("Undefined variable")
        if not isinstance(exit_code,int):
            run_error("Wrong exit code")
        sys.exit(exit_code)
    def do_add(arg):stack[-2] += stack[-1]; stack.pop()
    def do_sub(arg):stack[-2] -= stack[-1]; stack.pop()
    def do_mul(arg):stack[-2] *= stack[-1]; stack.pop()
    def do_div(arg):stack[-2] /= stack[-1]; stack.pop()
    def do_mod(arg):stack[-2] %= stack[-1]; stack.pop()
    def do_and(arg):stack[-2] = int(stack[-2]!=0 and stack[-1]!=0); stack.pop()
    def do_or(arg):stack[-2] = int(stack[-2]!=0 or  stack[-1]!=0); stack.pop()
    def do_cmpeq(arg):stack[-2] = int(stack[-2]==stack[-1]);stack.pop()
    def do_cmpne(arg):stack[-2] = int(stack[-2]!=stack[-1]);stack.pop()
    def do_cmpgt(arg):stack[-2] = int(stack[-2]>stack[-1]); stack.pop()
    def do_cmplt(arg):stack[-2] = int(stack[-2]<stack[-1]); stack.pop()
    def do_cmpge(arg):stack[-2] = int(stack[-2]>=stack[-1]);stack.pop()
    def do_cmple(arg):stack[-2] = int(stack[-2]<=stack[-1]);stack.pop()
    def do_neg(arg):stack[-1] = -stack[-1]
    def do_not(arg):stack[-1] = int(not stack[-1])
    def do_print(fmt):
        if len(fmt) <2 or fmt[0] != fmt[-1] or fmt[0] not in ("'",'"'):
            run_error("Format string error")
        argc = fmt.count("%d")
        out = fmt.strip('"').strip("'") % tuple(stack[len(stack) - argc:])
        sys.stdout.write(str(out) + "\n")
        printout.append(out)
        del stack[len(stack)-argc:]
    def do_readint(msg):
        if len(msg) < 2 or msg[0] != msg[-1] or msg[-1] not in ("'",'"'):
            run_error("Message string error")
        msg = msg.strip('"').strip("'")
        string = input(msg)
        if value.isdigit():
            value = int(string)
        else:
            value = 0
        stack.append(value)
        printout.append("\n  " + msg + str(value))
    def do_jmp(label):
        global eip
        if label in label_table:
            eip = label_table[label] - 1
        else:
            run_error("Wrong label")
    def do_jz(label):
        global eip
        if label in label_table:
            new_eip = label_table[label] - 1
        else:
            run_error("Wrong label")
        if stack.pop() == 0:
            eip = new_eip
    def do_ret(arg):
        global var_table,eip
        if arg == "~":
            retval = stack[-1]
        elif arg:
            if arg.isdigit():
                retval = int(arg)
            else:
                if arg in var_table:
                    retval = stack[var_table[arg]]
                else:
                    run_error("Undefined variable")
        else:
            retval = "/"
        i = len(stack) - 1
        while not isinstance(stack[i],tuple):
            i -= 1
        argc,eip,var_table = stack[i]
        del stack[i - argc:]
        stack.append(retval)

def is_var_name(char):
    if char == "":return False
    if char[0].isalpha() or char[0] == "_":
        for ch in char:
            if not (ch.isalnum() or ch == "_"):
                return False
        return True
    else:
        return False

def code_error(line,msg):
    print(line)
    print(f"^^^Error at last line:{msg}")
    sys.exit(-1)

def run_error(msg):
    code[eip][0] = f"**{msg}**"
    printout.append(msg)
    sys.exit(-1)

def read_file(filename):
    with open(filename,"r") as file:
        code = file.readlines()
    return code

def check_label(label):
    if label == "":return False
    func,sep,funname = label.partition(" @")
    if sep:
        if func.strip() != "FUNC" or not is_var_name(funname) or funname in func_table:
            return False
        else:
            func_table[funname] = len(code)
            return True
    else:
        if not is_var_name(label) or label in func_table or label in label_table:
            return False
        else:
            label_table[label] = len(code)
            return True

def assemb(file):
    label = ""
    for line in file.split("\n"):
        line = line.strip()
        if line == "" or line[0] in comment:
            continue
        labelname,sep,ist = line.partition(":")
        if sep and '"' not in labelname and "'" not in labelname:
            labelname = labelname.strip()
            ist = ist.strip()
            if not check_label(labelname):
                code_error(line,"Wrong label")
            if label:
                label = f"{label},{labelname}"
            else:
                label = labelname
            if ist == "" or ist[0] in comment:
                continue
        elif len(line) >= 7 and line[:7] == "ENDFUNC":
            if label:
                label = f"{label},ENDFUNC"
            else:
                label = "ENDFUNC"
            ist = "ret"
        else:
            ist = line
        
        dire,sep,arg = ist.partition(" ")
        if len(dire) >4 and (dire[-4:] == ".arg" or dire[-4:] == ".var"):
            dire = dire[-3:]
        code.append([label,dire,arg.strip()])
        label = ""
    code.append(("","exit","0"))

def call(funname):
    global var_table,eip
    if funname in func_table:
        entry = func_table[funname]
    else:
        run_error("Undefined function")
    if code[entry][1] == "arg":
        arg_list = code[entry][2].split(",")
    else:
        arg_list = []
    
    new_var_table = {}
    for addr,arg in enumerate(arg_list,len(stack) - len(arg_list)):
        arg = arg.strip()
        if not is_var_name(arg) or arg in new_var_table:
            run_error("Wrong arg name")
        new_var_table[arg] = addr
        new_var_table[addr] = arg
    stack.append((len(arg_list),eip,var_table))
    var_table = new_var_table
    eip = entry if len(arg_list) else entry - 1

def run():
    global eip
    eip = 0
    del stack[:]
    while True:
        label,dire,arg = code[eip]
        if dire[0] == "$":
            action,arg = call,dire[1:]
            if not is_var_name(arg):
                run_error("Wrong identifier")
        else:
            if not is_var_name(dire):
                run_error("Wrong identifier")
            action = getattr(Do,f"do_{dire}")
            if action is None:
                run_error("Unknown instruction")
        action(arg)
        eip += 1

if __name__ == "__main__":
    expr = """
var a
push 1
push 2
add
pop a
print "%d"
    """
    assemb(expr)
    run()