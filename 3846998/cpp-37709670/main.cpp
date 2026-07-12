#include <iostream>
#include <vector>
#include <ctype.h>
#include <map>
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
        //cout<<"stack::get("<<a<<")="<<*(_top-1-a)<<"("<<_top-1+a-mem<<")"<<endl;
        return *(_top-1+a);
    }
    int size(){
        return _top-mem;
    }
    void print(){
        cout<<"stack{";
        for(int*i=mem;i<_top;i++) cout<<*i<<",";
        cout<<"}\n";
    }
    int mem[n];
    int *_top=mem;
};
stack<4096> st,call_st;
stack<24576> sm;
int heap[32768];
int*hm=heap;
int used=0;
vector<string> code;
void run(){
    for(vector<string>::iterator pc=code.begin();pc<code.end();pc++){
        //cout<<*pc<<endl;
        //if(*pc=="PUSHSM") cout<<*(pc+1)<<endl;
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
        if(*pc=="ALLOCHM"){
            *hm=0;
            hm++;
        }
        if(*pc=="VALUEOF") st.push(heap[st.top()]);
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
        //cout<<"SM:";
        //sm.print();
        //cout<<"ST:";
        //st.print();
    }
}
map<string,string> op_to_string{
    {"+","ADD"},
    {"-","SUB"},
    {"*","MUL"},
    {"/","DIV"},
    {"%","MOD"},
    {"==","EQ"},
    {"!=","NE"},
    {">","GT"},
    {"<","LT"},
    {">=","GE"},
    {"<=","LE"},
    {"<<","LSHIFT"},
    {">>","RSHIFT"},
    {"&&","AND"},
    {"||","OR"},
    {"&","BIT_AND"},
    {"|","BIT_OR"},
    {"^","XOR"},
};
struct Compiler{
    string code;
    int ifcode=0,whilecondcode=0,whileendcode=0;
    stack<4096> scope;
    vector<string> res,vartb,funtb;
    vector<vector<string> > funpara;
    Compiler(string s=""):code(s){
        res.reserve(65536);
        vartb.reserve(24576);
        funtb.reserve(4096);
        funpara.reserve(4096);
        cout<<"Compiler:Memory allocate successed.\n";
    }
    void pre(){
        while(code.size()&&(code[0]=='\n'||code[0]=='\t'||code[0]==' '||code[0]=='\0')) code.erase(code.begin());
    }
    void write(string s){
        res.push_back(s);
    }
    string get(int n){
        pre();
        return code.substr(0,n);
    }
    string nextid(){
        pre();
        string s,_c=code;
        while(code[0]=='_'||isalnum(code[0])) s+=code[0],code.erase(code.begin());
        code=_c;
        return s;
    }
    void passid(){
        pre();
        while(code[0]=='_'||isalnum(code[0])) code.erase(code.begin());
    }
    void pass(int n=1,int f=0){
        if(!f) pre();
        code.erase(code.begin(),code.begin()+n);
    }
    void eat(string s){
        pre();
        if(get(s.size())!=s) throw;
        pass(s.size());
    }
    bool match(string s){
        return get(s.size())==s;
    }
    vector<string> compile(){
        program();
        return res;
    }
    void program(){
        write("CALL"),write("main"),write("PUTS"),write("\nEXIT\n"),write("EXIT");
        while(code.size()){
            pre();
            top_decl();
            pre();
        }
        write("RET");
    }
    void top_decl(){
        if(nextid()=="int"){
            passid();
            write("ALLOC"),write("1");
            vartb.push_back(nextid());
            passid();
        }
        else if(nextid()=="fun"){
            int cnt=0;
            scope.push(0);
            passid();
            funtb.push_back(nextid());
            funpara.push_back(vector<string>());
            passid();
            eat("(");
            if(get(1)!=")"){
                funpara[funpara.size()-1].push_back(nextid());
                passid();
                cnt++;
                vartb.push_back(funpara[funpara.size()-1][funpara[funpara.size()-1].size()-1]);
                while(get(1)==","){
                    eat(",");
                    funpara[funpara.size()-1].push_back(nextid());
                    passid();
                    cnt++;
                    vartb.push_back(funpara[funpara.size()-1][funpara[funpara.size()-1].size()-1]);
                }
            }
            eat(")");
            write(funtb[funtb.size()-1]+":");
            eat("{");
            stmts();
            write("RECYCLE");
            write(to_string(scope.pop()));
            eat("}");
            while(cnt--) vartb.pop_back();
        }
    }
    void stmts(){
        pre();
        while(code.size()&&code[0]!='}'){
            pre();
            stmt();
            pre();
        }
    }
    void stmt(){
        pre();
        if(nextid()=="int"){
            scope.top()++;
            passid();
            write("ALLOC"),write("1");
            vartb.push_back(nextid());
            passid();
        }
        else if(nextid()=="write"){
            passid();
            expr();
            write("WRITE");
        }
        else if(nextid()=="puts"){
            passid();
            while(code[0]!='[') pass(1,1);
            pass(1);
            string s="";
            while(code[0]!=']') s+=code[0],pass(1,1);
            pass(1);
            write("PUTS");
            write(s);
        }
        else if(nextid()=="set"){
            passid();
            string id=nextid();
            passid();
            int n=0;
            for(int i=vartb.size()-1;i>=0;i--)
                if(vartb[i]==id) break;
                else n++;
            expr();
            write("ASSIGNSM");
            write(to_string(-n));
        }
        else if(nextid()=="if"){
            passid();
            eat("(");
            expr();
            eat(")");
            eat("{");
            write("JNZ");
            write("IFEND"+to_string(ifcode));
            int _ifcode=ifcode++;
            scope.push(0);
            stmts();
            write("RECYCLE");
            write(to_string(scope.pop()));
            write("IFEND"+to_string(_ifcode)+":");
            eat("}");
        }
        else if(nextid()=="while"){
            passid();
            eat("(");
            write("WHILELOOPCOND"+to_string(whilecondcode)+":");
            expr();
            eat(")");
            eat("{");
            write("JNZ");
            write("WHILELOOPEND"+to_string(whileendcode));
            int _whilecondcode=whilecondcode++,_whileendcode=whileendcode++;
            scope.push(0);
            stmts();
            write("RECYCLE");
            write(to_string(scope.pop()));
            write("JMP");
            write("WHILELOOPCOND"+to_string(_whilecondcode));
            write("WHILELOOPEND"+to_string(_whileendcode)+":");
            eat("}");
        }
        else if(nextid()=="read"){
            passid();
            string id=nextid();
            passid();
            int n=0;
            for(int i=vartb.size()-1;i>=0;i--)
                if(vartb[i]==id) break;
                else n++;
            write("READ");
            write("ASSIGNSM");
            write(to_string(-n));
        }
        else if(nextid()=="return"){
            passid();
            expr();
            write("RET");
        }
        else{
            expr();
            write("POP");
        }
    }
    #define F(f,w) if(match(#f)) eat(#f),w(),write(op_to_string[#f]);
    void expr(){
        expr0();
        while(match("||")||match("&&")){F(||,expr0)F(&&,expr0)}
    }
    void expr0(){
        expr1();
        while(match("==")||match("!=")||match(">=")||
            match("<=")||match(">")||match("<")){
            F(==,expr1)F(!=,expr1)F(>=,expr1)
            F(<=,expr1)F(>,expr1)F(<,expr1)}
    }
    void expr1(){
        expr2();
        while(match("|")||match("&")||match("^")){F(|,expr2)F(&,expr2)F(^,expr2)}
    }
    void expr2(){
        expr3();
        while(match("+")||match("-")){F(+,expr3)F(-,expr3)}
    }
    void expr3(){
        factor();
        while(match("*")||match("/")||match("%")){F(*,factor)F(/,factor)F(%,factor)}
    }
    void factor(){
        pre();
        if(isdigit(code[0])) write("PUSH"),write(nextid()),passid();
        else if(isalpha(code[0])||code[0]=='_'){
            string id=nextid();
            passid();
            if(get(1)=="("){
                eat("(");
                int alloc=0;
                if(get(1)!=")"){
                    vector<string> f;
                    int cnt=0;
                    for(int i=0;i<funtb.size();i++) if(funtb[i]==id) f=funpara[i];
                    vartb.push_back(f[cnt++]);
                    expr();
                    write("ALLOC"),write("1");
                    write("ASSIGNSM"),write("0");
                    alloc++;
                    while(get(1)==","){
                        eat(",");
                        vartb.push_back(f[cnt++]);
                        expr();
                        write("ALLOC"),write("1");
                        write("ASSIGNSM"),write("0");
                        alloc++;
                    }
                }
                eat(")");
                write("CALL"),write(id);
                write("RECYCLE"),write(to_string(alloc));
                while(alloc--) vartb.pop_back();
                return;
            }
            write("PUSHSM");
            int n=0;
            for(int i=vartb.size()-1;i>=0;i--)
                if(vartb[i]==id) break;
                else n++;
            write(to_string(-n));
        }
        else if(code[0]=='('){
            eat("(");
            expr();
            eat(")");
        }
        else throw;
    }
};
int main()
{
    /*code=vector<string>{
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
    };*/
    code=Compiler("\
    fun f(a){if(a==0){return 1}return a*f(a-1)}\
    fun main(){puts[这是一个C语言编译器，运行原理是先编译成字节码，再解释执行\n\
但是它尚未实现图灵完备，有些地方还和C语言不一样\n\
它以后会越来越像C语言\n\
这是一个求阶乘的程序，请输入一个数\n]\
    int a\
    read a\
    write f(a)}\
    ").compile();
    //for(string i:code) cout<<i<<endl;
    cout<<"\nSTART RUNNING\n";
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
        set i i+1
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