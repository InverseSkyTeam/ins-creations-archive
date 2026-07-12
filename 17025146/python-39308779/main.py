print("""
一、字面量和类型
str:"string" 'string'
int:1230
real:2.56 3.0
bool:true false
nulltype:null
function:
func(arg1:type,arg2:type,...)[ -> returntype]{stmt}
|arg1:type,arg2:type,...|[ -> returntype]{stmt}
|arg1:type,arg2:type,...|[ -> returntype] <expr>
array:[1,2,3]
map(暂不支持):{key1:value1,key2:value2,...}
二、语句
变量声明(存在变量遮掩行为) let varname[:vartype] = <expr>
变量修改 varname = <expr>
分支
if <expr>{stmt}
elif <expr>{stmt}
else{stmt}

switch varname{
    case <expr>:
        stmt
    case <expr>:
        stmt
    ...
    default:
        stmt
}
循环
while <expr>{stmt}
for var in iterobj{stmt}
loop{stmt}
break
continue
函数
fun funcname(arg1:type,arg2:type,...)[->returntype]{stmt}
return value
调试
debugger
作用域
{
    stmt
}
三、运算
1、二元运算
+、-、*、/、^、%、and、or、>=、<=、==、!=、<、>
2、一元运算
+、-、not
3、三目运算(未实现)
value1?<expr>:value2
""")