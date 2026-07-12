#include <iostream>
#include <vector>
using namespace std;
template<int n=4096>
struct stack{
    stack(){}
    void push(int a){
        *_top=a;
        _top++;
    }
    int&top(){
        if(empty()) throw "Try to get the top of an empty stack!";
        return *(_top-1);
    }
    int&pop(){
        if(empty()) throw "Try to make an empty stack pop!";
        _top--;
        return *_top;
    }
    bool empty(){
        return _top==mem;
    }
    int&get(int a){
        return *(_top-1-a);
    }
    int mem[n];
    int *_top=mem;
};
stack<4096> st,call_st;
stack<24576> sm;
int used=0;
vector<string> code;
void run(){
    for(vector<string>::iterator pc=code.begin();pc<code.end();pc++){
        if(*pc=="PUTS") cout<<*(++pc);
        if(*pc=="COPY") st.push(st.top());
        if(*pc=="PUSH") st.push(stoi(*(++pc)));
        if(*pc=="POP") st.pop();
        if(*pc=="WRITE") cout<<st.pop();
        if(*pc=="READ") st.push(0),cin>>st.top();
        if(*pc=="EXIT") return;
        if(*pc=="CALL"){
            call_st.push(pc+1-code.begin());
            string name=*(++pc);
            for(pc=code.begin();pc<code.end();pc++) if(*pc==name+":") break;
        }
        if(*pc=="RET") pc=code.begin()+call_st.pop();
        if(*pc=="JMP"){
            string name=*(++pc);
            for(pc=code.begin();pc<code.end();pc++) if(*pc==name+":") break;
        }
        if(*pc=="JZ"){
            string name=*(++pc);
            if(st.pop()) for(pc=code.begin();pc<code.end();pc++) if(*pc==name+":") break;
        }
        if(*pc=="JNZ"){
            string name=*(++pc);
            if(!st.pop()) for(pc=code.begin();pc<code.end();pc++) if(*pc==name+":") break;
        }
        if(*pc=="ALLOC"){
            used+=stoi(*(++pc));
            for(int i=0;i<stoi(*pc);i++) sm.push(0);
        }
        if(*pc=="PUSHSM") st.push(sm.get(stoi(*(++pc))));
        if(*pc=="ASSIGNSM") sm.get(stoi(*(++pc)))=st.pop();
        if(*pc=="RECYCLE"){
            used-=stoi(*(++pc));
            for(int i=0;i<stoi(*pc);i++) sm.pop();
        }
        if(*pc=="DEBUG"){
            cout<<"ST:";
            for(int *i=st.mem;i<st._top;i++) cout<<*i<<" ";
            cout<<"\n";
        }
        if(*pc=="DEBUGSM"){
            cout<<"SM:";
            for(int *i=sm.mem;i<sm._top;i++) cout<<*i<<" ";
            cout<<"\n";
        }
        if(*pc=="ERROR") throw *(++pc);
        #define f(n,op) if(*pc==#n){\
            int r=st.pop(),l=st.pop();\
            st.push(l op r);\
        }
        f(ADD,+)f(SUB,-)f(MUL,*)f(DIV,/)f(MOD,%)
        f(EQ,==)f(NE,!=)f(GT,>)f(LT,<)f(GE,>=)f(LE,<=)
        f(LSHIFT,<<)f(RSHIFT,>>)
        f(AND,&&)f(OR,||)
        f(BIT_AND,&)f(BIT_OR,|)f(XOR,^)
        #undef f
        #define f(n,op) if(*pc==#n) st.push(op st.pop());
        f(NOT,!)f(INV,~)f(POS,+)f(NEG,-)
        #undef f
    }
}
int main()
{
    code=vector<string>{
"CALL","main",
"PUTS","EXIT",
"EXIT",
"f:",
    "ALLOC","1",
    "WHILELOOPCOND0:",
        "PUSHSM","0",
        "PUSHSM","1",
        "LT",
    "JNZ","WHILELOOPEND0",
        "PUSHSM","0",
        "WRITE",
        "PUTS","\n",
        "PUSHSM","0",
        "PUSH","1",
        "ADD",
        "ASSIGNSM","0",
    "JMP","WHILELOOPCOND0",
    "WHILELOOPEND0:",
    "RECYCLE","1",
    "RET",
"main:",
    "ALLOC","1",
    "PUSH","10",
    "ASSIGNSM","0",
    "PUSHSM","0",
    "CALL","f",
    "RECYCLE","1"
    "PUSH","0",
    "RET",
    };
    run();
    return 0;
}
/*
fun main(){
    int a,b
    read a
    read b
    write a+b
    return 0
}

CALL main
EXIT
main:
    ALLOC 2
    READ
    ASSIGNSM -1
    READ
    ASSIGNSM 0
    PUSHSM -1
    PUSHSM 0
    ADD
    WRITE
    RECYCLE 2
    PUSH 0
    RET

fun f(a){
    int i
    while(i<a){
        write i
        i=i+1
    }
    return
}
fun main(){
    f(10)
}

CALL main
PUTS EXIT
EXIT
f:
    ALLOC 1
    WHILELOOPCOND0:
        PUSHSM 0
        PUSHSM 1
        LT
    JNZ WHILELOOPEND0
        PUSHSM 0
        WRITE
        PUSHSM 0
        PUSH 1
        ADD
        ASSIGNSM 0
        PUTS \n
    JMP WHILELOOPCOND0
    WHILELOOPEND0:
    RECYCLE 1
    RET
main:
    ALLOC 1
    PUSH 10
    ASSIGNSM 0
    CALL f
    RECYCLE 1
    PUSH 0
    RET
*/