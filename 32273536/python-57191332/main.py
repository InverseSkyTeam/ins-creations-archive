from __future__ import annotations
import zipfile
zipfile.ZipFile("./lark.zip").extractall("./lark")
import reprlib
from typing import Optional
import lark
import enum
from reprlib import repr


class Type:
    def __init__(self) -> None:
        raise NotImplementedError()


class Package:
    def __init__(self, name: str, parent: Optional[Package] = None) -> None:
        self.name = name
        self.parent = parent

    @property
    def is_root_package(self) -> bool:
        return self.parent is None


class PackageRef:
    def __init__(self, paths: list[str]) -> None:
        self.paths = paths
        self.package = None

    @property
    def is_resolved(self) -> bool:
        return self.package is not None

    def mark_as_resolved(self, package: Package) -> None:
        self.package = package


class IntType(Type):
    def __init__(self, bits: int = 32) -> None:
        self.bits = bits


class FloatType(Type):
    def __init__(self, bits: int = 32) -> None:
        self.bits = bits


class PointerType(Type):
    def __init__(self, target: Type) -> None:
        self.target = target


class TypeRef:
    def __init__(self, ref_type: Optional[Type] = None) -> None:
        self.ref_type = ref_type

    @property
    def resolved(self) -> bool:
        return self.ref_type is not None

    def mark_as_resolved(self, type_: Type) -> None:
        self.ref_type = type_


class RawTypeRef(TypeRef):
    def __init__(self, name: str, ref_type: Type | None = None) -> None:
        super().__init__(ref_type)
        self.name = name


class GenericTypeRef(TypeRef):
    def __init__(
        self,
        original_type_ref: TypeRef,
        generic_var_type_ref: list[TypeRef],
        ref_type: Type | None = None,
    ) -> None:
        super().__init__(ref_type)
        self.original_type_ref = original_type_ref
        self.generic_vars = generic_var_type_ref


class PointerTypeRef(TypeRef):
    def __init__(self, target_type: TypeRef, ref_type: Type | None = None) -> None:
        super().__init__(ref_type)
        self.target_type = target_type


class PackageDeclaration:
    def __init__(self, name: str) -> None:
        self.name = name


class ImportDeclaration:
    def __init__(self, path: PackageRef) -> None:
        self.path = path


@enum.unique
class FunctionAttribute(enum.Enum):
    PUBLIC = enum.auto()
    PRIVATE = enum.auto()
    EXPORT = enum.auto()


@enum.unique
class GlobalVarriableAttribute(enum.Enum):
    PUBLIC = enum.auto()
    PRIVATE = enum.auto()
    EXPORT = enum.auto()


class FunctionParam:
    def __init__(self, name: str, type_: TypeRef) -> None:
        self.name = name
        self.type = type_


class FunctionDeclaration:
    def __init__(
        self,
        name: str,
        params: list[FunctionParam],
        return_type: TypeRef,
        body: Optional[Block] = None,
        attributes: Optional[set[FunctionAttribute]] = None,
    ) -> None:
        self.name = name
        self.params = params
        self.return_type = return_type
        self.body = body
        self.has_impl = body is not None
        self.attributes = attributes


class GlobalVarriableDeclaration:
    def __init__(
        self,
        name: str,
        type_: TypeRef,
        value: Optional[Expression] = None,
        attributes: Optional[set[GlobalVarriableAttribute]] = None,
    ) -> None:
        self.name = name
        self.type_ = type_
        self.value = value
        self.has_value = value is not None
        self.attributes = attributes


class IfStatement:
    def __init__(
        self, cond: Expression, then: Block, else_: Optional[Block] = None
    ) -> None:
        self.cond = cond
        self.then = then
        self.else_ = else_
        self.has_else = else_


class WhileStatement:
    def __init__(self, cond: Expression, body: Block) -> None:
        self.cond = cond
        self.body = body


class ReturnStatement:
    def __init__(self, value: Expression) -> None:
        self.value = value


class BreakStatement:
    def __init__(self) -> None:
        pass


class ContinueStatement:
    def __init__(self) -> None:
        pass


class LetStatement:
    def __init__(
        self, name: str, type_: TypeRef, value: Optional[Expression] = None
    ) -> None:
        self.type_ = type_
        self.value = value
        self.name = name


class ExpressionStatement:
    def __init__(self, expr: Expression) -> None:
        self.value = expr


class Block:
    def __init__(self, stmts: Statement) -> None:
        self.statements = stmts


@enum.unique
class BinaryOperator(enum.Enum):
    ASSIGN = enum.auto()
    AND = enum.auto()
    OR = enum.auto()
    GREATER_THAN = enum.auto()
    LESS_THAN = enum.auto()
    GREATER_EQUAL = enum.auto()
    LESS_EQUAL = enum.auto()
    EQUAL = enum.auto()
    NOT_EQUAL = enum.auto()
    ADD = enum.auto()
    SUB = enum.auto()
    MUL = enum.auto()
    DIV = enum.auto()
    ATTR = enum.auto()


@enum.unique
class UnaryOperator(enum.Enum):
    NOT = enum.auto()


class BinaryExpression:
    def __init__(self, lhs: Expression, rhs: Expression, op: BinaryOperator) -> None:
        self.lhs, self.rhs = lhs, rhs
        self.op = op


