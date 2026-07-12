from enum import Enum
import re

class State(Enum):
    INIT = "INIT"
    ADD = "ADD"
    SUB = "SUB"
    MUL = "MUL"
    DIV = "DIV"
    MOD = "MOD"
    POWER = "POWER"
    EQUAL = "EQUAL"
    LESS = "LESS"
    GREATER = "GREATER"
    LESSEQUAL = "LESSEQUAL"
    GREATEREQUAL = "GREATEREQUAL"
    NOTEQUAL = "NOTEQUAL"
    ASSIGN = "ASSIGN"
    SEMI = "SEMI"
    ENDL = "ENDL"
    COLON = "COLON"
    COMMA = "COMMA"
    DOT = "DOT"
    ARROW = "ARROW"
    LBR = "LBR"
    RBR = "RBR"
    LMID = "LMID"
    RMID = "RMID"
    LPARAN = "LPARAN"
    RPARAN = "RPARAN"
    LINEDOWN = "LINEDOWN"
    NUMBER = "NUMBER"
    STRING = "STRING"
    VARIABLE = "VARIABLE"
    END = "END"


# 类型Token
class TokenType(Enum):
    ADD = "+"
    SUB = "-"
    MUL = "*"
    DIV = "/"
    MOD = "%"
    POWER = "^"
    EQUAL = "=="
    LESS = "<"
    GREATER = ">"
    LESSEQUAL = "<="
    GREATEREQUAL = ">="
    NOTEQUAL = "!="
    ASSIGN = "="
    SEMI = ";"
    ENDL = "\n"
    COLON = ":"
    COMMA = ","
    DOT = "."
    ARROW = "->"
    LBR = "("
    RBR = ")"
    LMID = "["
    RMID = "]"
    LPARAN = "{"
    RPARAN = "}"
    LINEDOWN = "|"

    VARIABLE = "VARIABLE"
    END = "END"
    NUMBER = "NUMBER"
    STR = "STR"

    LET = "LET"
    CONST = "CONST"
    IF = "IF"
    ELIF = "ELIF"
    ELSE = "ELSE"
    SWITCH = "SWITCH"
    CASE = "CASE"
    DEFAULT = "DEFAULT"
    WHILE = "WHILE"
    LOOP = "LOOP"
    FOR = "FOR"
    IN ="IN"
    BREAK = "BREAK"
    CONTINUE = "CONTINUE"
    FUN = "FUN"
    RETURN = "RETURN"
    FUNC = "FUNC"
    IMPORT = "IMPORT"
    AS = "AS"
    DEBUGGER = "DEBUGGER"
    AND = "AND"
    OR = "OR"
    NOT = "NOT"
    
    
CONFIG = {
    "initial":State.INIT,
    "states":{
        State.INIT:{
            "isend":False,
            "trans":[
                {
                    "state":State.NUMBER,
                    "checker":re.compile("[0-9]")
                },
                {
                    "state":State.ADD,
                    "checker":"+"
                }
            ]
        },
        State.NUMBER:{
            "isend":True,
            "token":TokenType.NUMBER,
            "trans":[
                {
                    "state":State.NUMBER,
                    "checker":re.compile("[0-9\.]")
                }
            ]
        },
        State.ADD: {
            "isend":True,
            "token":TokenType.ADD,
            "trans":[
                
            ]
        }
    }
}