from plpg import *

rule = Rule("""
@ignore " \t\r\n";
number : /[0-9](\\.[0-9][0-9]?)?/;
@priority "+" 1 left;
@priority "-" 1 left;
@priority "*" 0 left;
@priority "/" 0 left;
S    ->   Expr {output};
Expr ->   Expr "+" Expr {add}
        | Expr "-" Expr {sub}
        | Expr "*" Expr {mul}
        | Expr "/" Expr {div}
        | "(" Expr ")" {group}
        | number {number}
        ;
""")

class Calclator(Parser):
    def output(self, args):
        print(args[0])
    def add(self, args):
        return args[0] + args[1]
    def sub(self, args):
        return args[0] - args[1]
    def mul(self, args):
        return args[0] * args[1]
    def div(self, args):
        return args[0] / args[1]
    def group(self, args):
        return args[0]
    def number(self, args):
        val = args[0].value
        return int(val) if val.isdigit() else float(val)

calc = Calclator(rule)
calc.parse("(1+2)*3")