class UnaryExpression:
    def __init__(self, op: UnaryOperator, expr: Expression) -> None:
        self.op, self.expr = op, expr


class CallExpression:
    def __init__(self, callee: Expression, args: list[Expression]) -> None:
        self.callee = callee
        self.args = args


class IndexExpression:
    def __init__(self, expr: Expression, index: Expression) -> None:
        self.expr = expr
        self.index = index


class NameRef:
    def __init__(self, name: str) -> None:
        self.name = name
        self.type_: Optional[Type] = None

    def assume(self) -> Type:
        assert self.type_ is not None
        return self.type_


class StringLiteral:
    def __init__(self, v: str) -> None:
        self.value = v


class IntegerLiteral:
    def __init__(self, v: int) -> None:
        self.value = v


class FloatLiteral:
    def __init__(self, v: float) -> None:
        self.value = v


class BooleanLiteral:
    def __init__(self, b: bool) -> None:
        self.value = b


class NullLiteral:
    def __init__(self) -> None:
        pass


# type Statement = IfStatement | WhileStatement | ReturnStatement | BreakStatement | ContinueStatement | LetStatement | ExpressionStatement | Block
# type Declaration = ImportDeclaration | PackageDeclaration | FunctionDeclaration | GlobalVarriableDeclaration
# type Expression = BinaryExpression | UnaryExpression | CallExpression | IndexExpression | NameRef | StringLiteral | IntegerLiteral | FloatLiteral | BooleanLiteral | NullLiteral


class ToAstTransformer(lark.Transformer):
    def start(self, trees):
        for t in trees:
            print(reprlib.repr(t))
        return trees

    def import_declaration(self, args):
        return ImportDeclaration(args[0])

    def composed_path(self, args):
        l: PackageRef = args[0]
        r: lark.Token = args[1]
        new_path = list(l.paths)
        new_path.append(r.value)
        return PackageRef(new_path)

    def raw_path(self, args):
        name = args[0].value
        return PackageRef([name])

    def package_declaration(self, args):
        return PackageDeclaration(args[0].value)

    @lark.v_args(True)
    def fn_def(self, attr, name, params, type, body):
        return FunctionDeclaration(name, params, type, body, attr)

    @lark.v_args(True)
    def fn_decl(self, attr, name, params, type):
        return FunctionDeclaration(name, params, type, attributes=attr)


# source = open("./grammar.lark", encoding="utf-8", mode="r")
parser = lark.Lark( # source
r"""
%import common.WS
%import common.CPP_COMMENT
%import common.C_COMMENT
%import common.SIGNED_NUMBER -> NUMBER
%import common.ESCAPED_STRING -> STRING
%import common.CNAME -> ID

%ignore WS
%ignore CPP_COMMENT
%ignore C_COMMENT

start: declaration*

?declaration: import_declaration
            | package_declaration
            | function_declaration
            | global_variable_declaration

import_declaration: "import" package_path ";"
package_declaration: "package" ID ";"
function_declaration: function_attribute* "func" ID "(" [param_list] ")" "->" type_name block -> fn_def
                    | function_attribute* "func" ID "(" [param_list] ")" "->" type_name ";" -> fn_decl
function_attribute: PUBLIC | PRIVATE | EXPORT
param_list: ID ":" type_name ("," ID ":" type_name)*
global_variable_declaration: "global" ID  ":" type_name ["=" expr] ";"

?statement: if_statement
        | while_statement
        | return_statement
        | break_statement
        | continue_statement
        | let_statement
        | expression_statement
        | block

block: "{" statement* "}"
if_statement: "if" expr block ("else" "if" expr block)* ["else" expr block]
while_statement: "while" expr block
return_statement: "return" [expr] ";"
break_statement: "break" ";"
continue_statement: "continue" ";"
let_statement: "let" ID ":" type_name ["=" expr] ";"
expression_statement: expr ";"

package_path: package_path "." ID -> composed_path
            | ID -> raw_path
type_name: type_name "." ID -> type_attr
        | "*" type_name -> ptr_type
        | type_name "[" type_name "]" -> generic_type
        | ID -> raw_type

?expr: expr "=" logic -> assign
    | logic

?logic: logic "and" compare -> and_
    | logic "or" compare -> or_
    | compare

?compare: compare ">" sum -> gt
    | compare "<" sum -> lt
    | compare ">=" sum -> ge
    | compare "<=" sum -> le
    | compare "==" sum -> eq
    | compare "!=" sum -> ne
    | sum

?sum: sum "+" product -> add
    | sum "-" product -> sub
    | product

?product: product "/" atom -> div
        | product "*" atom -> mul
        | atom

?atom : "(" expr ")"
    | "not" atom -> not_
    | atom "." primary -> dot
    | atom "[" expr "]" -> index
    | atom "(" [args] ")" -> call
    | primary

args: expr ("," expr)*

primary: NUMBER -> num
        | ID -> id
        | STRING ->string
        | TRUE -> true
        | FALSE -> false
        | NULL -> null

TRUE: "true"
FALSE: "false"
NULL: "null"
PUBLIC: "public"
EXPORT: "export"
PRIVATE: "private"
""", parser="lalr", transformer=ToAstTransformer())
tree = parser.parse(
    """
    package main;
    import stdio;
    global nothing: string = "haha";
    public func main(args: array[string] ) -> int {
        print("hello world");
        return 0;
    }       
    """
)
