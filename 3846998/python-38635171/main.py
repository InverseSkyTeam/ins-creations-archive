input("请将屏幕拉大，回车开始：")
print('''
integer3.1.2说明文档
1、类型
    内置类型：
        int
        float
        string
        bool
        null_t（直接用了python的NoneType）
        list
        type
        module
        object
        func
2、变量
    用var关键字定义变量
    var name[=value]...;
    赋值
    a=value;
    a[0]=value;
    a.a=value;
    a::a=value;
3、函数、类和模块
    函数
        lambda(<parameters>){<body>}
        定义匿名函数
    类
        anonymous_class[:<parents>]cons(<parameters>){<body>}{<members>}
        定义“匿名类型”
        name(<arguments>)
        调用name类的构造函数初始化name类的实例
        name::name
        获得属性的值
    模块
        anonymous_module{<members>}
        定义“匿名模块”
        import name
        导入“匿名模块”
        name::name
        获得属性的值
        name.name
        获得对象属性的值
    语法糖
        func name(<parameters>){<body>}
        class name[:<parents>]cons(<parameters>){<body>}{<members>}
        module name{members}
        object{name1:value1[,]name2:value2...}不定义类直接创建对象
        type(<object>)获取object的类型，一定要保证object是自定义类型的实例，哪怕是直接创建的对象也行
4、基本结构
    <body>部分如果只有一条语句可以不加大括号
    分支
        if(<condition>){<body>}[else{<body>}]
    while循环
        while(<condition>){<body>}
    for循环
        for(<variable declaration>;<condition>;<assign statement>){<body>}
    foreach循环
        foreach(i,j...:value){<body>}
5、内置函数
    print/println3
    inputln
    ord
    chr
    len
    substr
    type
差不多就这么多
最后附上我用它写的Brainfuck解释器源码
{
    var Getchar=
    anonymous_class
    cons(){
        this.line="";
    }
    {
        var line="";
        var get=lambda(){
            if(len(this.line)==0) this.line=inputln()+"\\n";
            var ch=this.line[0];
            this.line=substr(this.line,1);
            return ch;
        };
    };
    var get=Getchar();
    var code=inputln("这是一个用integer3.1.0写的Brainfuck解释器\\nBrainfuck>>>");
    var i=0;
    var mem=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
    var pos=8;
    while(i<len(code)){
        var c=code[i];
        if(c=="+") mem[pos]=mem[pos]+1;
        if(c=="-") mem[pos]=mem[pos]-1;
        if(c==">") pos=pos+1;
        if(c=="<") pos=pos-1;
        if(c==".") print(chr(mem[pos]));
        if(c==",") mem[pos]=ord(get.get());
        if(c=="["){
            if(mem[pos]==0){
                var l=1,r=0;
                i=i+1;
                while(i<len(code)){
                    if(code[i]=="[") l=l+1;
                    if(code[i]=="]"){
                        r=r+1;
                        if(l!=0){
                            r=r-1;
                            l=l-1;
                        }
                    }
                    if(l==0&&r==0) break;
                    i=i+1;
                }
            }
        }
        if(c=="]"){
            var l=0,r=1;
            i=i-1;
            while(i>=0){
                if(code[i]=="]") r=r+1;
                if(code[i]=="["){
                    l=l+1;
                    if(r!=0){
                        r=r-1;
                        l=l-1;
                    }
                }
                if(l==0&&r==0) break;
                i=i-1;
            }
            i=i-1;
        }
        i=i+1;
    }
}
''')