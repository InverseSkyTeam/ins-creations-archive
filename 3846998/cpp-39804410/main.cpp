#include <bits/stdc++.h>
using namespace std;
class AST;
class Scope;
class Function{
public:
    vector<string> para;
    AST*body=0;
    Scope*closure=0;
    Function(){}
    Function(vector<string> a,AST*b,Scope*c):para(a),body(b),closure(c){}
};
string ctos(char a){
    stringstream ss;
    ss<<a;
    return ss.str();
}
void _throw(char*s){
    cout<<s;
    exit(-1);
}
enum{
    INT,FLOAT,STRING,NONE,LIST,FUNCTION,BFUNCTION,POINTER,
};
enum{
    NORET=100,BREAK,CONTINUE,RETURN,
};
enum{
    ADD,SUB,MUL,DIV,MOD,
    EQ,NE,GT,LT,GE,LE,
    SHL,SHR,
    AND,OR,
    BAND,BOR,XOR,
    NOT,INV,
    LPAREN,RPAREN,
    LSB,RSB,
    BEGIN,END,
    SEMICOLON,
    ASSIGN,COMMA,
    INUM,FNUM,STR,NON,
    ID,
    EXIT,
};
int int_binary(int op,int a,int b){
    switch(op){
        case ADD:return a+b;
        case SUB:return a-b;
        case MUL:return a*b;
        case DIV:return a/b;
        case MOD:return a%b;
        case EQ:return a==b;
        case NE:return a!=b;
        case GT:return a>b;
        case LT:return a<b;
        case GE:return a>=b;
        case LE:return a<=b;
        case SHL:return a<<b;
        case SHR:return a>>b;
        case AND:return a&&b;
        case OR:return a||b;
        case BAND:return a&b;
        case BOR:return a|b;
        case XOR:return a^b;
    }
    _throw("错误的双目运算");
}
float float_binary(int op,float a,float b){
    switch(op){
        case ADD:return a+b;
        case SUB:return a-b;
        case MUL:return a*b;
        case DIV:return a/b;
        case EQ:return a==b;
        case NE:return a!=b;
        case GT:return a>b;
        case LT:return a<b;
        case GE:return a>=b;
        case LE:return a<=b;
        case AND:return a&&b;
        case OR:return a||b;
    }
    _throw("错误的双目运算");
}
int string_cmp(int op,string a,string b){
    switch(op){
        case EQ:return a==b;
        case NE:return a!=b;
        case GT:return a>b;
        case LT:return a<b;
        case GE:return a>=b;
        case LE:return a<=b;
    }
    _throw("错误的双目运算");
}
template<class T>
vector<T> vector_add(vector<T>a,vector<T>b){
    a.insert(a.end(),b.begin(),b.end());
    return a;
}
struct BreakV{};
struct ContinueV{};
class Val;
struct ReturnV{
    Val *v=0;
    ReturnV(){}
    ReturnV(Val *a):v(a){}
};
class Val{
public:
    int tp;
    int iv;
    float fv;
    string sv;
    vector<Val> lv;
    Function fnv;
    function<Val(vector<Val>)> bfv;
    Val*ptrv=0;
    struct None{} nv;
    struct NoRet{} nrv;
    BreakV brv;
    ContinueV cov;
    ReturnV rtv;
    Val(){}
    Val(int a):iv(a),tp(INT){}
    Val(float a):fv(a),tp(FLOAT){}
    Val(string a):sv(a),tp(STRING){}
    Val(vector<Val> a):lv(a),tp(LIST){}
    Val(Function a):fnv(a),tp(FUNCTION){}
    Val(function<Val(vector<Val>)>a):bfv(a),tp(BFUNCTION){}
    Val(Val*a):ptrv(a),tp(POINTER){}
    Val(None a):nv(a),tp(NONE){}
    Val(NoRet a):nrv(a),tp(NORET){}
    Val(BreakV a):brv(a),tp(BREAK){}
    Val(ContinueV a):cov(a),tp(CONTINUE){}
    Val(ReturnV a):rtv(a),tp(RETURN){}
    Val binary(int op,Val b){
        Val a=*this;
        if(a.tp==POINTER&&b.tp==INT&&op==ADD) return a.ptrv+b.iv;
        if(a.tp==INT&&b.tp==POINTER&&op==ADD) return a.iv+b.ptrv;
        if(a.tp==POINTER&&b.tp==INT&&op==SUB) return a.ptrv-b.iv;
        if(a.tp==POINTER&&b.tp==INT&&op==ADD) return a.ptrv+b.iv;
        if(a.tp==POINTER&&b.tp==POINTER&&op==SUB) return (int)(a.ptrv-b.ptrv);
        if(a.is_num()&&b.is_num()){
            if(a.tp==INT&&b.tp==INT) return int_binary(op,a.iv,b.iv);
            if(a.tp==FLOAT&&b.tp==FLOAT) return float_binary(op,a.fv,b.fv);
            if(a.is_float()||b.is_float()) return float_binary(op,a.convert(FLOAT).fv,b.convert(FLOAT).fv);
        }
        if(a.tp==STRING&&b.tp==STRING){
            if(op==ADD) return a.sv+b.sv;
            return string_cmp(op,a.sv,b.sv);
        }
        if(a.tp==LIST&&b.tp==LIST){
            if(op==ADD) return Val(vector_add(a.lv,b.lv));
            _throw("错误的双目运算");
        }
        if(op==EQ&&a.tp!=b.tp) return 0;
        if(op==EQ&&a.tp==b.tp) return 1;
        if(op==NE&&a.tp==b.tp) return 0;
        if(op==NE&&a.tp!=b.tp) return 1;
        _throw("错误的双目运算");
    }
    Val convert(int to){
        switch(tp){
            case INT:
            switch(to){
                case INT:return *this;
                case FLOAT:return Val(float(iv));
                default:_throw("错误的类型转换");
            }
            case FLOAT:
            switch(to){
                case INT:return Val(int(fv));
                case FLOAT:return *this;
                default:_throw("错误的类型转换");
            }
            case STRING:
            switch(to){
                case STRING:return *this;
                default:_throw("错误的类型转换");
            }
            case NONE:
            switch(to){
                case NONE:return *this;
                default:_throw("错误的类型转换");
            }
        }
        _throw("错误的类型转换");
    }
    bool is_int(){
        return tp==INT;
    }
    bool is_float(){
        return tp==FLOAT;
    }
    bool is_num(){
        return is_int()||is_float();
    }
    string tostr(){
        switch(tp){
            case INT:return to_string(iv);
            case FLOAT:return to_string(fv);
            case STRING:return sv;
            case NONE:return "none";
            case LIST:return connect(lv,",");
        }
        _throw("无法将此类型的值转为字符串");
    }
    string connect(vector<Val> l,string sep){
        if(l.size()==0) return "[]";
        string res="[";
        for(int i=0;i<l.size()-1;i++) res+=l[i].tostr()+sep;
        res+=(l.end()-1)->tostr();
        res+="]";
        return res;
    }
    Val unary(int op){
        if(tp==INT)
        switch(op){
            case ADD:return +iv;
            case SUB:return -iv;
            case NOT:return !iv;
            case INV:return ~iv;
        }
        if(tp==FLOAT)
        switch(op){
            case ADD:return +fv;
            case SUB:return -fv;
            case NOT:return !fv;
        }
        _throw("错误的单目运算");
    }
    Val getitem(Val n){
        if(n.tp!=INT) _throw("错误的索引");
        if(tp==STRING){
            if(n.iv>=sv.size()) _throw("下标越界");
            return Val(ctos(sv[n.iv]));
        }
        if(tp==LIST){
            if(n.iv>=lv.size()) _throw("下标越界");
            return lv[n.iv];
        }
        _throw("不能对该类型用下标取值");
    }
    Val&getitem_ref(Val n){
        if(n.tp!=INT) _throw("错误的索引");
        if(tp==LIST){
            if(n.iv>=lv.size()) _throw("下标越界");
            return lv[n.iv];
        }
        _throw("不能对该类型用下标取得元素的引用");
    }
    Val call(vector<Val>args);
};
class AST{
public:
    virtual Val eval()=0;
    virtual Val*ref()=0;
};
typedef Val::None None;
typedef Val::NoRet NoRet;
class Scope{
public:
    vector<map<string,Val> > st;
    Scope(){}
    Val&find(string name){
        for(int i=st.size()-1;i>=0;i--)
            if(st[i].find(name)!=st[i].end()) return st[i][name];
        _throw("未定义的变量");
    }
    void inscope(){
        st.push_back(map<string,Val>());
    }
    void outscope(){
        st.pop_back();
    }
    void define(string name,Val v=None()){
        (*(st.end()-1))[name]=v;
    }
} scope;
map<string,Val> zip(vector<string> a,vector<Val> b){
    map<string,Val> res;
    for(int i=0;i<a.size();i++) res[a[i]]=b[i];
    return res;
}
Val Val::call(vector<Val> args){
    if(tp!=FUNCTION&&tp!=BFUNCTION) _throw("不能调用此类型的值");
    if(tp==FUNCTION){
        if(args.size()!=fnv.para.size()) _throw("参数数量错误");
        Scope _scope=scope;
        scope=*fnv.closure;
        scope.inscope();
        *(scope.st.end()-1)=zip(fnv.para,args);
        Val ret=fnv.body->eval();
        scope.outscope();
        scope=_scope;
        if(ret.tp==NORET) return None();
        return *ret.rtv.v;
    }
    else{
        return bfv(args);
    }
}
class Const:public AST{
public:
    Val v;
    Const(Val a):v(a){}
    Val eval(){
        return v;
    }
    Val*ref(){
        _throw("错误的左值");
    }
};
class BinOp:public AST{
public:
    int op;
    AST *l,*r;
    BinOp(int _op,AST*_l,AST*_r):op(_op),l(_l),r(_r){}
    Val eval(){
        return l->eval().binary(op,r->eval());
    }
    Val*ref(){
        _throw("错误的左值");
    }
};
class UnaryOp:public AST{
public:
    int op;
    AST *v;
    UnaryOp(int _op,AST*_v):op(_op),v(_v){}
    Val eval(){
        return v->eval().unary(op);
    }
    Val*ref(){
        _throw("错误的左值");
    }
};
class Var:public AST{
public:
    string name;
    Var(string a):name(a){}
    Val eval(){
        return scope.find(name);
    }
    Val*ref(){
        return &scope.find(name);
    }
};
class Print:public AST{
public:
    AST*thing;
    Print(AST*a):thing(a){}
    Val eval(){
        cout<<thing->eval().tostr();
        return NoRet();
    }
    Val*ref(){
        _throw("错误的左值");
    }
};
class VarDecl:public AST{
public:
    vector<string> names;
    vector<AST*> values;
    VarDecl(vector<string> a,vector<AST*> b):names(a),values(b){}
    Val eval(){
        for(int i=0;i<names.size();i++) scope.define(names[i],values[i]->eval());
        return NoRet();
    }
    Val*ref(){
        _throw("错误的左值");
    }
};
class If:public AST{
public:
    vector<AST*> conds,cases;
    AST* defa;//default，不是什么define a
    If(vector<AST*> a,vector<AST*> b,AST*c):conds(a),cases(b),defa(c){}
    Val eval(){
        for(int i=0;i<conds.size();i++)
            if(conds[i]->eval().convert(INT).iv) return cases[i]->eval();
        return defa->eval();
    }
    Val*ref(){
        _throw("错误的左值");
    }
};
class While:public AST{
public:
    AST*cond,*body;
    While(AST*a,AST*b):cond(a),body(b){}
    Val eval(){
        while(cond->eval().convert(INT).iv){
            Val v=body->eval();
            if(v.tp==BREAK) break;
            if(v.tp==RETURN) return v.tp;
        }
        return NoRet();
    }
    Val*ref(){
        _throw("错误的左值");
    }
};
class NoOp:public AST{
public:
    NoOp(){}
    Val eval(){
        return NoRet();
    }
    Val*ref(){
        _throw("错误的左值");
    }
};
class Program:public AST{
public:
    vector<AST*> stmts;
    Program(vector<AST*> a):stmts(a){}
    Val eval(){
        scope.inscope();
        for(AST*i:stmts) i->eval();
        scope.outscope();
        return NoRet();
    }
    Val*ref(){
        _throw("错误的左值");
    }
};
class Block:public AST{
public:
    vector<AST*> stmts;
    Block(vector<AST*> a):stmts(a){}
    Val eval(){
        scope.inscope();
        for(AST*i:stmts){
            Val v=i->eval();
            if(v.tp>100){
                scope.outscope();
                return v;
            }
        }
        scope.outscope();
        return NoRet();
    }
    Val*ref(){
        _throw("错误的左值");
    }
};
class Assign:public AST{
public:
    AST*l,*r;
    Assign(AST*a,AST*b):l(a),r(b){}
    Val eval(){
        Val target=r->eval();
        *l->ref()=target;
        return target;
    }
    Val*ref(){
        _throw("错误的左值");
    }
};
class Element:public AST{
public:
    AST*l,*r;
    Element(AST*a,AST*b):l(a),r(b){}
    Val eval(){
        return l->eval().getitem(r->eval());
    }
    Val*ref(){
        return &l->ref()->getitem_ref(r->eval());
    }
};
class List:public AST{
public:
    vector<AST*> l;
    List(vector<AST*>a):l(a){}
    Val eval(){
        vector<Val> res;
        for(AST*i:l) res.push_back(i->eval());
        return Val(res);
    }
    Val*ref(){
        _throw("错误的左值");
    }
};
class Break:public AST{
public:
    Break(){}
    Val eval(){
        return BreakV();
    }
    Val*ref(){
        _throw("错误的左值");
    }
};
class Continue:public AST{
public:
    Continue(){}
    Val eval(){
        return ContinueV();
    }
    Val*ref(){
        _throw("错误的左值");
    }
};
class Return:public AST{
public:
    AST*v;
    Return(AST*a):v(a){}
    Val eval(){
        Val *_v=new Val(v->eval());
        return ReturnV(_v);
    }
    Val*ref(){
        _throw("错误的左值");
    }
};
class Lambda:public AST{
public:
    vector<string> para;
    AST*body;
    Lambda(vector<string> a,AST*b):para(a),body(b){}
    Val eval(){
        return Function(para,body,&scope);
    }
    Val*ref(){
        _throw("错误的左值");
    }
};
class CallFunc:public AST{
public:
    AST*func;
    vector<AST*> args;
    CallFunc(AST*a,vector<AST*>b):func(a),args(b){}
    Val eval(){
        vector<Val> _args;
        for(AST*i:args) _args.push_back(i->eval());
        return func->eval().call(_args);
    }
    Val*ref(){
        _throw("错误的左值");
    }
};
class Token{
public:
    int tp;
    string v;
    Token(int a=0,string b=""):tp(a),v(b){}
};
class Lexer{
public:
    string text;
    int p;
    Lexer(){}
    Lexer(string a):text(a),p(0){}
    Token get(){
        while(text[p]==' '||text[p]=='\n'||text[p]=='\t') p++;
        if(p==text.size()) return Token(EXIT);
        #define match(op) text.substr(p,string(op).size())==op
        if(match("+")) return p++,Token(ADD);
        if(match("-")) return p++,Token(SUB);
        if(match("*")) return p++,Token(MUL);
        if(match("/")) return p++,Token(DIV);
        if(match("%")) return p++,Token(MOD);
        if(match("==")) return p+=2,Token(EQ);
        if(match("!=")) return p+=2,Token(NE);
        if(match(">=")) return p+=2,Token(GE);
        if(match("<=")) return p+=2,Token(LE);
        if(match("<<")) return p+=2,Token(SHL);
        if(match(">>")) return p+=2,Token(SHR);
        if(match(">")) return p++,Token(GT);
        if(match("<")) return p++,Token(LT);
        if(match("&&")) return p+=2,Token(AND);
        if(match("||")) return p+=2,Token(OR);
        if(match("|")) return p++,Token(OR);
        if(match("&")) return p++,Token(AND);
        if(match("^")) return p++,Token(XOR);
        if(match("!")) return p++,Token(NOT);
        if(match("~")) return p++,Token(INV);
        if(match("(")) return p++,Token(LPAREN);
        if(match(")")) return p++,Token(RPAREN);
        if(match(";")) return p++,Token(SEMICOLON);
        if(match("=")) return p++,Token(ASSIGN);
        if(match(",")) return p++,Token(COMMA);
        if(match("{")) return p++,Token(BEGIN);
        if(match("}")) return p++,Token(END);
        if(match("[")) return p++,Token(LSB);
        if(match("]")) return p++,Token(RSB);
        #undef match
        if(isdigit(text[p])){
            string s;
            s+=text[p++];
            while(isdigit(text[p])||text[p]=='.') s+=text[p++];
            if(s.find(".")!=string::npos) return Token(FNUM,s);
            return Token(INUM,s);
        }
        if(isalpha(text[p])||text[p]=='_'){
            string s;
            s+=text[p++];
            while(isalnum(text[p])||text[p]=='_') s+=text[p++];
            if(s=="none") return Token(NON);
            return Token(ID,s);
        }
        if(text[p]=='"'){
            string s;
            //s+=text[++p];
            p++;
            while(text[p]!='"'){
                if(text[p]=='\\'){
                    p++;
                    switch(text[p]){
                        case 'n':p++;s+='\n';break;
                        case 't':p++;s+='\t';break;
                        case 'f':p++;s+='\f';break;
                        case 'b':p++;s+='\b';break;
                        case 'r':p++;s+='\r';break;
                        case '\\':p++;s+='\\';break;
                        case '"':p++;s+='\"';break;
                        case '\'':p++;s+='\'';break;
                        default:
                        if(isdigit(text[p])){
                            char res;
                            res+=64*(text[p++]-'0');
                            res+=8*(text[p++]-'0');
                            res+=(text[p++]-'0');
                            s+=res;
                        }
                        else throw;
                    }/*
                    if(res){
                        s+=res;
                        p++;
                    }
                    else{
                        if(isdigit(text[p])){
                            char res;
                            res+=64*(text[p++]-'0');
                            res+=8*(text[p++]-'0');
                            res+=(text[p++]-'0');
                            s+=res;
                        }
                        else throw;
                    }*/
                }
                else s+=text[p++];
            }
            p++;
            return Token(STR,s);
        }
        _throw("无法识别的字符");
    }
};
class Parser{
public:
    Lexer lexer;
    Token tk;
    Parser(Lexer a):lexer(a){
        tk=lexer.get();
    }
    Token eat(int a=-1){
        if(a==-1||tk.tp==a){
            Token _tk=tk;
            tk=lexer.get();
            return _tk;
        }
        _throw("语法错误");
    }
    AST*program(){
        vector<AST*> stmts;
        while(tk.tp!=EXIT){
            stmts.push_back(stmt());
        }
        return new Program(stmts);
    }
    AST*block(){
        eat(BEGIN);
        vector<AST*> stmts;
        while(tk.tp!=END){
            stmts.push_back(stmt());
        }
        eat(END);
        return new Block(stmts);
    }
    AST*stmt(){
        if(tk.tp==ID){
            if(tk.v=="print"){
                eat();
                AST*v=expr();
                eat(SEMICOLON);
                return new Print(v);
            }
            if(tk.v=="var"){
                eat();
                vector<string> names;
                vector<AST*> values;
                names.push_back(eat(ID).v);
                if(tk.tp==ASSIGN) eat(),values.push_back(expr());
                else values.push_back(new Const(Val(None())));
                while(tk.tp==COMMA){
                    eat();
                    names.push_back(eat(ID).v);
                    if(tk.tp==ASSIGN) eat(),values.push_back(expr());
                    else values.push_back(new Const(Val(None())));
                }
                eat(SEMICOLON);
                return new VarDecl(names,values);
            }
            if(tk.v=="if"){
                eat();
                vector<AST*> conds,cases;
                AST*defa=new NoOp();
                conds.push_back(expr());
                cases.push_back(block());
                while(tk.tp==ID&&tk.v=="elif"){
                    eat();
                    conds.push_back(expr());
                    cases.push_back(block());
                }
                if(tk.tp==ID&&tk.v=="else") eat(),defa=block();
                return new If(conds,cases,defa);
            }
            if(tk.v=="while"){
                eat();
                AST*cond=expr(),*body=block();
                return new While(cond,body);
            }
            if(tk.v=="break"){
                eat();
                eat(SEMICOLON);
                return new Break();
            }
            if(tk.v=="continue"){
                eat();
                eat(SEMICOLON);
                return new Continue();
            }
            if(tk.v=="return"){
                eat();
                AST*v=expr();
                eat(SEMICOLON);
                return new Return(v);
            }
        }
        AST*e=expr();
        eat(SEMICOLON);
        return e;
    }
    AST*expr(){
        AST*res=expr4();
        if(tk.tp==ASSIGN){
            eat();
            return new Assign(res,expr());
        }
        return res;
    }
    AST*expr4(){
        AST*res=expr3();
        while(tk.tp==AND||tk.tp==OR){
            int op=eat().tp;
            res=new BinOp(op,res,expr3());
        }
        return res;
    }
    AST*expr3(){
        AST*res=expr2();
        while(tk.tp==BAND||tk.tp==BOR||tk.tp==XOR){
            int op=eat().tp;
            res=new BinOp(op,res,expr2());
        }
        return res;
    }
    AST*expr2(){
        AST*res=expr1();
        while(tk.tp==EQ||tk.tp==NE||tk.tp==GT||tk.tp==LT||tk.tp==GE||tk.tp==LE){
            int op=eat().tp;
            res=new BinOp(op,res,expr1());
        }
        return res;
    }
    AST*expr1(){
        AST*res=expr0();
        while(tk.tp==SHL||tk.tp==SHR){
            int op=eat().tp;
            res=new BinOp(op,res,expr0());
        }
        return res;
    }
    AST*expr0(){
        AST*res=term();
        while(tk.tp==ADD||tk.tp==SUB){
            int op=eat().tp;
            res=new BinOp(op,res,term());
        }
        return res;
    }
    AST*term(){
        AST*res=factor();
        while(tk.tp==MUL||tk.tp==DIV||tk.tp==MOD){
            int op=eat().tp;
            res=new BinOp(op,res,factor());
        }
        return res;
    }
    AST*factor(){
        if(tk.tp==ID&&tk.v=="lambda"){
            eat();
            eat(LPAREN);
            vector<string>para;
            if(tk.tp!=RPAREN){
                para.push_back(eat(ID).v);
                while(tk.tp==COMMA){
                    eat();
                    para.push_back(eat(ID).v);
                }
            }
            eat(RPAREN);
            return fh(new Lambda(para,block()));
        }
        if(tk.tp==INUM){
            int res=stoi(eat().v);
            return fh(new Const(Val(res)));
        }
        if(tk.tp==FNUM){
            float res=stof(eat().v);
            return fh(new Const(Val(res)));
        }
        if(tk.tp==STR){
            string res=eat().v;
            return fh(new Const(Val(res)));
        }
        if(tk.tp==NON){
            eat();
            return fh(new Const(Val(None())));
        }
        if(tk.tp==ID) return fh(new Var(eat().v));
        if(tk.tp==LPAREN){
            eat();
            AST*v=expr();
            eat(RPAREN);
            return fh(v);
        }
        if(tk.tp==LSB){
            eat();
            vector<AST*> res;
            if(tk.tp!=RSB){
                res.push_back(expr());
                while(tk.tp==COMMA){
                    eat();
                    res.push_back(expr());
                }
            }
            eat(RSB);
            return fh(new List(res));
        }
        if(tk.tp==ADD||tk.tp==SUB||tk.tp==NOT||tk.tp==INV) return new UnaryOp(eat().tp,fh(factor()));
        _throw("语法错误");
    }
    AST*fh(AST*v){
        if(tk.tp==LSB){
            eat();
            AST*r=expr();
            eat(RSB);
            return fh(new Element(v,r));
        }
        if(tk.tp==LPAREN){
            eat();
            vector<AST*> args;
            if(tk.tp!=RPAREN){
                args.push_back(expr());
                while(tk.tp==COMMA){
                    eat();
                    args.push_back(expr());
                }
            }
            eat(RPAREN);
            return fh(new CallFunc(v,args));
        }
        return v;
    }
};
int main()
{
    AST*tree=Parser(Lexer("\
print ~1;\
print \"\\n\";\
print -1.2;\
")).program();
    puts("语法分析结束");
    scope.inscope();
    scope.define("chr",(function<Val(vector<Val>)>)[](vector<Val>args)->Val{
        if(args.size()!=1) _throw("参数数量错误");
        if(args[0].tp!=INT) _throw("chr函数要求参数是整型");
        return ctos(args[0].iv);
    });
    scope.define("ord",(function<Val(vector<Val>)>)[](vector<Val>args)->Val{
        if(args.size()!=1) _throw("参数数量错误");
        if(args[0].tp!=STRING) _throw("ord函数要求参数是字符串");
        if(args[0].sv.size()!=1) _throw("ord函数要求参数是只有一个字符的字符串");
        return args[0].sv[0];
    });
    scope.define("len",(function<Val(vector<Val>)>)[](vector<Val>args)->Val{
        if(args.size()!=1) _throw("参数数量错误");
        if(args[0].tp==STRING) return (int)args[0].sv.size();
        else if(args[0].tp==LIST) return (int)args[0].lv.size();
        else _throw("len函数要求参数是字符串或列表");
    });
    scope.define("readln",(function<Val(vector<Val>)>)[](vector<Val>args)->Val{
        if(args.size()!=0) _throw("参数数量错误");
        string s;
        getline(cin,s);
        return s;
    });
    scope.define("stoi",(function<Val(vector<Val>)>)[](vector<Val>args)->Val{
        if(args.size()!=1) _throw("参数数量错误");
        if(args[0].tp==STRING) return stoi(args[0].sv);
        else _throw("stoi函数要求参数是字符串");
    });
    scope.define("stof",(function<Val(vector<Val>)>)[](vector<Val>args)->Val{
        if(args.size()!=1) _throw("参数数量错误");
        if(args[0].tp==STRING) return stof(args[0].sv);
        else _throw("stof函数要求参数是字符串");
    });
    scope.define("to_string",(function<Val(vector<Val>)>)[](vector<Val>args)->Val{
        if(args.size()!=1) _throw("参数数量错误");
        return args[0].tostr();
    });
    tree->eval();
    scope.outscope();
    puts("\n运行结束");
    return 0;
}
/*
var a=2;\
if a==0{print \"a=0\";}\
elif a==1{print \"a=1\";}\
else{print \"a=2\";}\

var a=0;\
while a<10{\
    print a;\
    print \"\\n\";\
    a=a+1;\
}\

print \"Hello!\\n\";\
var a=0;\
while a<10{\
    print a;\
    print \"\\n\";\
    a=a+1;\
}\
print a;\

print \"Hello\"+\"Hello!\"[5];\

var i=0;\
while 1{\
    if i==10{break;}\
    i=i+1;\
    if i==5{continue;}\
    print i;\
}\

var f=lambda(a){\
    print a;\
    return \"world!\\n\";\
};\

*/