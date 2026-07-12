'''
Butterfly0.0.5文档
1、输出语句
    print[sep=...,end=...,flush=...] value1,value2,...;
2、宏（算不上真正的宏，只是瞎起的名）
    getchar!():string
    readln!():string
    len!(value:string|any[]):int
    chr!(value:int):string
    ord!(value:string):int
    array_add!(a:any[],b:any[]):any[]
3、语句
    变量定义
        var var1:type1[=value1],...;
    函数定义
        func funcname(para1:type1,...):returntype{
            ...
        }
        注意不会自动return
        最后必须有返回语句
    方法定义
        method typename methodname(para1:type1,...):returntype{
            ...
        }
    结构体定义
        struct T{
            attr1:type1;
            ...
        }
    分支
        if(bool){
            ...
        }
        else if(bool){
            ...
        }
        else{
            ...
        }
        大括号可省略
    循环
        while(bool){
            ...
        }
        大括号可省略
4、匿名函数
    lambda(para1:type1,...):returntype{
        ...
    }
5、类型
    typename|typename[]|function<returntype,paratype1,paratype2,...>
6、列表字面值
    array:elementtype{element1,...}
'''