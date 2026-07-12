###############################################################################
#  DrawAST Tree    绘图仪
###############################################################################

from pyecharts import options as opts
from pyecharts.charts import Page, Tree

class NodeVisitor(object):
    def visit(self, node):
        # 获取节点类型名称组成访问器方法名（子类Interpreter中方法的名称）
        method_name = 'visit_' + type(node).__name__
        # 获取访问器对象，找不到访问器时获取“generic_visit”
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception('No visit_{} method'.format(type(node).__name__))

class DrawASTtreeImg(NodeVisitor):  # 添加符号表生成器类
    def __init__(self, tree): 
        self.tree = tree  
        self.ASTdata = []  
   
    def visit_Program(self, node):
        blockdata=self.visit(node.compound)
        Programdata={"children":blockdata,"name": "Program："+node.name}
        data=[Programdata]
        return data

    def visit_Assign(self, node):
        vardata=self.visit_Variable(node.var_node)
        Typedata=self.visit_VarType(node.type_node)
        VarDecldata={"children":vardata+Typedata,"name": "Assign"}
        return VarDecldata
    
    def visit_ManyAssign(self, node):
        dt=[]
        for i in node.children:
            dt.append(self.visit_Assign(i))
        VarDecldata={"children":dt,"name": "ManyAssign"}
        return VarDecldata

    def visit_Sout(self, node):
        dt=[]
        for i in node.params:
            try:
                dt.append(self.visit(i)[0])
            except:
                dt.append(self.visit(i))
        Dt={"children":dt,"name": "Sout"}
        return Dt

    def visit_Srin(self, node):
        dt=[]
        for i in node.params:
            dt.append(self.visit(i)[0])
        Dt={"children":dt,"name": "Srin"}
        return Dt

    def visit_Variable(self, node):  # 访问变量节点
        var_name = node.name  # 获取变量名称
        vardata={"name": "Var\n"+var_name}
        data = [vardata]
        return data

    def visit_VarType(self, node):  # 添加访问类型的方法
        Typedata={"name": "Type\n"+node.name}
        data=[Typedata]
        return data

    def visit_Compound(self, node):  # 访问复合语句节点
        comchild=[]
        for child in node.children:  # 遍历复合语句节点的子节点
            comchild.append(self.visit(child))  # 访问子节点
        Compounddata={"children":comchild,"name": "Compound"}
        data=[Compounddata]
        return data

    def visit_Var(self, node): # 访问访问变量语句节点
        dt = {"name":"Var\n"+node.name}
        rdt = [dt]
        return rdt

    def visit_Assign(self, node):  # 访问赋值语句节点
        vardata={"name":"Var\n"+node.left.name}
        rightdata= self.visit(node.right)
        Assignchild = [vardata]+rightdata
        Assigndata={"children":Assignchild, "name": "Assign"}
        return Assigndata
    
    def visit_Const(self, node):  # 访问赋值语句节点
        vardata={"name":"Var\n"+node.left.name}
        rightdata= self.visit(node.right)
        Assignchild = [vardata]+rightdata
        Assigndata={"children":Assignchild, "name": "ConstAssign"}
        return Assigndata

    def visit_Change(self,node):
        leftdata=self.visit(node.left)
        rightdata=self.visit(node.right)
        data={"children":leftdata+rightdata,"name": "Change"}
        return data

    def visit_BinOp(self, node):  # 访问二元运算符类型节点的方法
        leftdata=self.visit(node.left)
        rightdata=self.visit(node.right)
        BinOpdata={"children":leftdata+rightdata,"name": "BinOp\n"+node.op.type}
        data = [BinOpdata]
        return data

     
    def visit_Num(self, node):  # 访问数字类型节点的方法
        Numdata = {"name": "Num\n"+str(node.value)}
        data = [Numdata]
        return data

    def visit_Float(self, node):  
        Numdata = {"name": "Float\n"+str(node.value)}
        data = [Numdata]
        return data
    
    def visit_STRING(self, node):  
        Numdata = {"name": "String\n"+str(node.value)}
        data = [Numdata]
        return data
    
    def visit_Bool(self, node):  
        Numdata = {"name": "Bool\n"+str(node.value)}
        data = [Numdata]
        return data

    def visit_IF(self, node):  
        data = {"children":[self.visit(node.condition)[0],self.visit(node.then_node)[0],self.visit(node.else_node)[0]],"name": "If(Else)"}
        return data

    def visit_While(self,node):
        compound= self.visit(node.then_node)
        condition = {"children":self.visit(node.condition),"name":"Condition"}
        data = {"children":[condition,compound],"name":"While"}
        return data
    
    def visit_For(self,node):
        compound= self.visit(node.then)
        lip=[]
        for i in node.p:
            lip.append(self.visit(i)[0])
        range = {"children":lip,"name":"Range"}
        data = {"children":[range,compound[0]],"name":"For"}
        return data

    def visit_Return(self,node):
        data = {"children":self.visit(node.value),"name": "Return"}
        return data

    def visit_FunCall(self,node):
        par=[]
        for i in node.params:
            par.append(self.visit(i)[0])
        things=[{"children":par,"name":"Params\n"}]
        data = {"children":things,"name": "FunCall\n"+str(node.name)}
        return data
    
    def visit_FuncNode(self,node):
        par=[]
        for i in node.params:
            par.append(self.visit(i))

        things=[{"children":par,"name":"Params"},self.visit(node.block)[0]]
        data = {"children":things,"name": "FunNode\n"+str(node.name)}
        return data
    
    def visit_Param(self,node):
        data = {"children":[self.visit(node.name)[0],self.visit(node.types)[0]],"name": "Param\n"}
        return data

    def visit_Toint(self,node):
        data = {"children":self.visit(node.string),"name": "Toint\n"}
        return [data]
    def visit_Tostr(self,node):
        data = {"children":self.visit(node.inter),"name": "Tostr\n"}
        return [data]
    def visit_Tochr(self,node):
        data = {"children":self.visit(node.inter),"name": "Tochr\n"}
        return [data]
    def visit_Toord(self,node):
        data = {"children":self.visit(node.char),"name": "Toord\n"}
        return [data]
    def visit_Len(self,node):
        data = {"children":[node.string],"name":"Len"}
        return data
        
    def visit_Break(self,node):
        return {"name":"Break"}

    def visit_Continue(self,node):
        return {"name":"Continue"}

    def visit_UnaryOp(self, node):#一元操作符
        op = node.op.type
        exprdata=self.visit(node.expr)
        UnaryOpdata={"children":exprdata,"name": "UnaryOp:"+op}
        data = [UnaryOpdata]
        return data

    def visit_NoOp(self, node):  # 访问空语句节点
        NoOpdata={"name": "Null"}
        data = [NoOpdata]
        return NoOpdata

    def visit_NoneType(self,node):
        return self.visit_NoOp(node)

    def drawAST(self):
        data = self.visit(self.tree)  # 返回语法树可视化的遍历结果
        print(data)
        Asttree = (
            Tree()
                .add("", data, initial_tree_depth=-1, orient="TB")
                .set_global_opts(title_opts=opts.TitleOpts(title="AST树结构"))
                )
        Asttree.render('AstTree.html')