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