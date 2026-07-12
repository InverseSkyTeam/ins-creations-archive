#include <bits/stdc++.h>
using namespace std;
enum{
    Add,Sub,Mul,Div,Mod,
    Eq,Ne,Gt,Lt,Ge,Le,
    Lsh,Rsh,
    And,Or,BitAnd,BitOr,Xor,
    Not,Inv,

    Eof,
    Const,Id,
    Begin,End,LParen,RParen,LSB,RSB,
    Semi,Colon,Dot,Comma,Assign,Arrow,
};
int get_prio(int op){
    if(op==Mul||op==Div||op==Mod) return 100;
    if(op==Add||op==Sub) return 99;
    if(op==Lsh||op==Rsh) return 98;
    if(op==Eq||op==Ne||op==Gt||op==Lt||op==Ge||op==Le) return 97;
    if(op==BitAnd||op==BitOr||op==Xor) return 96;
    if(op==And||op==Or) return 95;
    return -1;
}
class Statement;
struct value;
struct Scope;
struct Fn;
struct value{
    string ctos(char a){
        stringstream ss;
        ss<<a;
        return ss.str();
    }
    enum{
        Int,Float,Bool,Str,Null,List,Func,BuiltinFunc,
    };
    int tp;
    void* val;
    value(int a):tp(Int),val((void*)(new int(a))){}
    value(float a):tp(Float),val((void*)(new float(a))){}
    value(bool a):tp(Bool),val((void*)(new bool(a))){}
    value(string a):tp(Str),val((void*)(new string(a))){}
    value():tp(Null),val(0){}
    value(vector<value> a):tp(List),val(new vector<value>(a)){}
    value(Fn a);
    value(function<value(vector<value>)> a):tp(BuiltinFunc),val(new function<value(vector<value>)>(a)){}
    value unary(int op){
        if(tp==Int||tp==Bool){
            int v;
            if(tp==Int) v=*(int*)val;
            else v=*(bool*)val;
            switch(op){
                case Add:return v;
                case Sub:return -v;
                case Not:return !v;
                case Inv:return ~v;
                default:throw "Unary:Invalid operator.";
            }
        }
        if(tp==Float){
            float v=*(float*)val;
            switch(op){
                case Add:return v;
                case Sub:return -v;
                case Not:return !v;
                default:throw "Unary:Invalid operator.";
            }
        }
        throw "Unary:Invalid type.";
    }
    value binary(int op,value b){
        if((tp==Int||tp==Float||tp==Bool)&&(b.tp==Int||b.tp==Float||b.tp==Bool)){
            if(tp==Float||b.tp==Float){
                float av,bv;
                if(tp==Float) av=*(float*)val;
                if(tp==Int) av=*(int*)val;
                if(tp==Bool) av=*(bool*)val;
                if(b.tp==Float) bv=*(float*)b.val;
                if(b.tp==Int) bv=*(int*)b.val;
                if(b.tp==Bool) bv=*(bool*)b.val;
                switch(op){
                    case Add:return av+bv;
                    case Sub:return av-bv;
                    case Mul:return av*bv;
                    case Div:return av/bv;
                    case Eq:return av==bv;
                    case Ne:return av!=bv;
                    case Gt:return av>bv;
                    case Lt:return av<bv;
                    case Ge:return av>=bv;
                    case Le:return av<=bv;
                    case And:return av&&bv;
                    case Or:return av||bv;
                    default:throw "Binary:Invalid operator.";
                }
            }
            else{
                int av,bv;
                if(tp==Int) av=*(int*)val;
                if(tp==Bool) av=*(bool*)val;
                if(b.tp==Int) bv=*(int*)b.val;
                if(b.tp==Bool) bv=*(bool*)b.val;
                switch(op){
                    case Add:return av+bv;
                    case Sub:return av-bv;
                    case Mul:return av*bv;
                    case Div:return av/bv;
                    case Mod:return av%bv;
                    case Eq:return av==bv;
                    case Ne:return av!=bv;
                    case Gt:return av>bv;
                    case Lt:return av<bv;
                    case Ge:return av>=bv;
                    case Le:return av<=bv;
                    case Lsh:return av<<bv;
                    case Rsh:return av>>bv;
                    case And:return av&&bv;
                    case Or:return av||bv;
                    case BitAnd:return av&bv;
                    case BitOr:return av|bv;
                    case Xor:return av^bv;
                    default:throw "Binary:Invalid operator.";
                }
            }
        }
        if(op==Add&&tp==Str&&b.tp==Str) return *(string*)val+*(string*)b.val;
        throw "Binary:Invalid type.";
    }
    value noref_index(value v){
        if(v.tp!=Int) throw "Index:Index is not integer.";
        if(tp==List) return (*(vector<value>*)val)[*(int*)v.val];
        if(tp==Str) return ctos((*(string*)val)[*(int*)v.val]);
        throw "Index:Object is not list or str.";
    }
    value& ref_index(value v){
        if(v.tp!=Int) throw "Index:Index is not integer.";
        if(tp==List) return (*(vector<value>*)val)[*(int*)v.val];
        throw "Index:Object is not list.";
    }
    void print(){
        switch(tp){
            case Int:cout<<*(int*)val;break;
            case Float:cout<<*(float*)val;break;
            case Str:cout<<*(string*)val;break;
            case Null:cout<<"null";break;
            case Bool:cout<<*(bool*)val;break;
            case List:{
                cout<<"[";
                vector<value> v=*(vector<value>*)val;
                if(v.size()){
                    for(int i=0;i<v.size()-1;i++){
                        v[i].print();
                        cout<<", ";
                    }
                    v[v.size()-1].print();
                }
                cout<<"]";
                break;
            }
            default:throw "Print:Can't convert the value to str.";
        }
    }
    bool to_bool(){
        switch(tp){
            case Int:return *(int*)val;
            case Bool:return *(bool*)val;
            case Float:return *(float*)val;
            case Str:return ((string*)val)->size();
            case List:return ((vector<value>*)val)->size();
            case Null:return 0;
            default:return "ToBool:Can't convert the value to bool.";
        }
    }
    value call(vector<value> args);
};
struct Scope{
    vector<map<string,value> > v;
    Scope(){
        v.push_back(map<string,value>());
    }
    value&find(string name){
        for(int i=v.size()-1;i>=0;i--){
            if(v[i].find(name)!=v[i].end()) return v[i][name];
        }
        throw "Find:Undefined variable.";
    }
    void define(string name,value val){
        v[v.size()-1][name]=val;
    }
    void buildin(string name,function<value(vector<value>)> val){
        v[v.size()-1][name]=val;
    }
    void in(map<string,value> mp=map<string,value>()){
        v.push_back(mp);
    }
    void out(){
        v.pop_back();
    }
};
struct Fn{
    vector<string> para;
    Statement*body;
    Scope scope;//Scope而非Scope&，即无法修改上级作用域
    Fn(vector<string> p,Statement*b,Scope s):para(p),body(b),scope(s){}
};
value::value(Fn a):tp(Func),val(new Fn(a)){}
enum{
    Break,Continue,Return,NoSignal
};
struct Signal{
    int signal;
    value retval;
    Signal(int s):signal(s){}
    Signal(value rv):retval(rv),signal(Return){}
};
class Expression{
public:
    virtual value eval(Scope&scope)=0;
    virtual value&ref(Scope&scope)=0;
};
class Statement{
public:
    virtual Signal run(Scope&scope)=0;
};
value value::call(vector<value> args){
    if(tp==BuiltinFunc) return (*(function<value(vector<value>)>*)val)(args);
    if(tp==Func){
        Fn fn=*(Fn*)val;
        map<string,value> mp;
        if(args.size()!=fn.para.size()) throw "Call:Unmatched arguments.";
        for(int i=0;i<args.size();i++) mp[fn.para[i]]=args[i];
        Scope scope=fn.scope;
        scope.in(mp);
        Signal sig=fn.body->run(scope);
        if(sig.signal==NoSignal) return value();
        return sig.retval;
    }
    throw "Call:Expect a function";
}
class ConstExpr:public Expression{
public:
    value v;
    ConstExpr(value a):v(a){}
    value eval(Scope&scope){
        return v;
    }
    value&ref(Scope&scope){throw "Ref:Wrong lvalue.";}
};
class Variable:public Expression{
public:
    string name;
    Variable(string n):name(n){}
    value eval(Scope&scope){
        return scope.find(name);
    }
    value&ref(Scope&scope){return scope.find(name);}
};
class Binary:public Expression{
public:
    int op;
    Expression *l,*r;
    Binary(int x,Expression*a,Expression*b):op(x),l(a),r(b){}
    value eval(Scope&scope){
        return l->eval(scope).binary(op,r->eval(scope));
    }
    value&ref(Scope&scope){throw "Ref:Wrong lvalue.";}
};
class Unary:public Expression{
public:
    int op;
    Expression *v;
    Unary(int x,Expression*a):op(x),v(a){}
    value eval(Scope&scope){
        return v->eval(scope).unary(op);
    }
    value&ref(Scope&scope){throw "Ref:Wrong lvalue.";}
};
class Index:public Expression{
public:
    Expression*obj,*index;
    Index(Expression*o,Expression*i):obj(o),index(i){}
    value eval(Scope&scope){
        return obj->eval(scope).noref_index(index->eval(scope));
    }
    value&ref(Scope&scope){return obj->eval(scope).ref_index(index->eval(scope));}
};
class MakeList:public Expression{
public:
    vector<Expression*> v;
    MakeList(vector<Expression*> a):v(a){}
    value eval(Scope&scope){
        vector<value> r;
        for(Expression*i:v) r.push_back(i->eval(scope));
        return r;
    }
    value&ref(Scope&scope){throw "Ref:Wrong lvalue.";}
};
class Lambda:public Expression{
public:
    vector<string> para;
    Statement*body;
    Lambda(vector<string> p,Statement*b):para(p),body(b){}
    value eval(Scope&scope){
        return Fn(para,body,scope);
    }
    value&ref(Scope&scope){throw "Ref:Wrong lvalue.";}
};
class Call:public Expression{
public:
    Expression*fn;
    vector<Expression*>args;
    Call(Expression*a,vector<Expression*>b):fn(a),args(b){}
    value eval(Scope&scope){
        vector<value> v;
        for(Expression*i:args) v.push_back(i->eval(scope));
        return fn->eval(scope).call(v);
    }
    value&ref(Scope&scope){throw "Ref:Wrong lvalue.";}
};
class ExprStmt:public Statement{
public:
    Expression*e;
    ExprStmt(Expression*a):e(a){}
    Signal run(Scope&scope){
        e->eval(scope);
        return Signal(NoSignal);
    }
};
class LetStmt:public Statement{
public:
    vector<string> names;
    vector<Expression*> values;
    LetStmt(vector<string> n,vector<Expression*> v):names(n),values(v){}
    Signal run(Scope&scope){
        for(int i=0;i<names.size();i++) scope.define(names[i],values[i]->eval(scope));
        return Signal(NoSignal);
    }
};
class PrintStmt:public Statement{
public:
    Expression*v;
    PrintStmt(Expression*a):v(a){}
    Signal run(Scope&scope){
        v->eval(scope).print();
        return Signal(NoSignal);
    }
};
class Block:public Statement{
public:
    vector<Statement*> v;
    Block(vector<Statement*> a):v(a){}
    Signal run(Scope&scope){
        for(Statement*i:v){
            Signal a=i->run(scope);
            if(a.signal!=NoSignal) return a;
        }
        return Signal(NoSignal);
    }
};
class AssignStmt:public Statement{
public:
    Expression*l,*r;
    AssignStmt(Expression*a,Expression*b):l(a),r(b){}
    Signal run(Scope&scope){
        l->ref(scope)=r->eval(scope);
        return Signal(NoSignal);
    }
};
class WhileStmt:public Statement{
public:
    Expression*cond;
    Statement*body;
    WhileStmt(Expression*a,Statement*b):cond(a),body(b){}
    Signal run(Scope&scope){
        while(cond->eval(scope).to_bool()){
            scope.in();
            Signal v=body->run(scope);
            scope.out();
            if(v.signal==Break) break;
            if(v.signal==Return) return v;
        }
        return Signal(NoSignal);
    }
};
class IfStmt:public Statement{
public:
    Expression*cond;
    Statement*t,*f;
    IfStmt(Expression*a,Statement*b,Statement*c):cond(a),t(b),f(c){}
    Signal run(Scope&scope){
        if(cond->eval(scope).to_bool()){
            scope.in();
            Signal v=t->run(scope);
            scope.out();
            return v;
        }
        scope.in();
        Signal v=f->run(scope);
        scope.out();
        return v;
    }
};
class NoOp:public Statement{
public:
    NoOp(){}
    Signal run(Scope&scope){
        return Signal(NoSignal);
    }
};
class BreakStmt:public Statement{
public:
    BreakStmt(){}
    Signal run(Scope&scope){
        return Signal(Break);
    }
};
class ContinueStmt:public Statement{
public:
    ContinueStmt(){}
    Signal run(Scope&scope){
        return Signal(Continue);
    }
};
class ReturnStmt:public Statement{
public:
    Expression*r;
    ReturnStmt(Expression*a):r(a){}
    Signal run(Scope&scope){
        return Signal(r->eval(scope));
    }
};
struct Token{
    int tp;
    string v;
    Token(){}
    Token(int a,string b=""):tp(a),v(b){}
    void print(){
        cout<<"tp:"<<tp<<" "<<"v:"<<v<<endl;
    }
};
vector<Token> lex(string s){
    size_t p=0;
    vector<Token> res;
    while(p<s.size()){
        while(p<s.size()&&(s[p]==' '||s[p]=='\n'||s[p]=='\t')) p++;
        if(p==s.size()) break;
        if(isdigit(s[p])){
            string x;
            while(p<s.size()&&(isdigit(s[p])||s[p]=='.')) x+=s[p++];
            res.push_back(Token(Const,x));
        }
        else if(isalpha(s[p])||s[p]=='_'){
            string x;
            while(p<s.size()&&(isalnum(s[p])||s[p]=='_')) x+=s[p++];
            res.push_back(Token(Id,x));
        }
        else if(s[p]=='"'){
            p++;
            string x="\"";
            while(p<s.size()&&s[p]!='"'){
                if(s[p]=='\\'){
                    p++;
                    if(isdigit(s[p])){
                        x+=stoi(s.substr(p,3),0,8);
                        p+=3;
                    }
                    else{
                        switch(s[p++]){
                            case 'e':x+='\e';break;
                            case 'r':x+='\r';break;
                            case 't':x+='\t';break;
                            case 'a':x+='\a';break;
                            case 'f':x+='\f';break;
                            case 'v':x+='\v';break;
                            case 'b':x+='\b';break;
                            case 'n':x+='\n';break;
                            case '"':x+='"';break;
                            case '\'':x+='\'';break;
                            case '\\':x+='\\';break;
                            default:throw "Lex:Wrong input.";
                        }
                    }
                }
                else x+=s[p++];
            }
            if(p==s.size()) throw "Lex:Wrong input.";
            x+=s[p++];
            res.push_back(Token(Const,x));
        }
        #define f(op,name) else if(s.substr(p,string(#op).size())==#op) res.push_back(Token(name)),p+=string(#op).size();
        f(+,Add)f(-,Sub)f(*,Mul)f(/,Div)f(%,Mod)
        f(=>,Arrow)f(==,Eq)f(!=,Ne)f(>=,Ge)f(<=,Le)
        f(<<,Lsh)f(>>,Rsh)
        f(>,Gt)f(<,Lt)
        f(&&,And)f(||,Or)f(&,BitAnd)f(|,BitOr)f(^,Xor)
        f(!,Not)f(~,Inv)
        f({,Begin)f(},End)f([,LSB)f(],RSB)
        f(;,Semi)f(:,Colon)f(.,Dot)f(=,Assign)
        else if(s.substr(p,string("(").size())=="(") res.push_back(Token(LParen)),p+=string("(").size();
        else if(s.substr(p,string("(").size())==")") res.push_back(Token(RParen)),p+=string(")").size();
        else if(s.substr(p,string(",").size())==",") res.push_back(Token(Comma)),p+=string(",").size();
        #undef f
        else{
            throw "Lex:Wrong input.";
        }
    }
    res.push_back(Token(Eof));
    return res;
}
struct Parser{
    vector<Token> tokens;
    Token tk;
    int p;
    Parser(vector<Token> a):tokens(a),tk(a[0]),p(0){}
    Token eat(int ex=-1){
        if(ex==-1||tk.tp==ex){
            tk=tokens[++p];
            return tokens[p-1];
        }
        //cout<<ex<<" "<<tk.tp;
        throw "Parser:Unmatched token.";
    }
    int getPair(){
        if(tk.tp!=LParen) throw;
        int x=p+1;
        int l=1,r=0;
        while(x<tokens.size()){
            if(tokens[x].tp==LParen) l++;
            if(tokens[x].tp==RParen){
                if(l) l--;
                else r++;
            }
            if(l==0&&r==0) return x;
            x++;
        }
        throw "GetPair:Unmatched parentheses.";
    }
    Statement*block(){
        if(tk.tp!=Begin){
            vector<Statement*> l{stmt()};
            return new Block(l);
        }
        eat(Begin);
        vector<Statement*> l;
        while(tk.tp!=End){
            l.push_back(stmt());
        }
        eat(End);
        return new Block(l);
    }
    Statement*stmt(){
        if(tk.tp==Id){
            /*if(tk.v==string("print")){
                eat();
                Expression*e=expr();
                eat(Semi);
                return new PrintStmt(e);
            }*/
            if(tk.v==string("let")){
                eat();
                vector<string> names{eat(Id).v};
                vector<Expression*> values{new ConstExpr(value())};
                if(tk.tp==Assign){
                    eat();
                    values[values.size()-1]=expr();
                }
                while(tk.tp==Comma){
                    eat();
                    names.push_back(eat(Id).v);
                    if(tk.tp==Assign){
                        eat();
                        values.push_back(expr());
                    }
                    else values.push_back(new ConstExpr(value()));
                }
                eat(Semi);
                return new LetStmt(names,values);
            }
            if(tk.v=="while"){
                eat();
                eat(LParen);
                Expression*e=expr();
                eat(RParen);
                return new WhileStmt(e,block());
            }
            if(tk.v=="if"){
                eat();
                eat(LParen);
                Expression*e=expr();
                eat(RParen);
                Statement*t=block();
                if(tk.tp==Id&&tk.v=="else"){
                    eat();
                    return new IfStmt(e,t,block());
                }
                return new IfStmt(e,t,new NoOp());
            }
            if(tk.v=="break"){
                eat();
                eat(Semi);
                return new BreakStmt();
            }
            if(tk.v=="continue"){
                eat();
                eat(Semi);
                return new ContinueStmt();
            }
            if(tk.v=="return"){
                eat();
                Expression*e=expr();
                eat(Semi);
                return new ReturnStmt(e);
            }
        }
        Expression*e=expr();
        if(tk.tp==Assign){
            eat();
            Expression*v=expr();
            eat(Semi);
            return new AssignStmt(e,v);
        }
        eat(Semi);
        return new ExprStmt(e);
    }
    Expression*expr(){
        Expression*_res=factor();
        if(tk.tp<=Xor){
            int a=eat().tp;
            Binary res=Binary(a,_res,factor());
            while(tk.tp<=Xor){
                int op=eat().tp;
                int prio=get_prio(op);
                Expression*r=factor();
                if(get_prio(res.op)>prio) res=Binary(op,new Binary(res),r);
                else res=Binary(res.op,res.l,new Binary(op,res.r,r));
            }
            return new Binary(res);
        }
        return _res;
    }
    Expression*factor(){
        if(tk.tp==Const){
            string t=eat().v;
            if(isdigit(t[0])){
                if(t.find(".")!=string::npos) return fh(new ConstExpr(stof(t)));
                else return fh(new ConstExpr(stoi(t)));
            }
            if(t[0]=='"') return fh(new ConstExpr(t.substr(1,t.size()-2)));
        }
        if(tk.tp==Id) return fh(new Variable(eat().v));
        if(tk.tp==LParen){
            if(tokens[getPair()+1].tp==Arrow){
                eat();
                vector<string> para;
                if(tk.tp!=RParen){
                    para.push_back(eat(Id).v);
                    while(tk.tp==Comma){
                        eat();
                        para.push_back(eat(Id).v);
                    }
                }
                eat(RParen);
                eat(Arrow);
                return fh(new Lambda(para,block()));
            }
            eat();
            Expression*e=expr();
            eat(RParen);
            return fh(e);
        }
        if(tk.tp==Add||tk.tp==Sub||tk.tp==Not||tk.tp==Inv){
            int op=eat().tp;
            return new Unary(op,factor());
        }
        if(tk.tp==LSB){
            eat();
            vector<Expression*> l;
            if(tk.tp!=RSB){
                l.push_back(expr());
                while(tk.tp==Comma){
                    eat();
                    l.push_back(expr());
                }
            }
            eat(RSB);
            return fh(new MakeList(l));
        }
        tk.print();
        throw "Parse:Can't parse this token.";
    }
    Expression*fh(Expression*v){
        if(tk.tp==LSB){
            eat();
            Expression*idx=expr();
            eat(RSB);
            return fh(new Index(v,idx));
        }
        if(tk.tp==LParen){
            eat();
            vector<Expression*> args;
            if(tk.tp!=RParen){
                args.push_back(expr());
                while(tk.tp==Comma){
                    eat();
                    args.push_back(expr());
                }
            }
            eat(RParen);
            return fh(new Call(v,args));
        }
        return v;
    }
};
int main(int argc,char**argv)
{
    /*value v1(vector<value>{1,2,2});
    value v2=v1;
    v2.ref_index(2)=3;
    v1.noref_index(2).print();*/
    Scope scope;
    scope.buildin("print",[](vector<value> args){
        for(value i:args) i.print();
        return value();
    });
    scope.buildin("println",[](vector<value> args){
        for(value i:args) i.print();
        puts("");
        return value();
    });
    scope.buildin("readln",[](vector<value> args){
        string s;
        getline(cin,s);
        return s;
    });
    scope.buildin("getchar",[](vector<value> args){
        string s;
        s+=getchar();
        return s;
    });
    scope.buildin("ord",[](vector<value> a){
        return (*(string*)a[0].val)[0];
    });
    scope.buildin("chr",[](vector<value> a){
        string s;
        s+=*(int*)a[0].val;
        return s;
    });
    scope.buildin("length",[](vector<value> a){
        if(a[0].tp==value::Str) return (int)(*(string*)a[0].val).size();
        if(a[0].tp==value::List) return (int)(*(vector<value>*)a[0].val).size();
        throw "Length:Type of object isn't str or list.";
    });
    /*FILE*f=fopen("test_program.cnl","r");
    string s;
    while(!feof(f)){
        s+=fgetc(f);
    }
    s=s.substr(0,s.size()-1);
    vector<Token> tokens=lex(s);
    //for(Token i:tokens) i.print();
    Parser(tokens).block()->run(scope);*/
    return 0;
}