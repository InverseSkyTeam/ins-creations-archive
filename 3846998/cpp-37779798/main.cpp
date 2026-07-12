#include <stdio.h>
#include <memory.h>
#include <stdlib.h>
enum{
    EXIT,
    PUSH,POP,LS,COPY,
    ADD,SUB,MUL,DIV,MOD,
    EQ,NE,GT,LT,GE,LE,
    LSHIFT,RSHIFT,
    AND,OR,
    BITAND,BITOR,XOR,
    POS,NEG,NOT,INV,
    LABEL,
    JMP,JZ,JNZ,
    CALL,RET,
    WI,WC,WS,RI,RC,RS,RL,
    DEFINE,DELETE,ASSIGN,LOAD,
    MAIN,
};
int mem[65536];
int*text=mem,*pc=text,*sp=mem+16384,*csp=mem+24576,*ssp=mem+32768;
void run(){
    while(1){
        if(*pc==EXIT) break;
        #define w(n,do) else if(*pc==n)do
        w(LABEL,{pc++;})
        w(PUSH,{*sp++=*++pc;})
        w(POP,{sp--;})
        w(LS,{
            *sp++=0;
            for(int i=0;*pc;i++) *sp++=*++pc;
            sp--;
        })
        w(WI,{printf("%d",*--sp);})
        w(WC,{printf("%c",*--sp);})
        w(WS,{
            for(int i=0;*(sp-1);i++) printf("%c",*--sp);
        })
        w(COPY,{
            int top=*(sp-1);
            *sp++=top;
        })
        w(RI,{scanf("%d",sp++);})
        w(RC,{*sp++=getchar();})
        w(RS,{
            char str[100];
            scanf("%s",str);
            int i=0;
            *sp++=0;
            for(;str[i];i++);
            for(i--;i>=0;i--) *sp++=str[i];
        })
        w(RL,{
            char str[100];
            gets(str);
            int i=0;
            *sp++=0;
            for(;str[i];i++);
            for(i--;i>=0;i--) *sp++=str[i];
        })
        #define f(n,op) else if(*pc==n){\
            int r=*--sp,l=*--sp;\
            *sp++=l op r;\
        }
        f(ADD,+)f(SUB,-)f(MUL,*)f(DIV,/)f(MOD,%)
        f(EQ,==)f(NE,!=)f(GT,>)f(LT,<)f(GE,>=)f(LE,<=)
        f(LSHIFT,<<)f(RSHIFT,>>)
        f(AND,&&)f(OR,||)
        f(BITAND,&)f(BITOR,|)f(XOR,^)
        #undef f
        #define f(n,op) else if(*pc==n) *(sp-1)=op*(sp-1);
        f(NOT,!)f(INV,~)f(POS,+)f(NEG,-)
        #undef f
        w(JMP,{
            int lbl=*++pc;
            for(pc=mem;pc<mem+16384;pc++) if(*pc==LABEL&&*(pc+1)==lbl) break;
            ++pc;
        })
        w(JZ,{
            if(*--sp){
                int lbl=*++pc;
                for(pc=mem;pc<mem+16384;pc++) if(*pc==LABEL&&*(pc+1)==lbl) break;
                ++pc;
            }
        })
        w(JNZ,{
            if(!*--sp){
                int lbl=*++pc;
                for(pc=mem;pc<mem+16384;pc++) if(*pc==LABEL&&*(pc+1)==lbl) break;
                ++pc;
            }
        })
        w(CALL,{
            int lbl=*++pc;
            *csp++=pc-mem;
            for(pc=mem;pc<mem+16384;pc++) if(*pc==LABEL&&*(pc+1)==lbl) break;
            ++pc;
        })
        w(RET,{pc=mem+*--csp;})
        w(DEFINE,{*ssp++=0;})
        w(DELETE,{ssp--;})
        w(ASSIGN,{
            int ptr=*--sp;
            int v=*--sp;
            *(mem+ptr)=v;
        })
        w(LOAD,{
            *(sp-1)=*(mem+*(sp-1));
        })
        #undef w
        pc++;
    }
}
int _text[16384]={
    /*
    int add(int a,int b){
        return a+b;
    }
    int main(){
        WI add(1,2);
        return 0;
    }
    */
    CALL,MAIN,
    EXIT,
    LABEL,100,
        DEFINE,//a->mem[32768]
        DEFINE,//b->mem[32769]
        PUSH,32769,
        ASSIGN,
        PUSH,32768,
        ASSIGN,
        PUSH,32768,
        LOAD,
        PUSH,32769,
        LOAD,
        ADD,
        DELETE,
        DELETE,//回收参数占用的空间
        RET,
    LABEL,MAIN,
        PUSH,1,
        PUSH,2,//参数顺序入栈
        CALL,100,
        WI,
        PUSH,0,
        RET,
};
int main()
{
    memcpy(text,_text,16384*4);
    run();
    printf("\nEXIT\n");
    printf("回车开始我的优秀作品推荐，您也可以直接结束程序");
    getchar();
    printf(
        "上首页的竟然是这个破烂\n"
        "所以在此推荐一下我的优秀作品\n"
        "编程语言方面：\n"
        "Python："
        "integer3-语言解释器：https://code.xueersi.com/home/project/detail?lang=code&pid=34276743&version=python&form=python&langType=python\n"
        "integer3.2.3.1：https://code.xueersi.com/home/project/detail?lang=code&pid=40501319&version=python&form=python&langType=python\n"
        "Rain0.7：https://code.xueersi.com/home/project/detail?lang=code&pid=40601579&version=python&form=python&langType=python\n"
        "Tiny Lisp1.7：https://code.xueersi.com/home/project/detail?lang=code&pid=40395863&version=python&form=python&langType=python\n"
        "My Python1.1：https://code.xueersi.com/home/project/detail?lang=code&pid=39969134&version=python&form=python&langType=python\n"
        "Butterfly0.0.7.1：https://code.xueersi.com/home/project/detail?lang=code&pid=39380821&version=python&form=python&langType=python\n"
        "C++："
        "Array&Stack语言，基于c++：https://code.xueersi.com/home/project/detail?lang=code&pid=32911540&version=cpp&form=cpp&langType=cpp\n"
        "N则运算-拓展（但真的只是计算吗？）：https://code.xueersi.com/home/project/detail?lang=code&pid=39804410&version=cpp&form=cpp&langType=cpp\n"
        "伪·C语言0.2编辑器：https://code.xueersi.com/home/project/detail?lang=code&pid=37720803&version=cpp&form=cpp&langType=cpp\n"
        "自创语言解释器：https://code.xueersi.com/home/project/detail?lang=code&pid=36333644&version=cpp&form=cpp&langType=cpp\n"
        "终端可视化/游戏方面：\n"
        "贪吃蛇0.1：https://code.xueersi.com/home/project/detail?lang=code&pid=40445707&version=cpp&form=cpp&langType=cpp\n"
        "C++跑酷0.0：https://code.xueersi.com/home/project/detail?lang=code&pid=40462850&version=cpp&form=cpp&langType=cpp\n"
        "IIDE本地版：https://code.xueersi.com/home/project/detail?lang=code&pid=40673636&version=python&form=python&langType=python\n"
    );
    return 0;
}