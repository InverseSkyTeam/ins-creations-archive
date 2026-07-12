from __future__ import annotations
import enum
import sys
from typing import Any

sys.setrecursionlimit(10)


class VMError(Exception):
    """The exception raised when an error occurs in the VM."""

    ...


class OpCode(enum.Enum):
    """The opcodes for the bytecode."""

    POP = 0  # Pop the top of the stack.
    LOAD_CONST = 1  # Load a value onto the stack.
    LOAD_VAR = 2  # Load a variable onto the stack.

    NEW_VAR = 3  # Create a new variable.
    STORE_VAR = 4  # Store a value in a variable.
    DEL_VAR = 5

    CALL = 6  # Call a function.
    RET = 7  # Return from a function.

    FN = 8  # Define a function.
    END_FN = 9  # End a function.

    JMP = 10
    JN = 11
    JNZ = 12

    LABEL = 13

    ADD = 14
    SUB = 15
    MUL = 16
    DIV = 17

    CMP_GT = 18
    CMP_LT = 19
    CMP_EQ = 20
    CMP_NEQ = 21
    CMP_GTE = 22
    CMP_LTE = 23

    TRACE = 24
    EXIT = 25

    PRINT = 26


def exec_(code: list[tuple[Any, ...]]) -> None:
    NIL = object()
    code = code.copy()
    v_stack = []
    # fn_name fn_begin fn_end
    call_frame = [("__global__", NIL, NIL)]
    env = [{}]
    cur_pos = 0
    while cur_pos < len(code):
        inst = code[cur_pos]
        inst_name: OpCode = inst[0]
        inst_args = inst[1:] if len(inst) > 1 else []
        if call_frame[-1][-1] is not NIL and cur_pos > call_frame[-1][-1]:  # type: ignore
            raise VMError("Ret expected")
        match inst_name:
            case OpCode.POP:
                v_stack.pop()
            case OpCode.LOAD_CONST:
                v_stack.extend(inst_args)
            case OpCode.LOAD_VAR:
                v_stack.append(env[-1][inst_args[0]])
            case OpCode.NEW_VAR:
                env[-1][inst_args[0]] = NIL
            case OpCode.STORE_VAR:
                env[-1][inst_args[0]] = v_stack.pop()
            case OpCode.DEL_VAR:
                del env[-1][inst_args[0]]
            case OpCode.CALL:
                # load function body
                fn_body = env[-1][inst_args[0]]
                # insert fn body after this instruction
                # TODO: too slow!
                for index in range(len(fn_body)):
                    code.insert(cur_pos + index + 1, fn_body[index])
                # update call frame
                call_frame.append((fn_name, cur_pos + 1, cur_pos + len(fn_body) + 1))
                # update env
                env.append({inst_args[0]: fn_body})
                # print(code)

            case OpCode.RET:
                # pop call frame
                cur_call = call_frame.pop()
                # remove function body
                del code[cur_call[1] : cur_call[2]]

                # in the top frame already, can't return
                # make linter happy
                assert isinstance(cur_call[1], int), "Unexpected RET"
                # restore cur_pos ptr
                cur_pos: int = cur_call[1] - 1
                # restore env
                env.pop()
                # print(code)

            case OpCode.FN:
                fn_name = inst_args[0]
                fn_body = []
                cur_pos += 1
                while cur_pos < len(code):
                    if code[cur_pos][0] == OpCode.END_FN:
                        break
                    else:
                        fn_body.append(code[cur_pos])
                    cur_pos += 1
                env[-1][fn_name] = fn_body
                # del code[cur_pos : cur_pos + len(fn_body)]
                # cur_pos -= 1
            case OpCode.END_FN:
                raise VMError("Unexpected END_FN")
            case OpCode.JMP:
                label_name = inst_args[0]
                # TODO: too slow!
                for index in range(len(code)):
                    if code[index][0] == OpCode.LABEL and code[index][1] == label_name:
                        cur_pos = index
                        break
            case OpCode.JN:
                if not v_stack.pop():
                    label_name = inst_args[0]
                    # TODO: too slow!
                    for index in range(len(code)):
                        if (
                            code[index][0] == OpCode.LABEL
                            and code[index][1] == label_name
                        ):
                            cur_pos = index
                            break
            case OpCode.JNZ:
                if v_stack.pop():
                    label_name = inst_args[0]
                    # TODO: too slow!
                    for index in range(len(code)):
                        if (
                            code[index][0] == OpCode.LABEL
                            and code[index][1] == label_name
                        ):
                            cur_pos = index
                            break
            case OpCode.LABEL:
                # ignored
                pass
            case OpCode.CMP_GT:
                v_stack.append(v_stack.pop() > v_stack.pop())
            case OpCode.CMP_LT:
                v_stack.append(v_stack.pop() < v_stack.pop())
            case OpCode.CMP_EQ:
                v_stack.append(v_stack.pop() == v_stack.pop())
            case OpCode.CMP_NEQ:
                v_stack.append(v_stack.pop() != v_stack.pop())
            case OpCode.CMP_GTE:
                v_stack.append(v_stack.pop() >= v_stack.pop())
            case OpCode.CMP_LTE:
                v_stack.append(v_stack.pop() <= v_stack.pop())
            case OpCode.ADD:
                v_stack.append(v_stack.pop() + v_stack.pop())
            case OpCode.SUB:
                v_stack.append(v_stack.pop() - v_stack.pop())
            case OpCode.MUL:
                v_stack.append(v_stack.pop() * v_stack.pop())
            case OpCode.DIV:
                v_stack.append(v_stack.pop() * v_stack.pop())
            case OpCode.TRACE:
                print(f"***DEBUG*** CURRENT STACK: {v_stack}")
                # print(f"***DEBUG*** CURRENT ENV: {env}")
                # print(f"***DEBUG*** CURRENT CALL FRAME: {call_frame}")
            case OpCode.EXIT:
                break
            case OpCode.PRINT:
                print(v_stack.pop())
            case _:
                raise VMError(f"Unknown opcode: {inst_name} {inst_args}")
        cur_pos += 1


