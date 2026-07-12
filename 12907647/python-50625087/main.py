import time
t = time.time()
class a:
    def __init__(self):
        self.awa = 1
    @classmethod
    def aa(cls):
        return cls
x = eval('a()'+'.aa()()'*100+'.aa()')
y = eval('x()'+'.aa()()'*100+'.aa()')
x = eval('y()'+'.aa()()'*100+'.aa()')
y = eval('x()'+'.aa()()'*100+'.aa()')
for i in range(100):
    x = eval('y()'+'.aa()()'*100+'.aa()')
    y = eval('x()'+'.aa()()'*100+'.aa()')
x = eval('y()'+'.aa()()'*100+'.aa()')
print(time.time()-t)
print(x().awa)
print(a().aa()().aa()().awa)
print(x().aa()().awa is a().aa()().aa()().awa)

# 递归报错
# x = eval('y()'+'.aa()()'*1000+'.aa()')
# y = eval('x()'+'.aa()()'*1000+'.aa()')