# if __name__ == "__main__":
# exec_(
#     [
#         (OpCode.FN, "greet"),
#         (OpCode.LOAD_CONST, 1),
#         (OpCode.LOAD_CONST, 2),
#         (OpCode.ADD,),
#         (OpCode.STORE_VAR, "a"),
#         (OpCode.TRACE,),
#         (OpCode.RET,),
#         (OpCode.END_FN,),
#         (OpCode.CALL, "greet"),
#         (OpCode.TRACE,),
#     ]
# )

# exec_([(OpCode.LABEL, "begin"), (OpCode.TRACE,), (OpCode.JMP, "begin")])
exec_(
    [
        (OpCode.FN, "add"),
        # (OpCode.TRACE,),
        (OpCode.STORE_VAR, "a"),
        (OpCode.LOAD_VAR, "a"),
        (OpCode.LOAD_CONST, 0),
        (OpCode.CMP_LT,),
        (OpCode.JNZ, "greater_than_zero"),
        (OpCode.LOAD_CONST, 0),
        # (OpCode.TRACE,),
        (OpCode.RET,),
        (OpCode.LABEL, "greater_than_zero"),
        (OpCode.LOAD_CONST, 1),
        (OpCode.LOAD_VAR, "a"),
        (OpCode.SUB,),
        (OpCode.CALL, "add"),
        (OpCode.LOAD_VAR, "a"),
        (OpCode.ADD,),
        (OpCode.RET,),
        (OpCode.END_FN,),
        (OpCode.LOAD_CONST, 1000),
        (OpCode.CALL, "add"),
        (OpCode.PRINT,),
    ]
)
