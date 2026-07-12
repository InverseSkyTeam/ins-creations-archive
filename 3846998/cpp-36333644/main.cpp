/*
func puts(str){
    for i=0 to length str{
        putchar str[i];
    }
}
func main(){
    expr puts("Hello,world!");
}

program:assign*'.'
stmt:((expr|prints|putchars)';')|fors|ifs|whiles|block
expr:...
prints:'print'expr
putchars:'putchar'expr;
fors:'for'id'='expr'to'expr('skip'expr)? block
ifs:'if''('expr')'block('else''if''('expr')'block)*('else'block)?
whiles:...
block:'{'stmt*'}'
id:...
*/
#include <bits/stdc++.h>
using namespace std;
string ctos(char a){
    stringstream ss;
    ss<<a;
    return ss.str();
}
bool isid(char c){return isalnum(c)||c=='_';}
bool isidf(char c){return isid(c)&&!isdigit(c);}
void raise(string s=""){
    cout<<s<<"\n";
    throw;
}
struct Scope;
template<typename T>
vector<T> operator+(vector<T> a,vector<T> b){
    vector<T> c=a;
    c.insert(c.end(),b.begin(),b.end());
    return c;
}
struct Func{
    vector<string> params;
    Scope*scope;
    string code;
    Func(){}
    Func(vector<string> pm,Scope*p,string c):params(pm),scope(p),code(c){}
};
struct NoneType{};
enum{
    Break,
    Continue,
    CantFind,
    NoInitValue
};
struct SC{
    int n;
    SC(int a):n(a){}
};
struct Val;
struct Type{
    vector<Val> parents;
    map<string,Val> attr;
    Type(vector<Val> p,map<string,Val> a):parents(p),attr(a){}
};
struct Object{
    //string t;
    map<string,Val> attr;
    Object(/*string p,*/map<string,Val> a):/*t(p),*/attr(a){}
};
struct Val{
    int *Iv=0;
    vector<Val> *Lv=0;
    Func *Fv=0;
    NoneType *Nv=0;
    char *Cv=0;
    SC *SCv=0;
    Type *Tv=0;
    Object *Ov=0;
    Val(){}
    Val(int a){Iv=new int(a);}
    Val(char a){Cv=new char(a);}
    Val(vector<Val> a){Lv=new vector<Val>(a);}
    Val(Func a){Fv=new Func(a);}
    Val(NoneType a){Nv=new NoneType;}
    Val(SC a){SCv=new SC(a);}
    Val(Type a){Tv=new Type(a);}
    Val(Object a){Ov=new Object(a);}
    string ltos(){
        string s;
        for(auto i:*Lv) s+=*i.Cv;
        return s;
    }
    operator string(){if(Nv) return "None";if(Iv) return to_string(*Iv);if(Cv) return ctos(*Cv);throw;}
    operator bool(){if(Iv) return bool(*Iv);if(Lv) return bool((*Lv).size());if(Nv) return 0;throw;}
    Val operator+(Val b){if(Iv&&b.Iv) return (*Iv)+(*b.Iv);if(Lv&&b.Lv) return (*Lv)+(*b.Lv);throw;}
    Val operator-(Val b){if(Iv&&b.Iv) return (*Iv)-(*b.Iv);if(Ov) return callFunc(*get("operatorSub"),vector<Val>{*Ov,*b.Ov});throw;}
    Val operator*(Val b){if(Iv&&b.Iv) return (*Iv)*(*b.Iv);throw;}
    Val operator/(Val b){if(Iv&&b.Iv) return (*Iv)/(*b.Iv);throw;}
    Val operator%(Val b){if(Iv&&b.Iv) return (*Iv)%(*b.Iv);throw;}
    Val operator==(Val b){if(Iv&&b.Iv) return (*Iv)==(*b.Iv);throw;}
    Val operator!=(Val b){if(Iv&&b.Iv) return (*Iv)!=(*b.Iv);throw;}
    Val operator<=(Val b){if(Iv&&b.Iv) return (*Iv)<=(*b.Iv);throw;}
    Val operator>=(Val b){if(Iv&&b.Iv) return (*Iv)>=(*b.Iv);throw;}
    Val operator<(Val b){if(Iv&&b.Iv) return (*Iv)<(*b.Iv);throw;}
    Val operator>(Val b){if(Iv&&b.Iv) return (*Iv)>(*b.Iv);throw;}
    Val operator&&(Val b){if(Iv&&b.Iv) return (*Iv)&&(*b.Iv);throw;}
    Val operator||(Val b){if(Iv&&b.Iv) return (*Iv)||(*b.Iv);throw;}
    Val operator&(Val b){if(Iv&&b.Iv) return (*Iv)&(*b.Iv);throw;}
    Val operator|(Val b){if(Iv&&b.Iv) return (*Iv)|(*b.Iv);throw;}
    Val operator^(Val b){if(Iv&&b.Iv) return (*Iv)^(*b.Iv);throw;}
    Val* operator[](Val b){if(Lv&&b.Iv) return &(*Lv)[*b.Iv];if(Ov&&b.Iv) return &get(get("__listAttr__")->ltos())[*b.Iv];throw;}
    Val operator+(){if(Iv) return +(*Iv);throw;}
    Val operator-(){if(Iv) return -(*Iv);throw;}
    Val operator!(){if(Iv) return !(*Iv);throw;}
    Val operator~(){if(Iv) return ~(*Iv);throw;}
    Val length(){if(Lv) return (int)Lv->size();throw;}
    string type(){
        if(Iv) return "int";
        if(Lv) return "list";
        if(Fv) return "func";
        if(Nv) return "NoneType";
        if(Cv) return "char";
        if(SCv) return "SpecialCode";
        if(Tv) return "type";
        if(Ov) return "object";
        throw;
    }
    Val* get(string name){
        if(Tv){
            if(Tv->attr.find(name)!=Tv->attr.end()) return &Tv->attr[name];
            else{
                for(Val i:Tv->parents){
                    Val* g=i.get(name);
                    if(g!=new Val(SC(CantFind))) return g;
                }
                return new Val(SC(CantFind));
            }
        }
        if(Ov){ 
            if(Ov->attr.find(name)!=Ov->attr.end()) return &Ov->attr[name];
            else return new Val(SC(CantFind));
        }
        throw;
    }
    map<string,Val> getAttrs(){
        if(!Tv) throw;
        map<string,Val> a=Tv->attr;
        for(Val i:Tv->parents) for(auto j:i.getAttrs()) if(a.find(j.first)==a.end()) a.insert(j);
        return a;
    }
    Val _new(){
        if(!Tv) throw;
        map<string,Val> a=this->getAttrs();
        return Object(a);
    }
    Val _new(vector<Val> args);
    Val callFunc(Val w,vector<Val> args);
};
struct Scope{
    Scope*parent;
    map<string,Val> var;
    Scope(){}
    Scope(Scope *a){parent=a;}
    void top_set(string n,Val v){*top_find(n)=v;}
    void define(string n,Val v){var[n]=v;}
    Val* top_find(string n){
        if(var.find(n)!=var.end()) return &var[n];
        throw "Used an undefined variable '"+n+"'!";
    }
    Val* find(string n){
        Scope*s=this;
        try{return s->top_find(n);}
        catch(...){
            try{return s->parent->find(n);}
            catch(...){raise("Used an undefined variable '"+n+"'!");}
        }
    }
};
ostream&operator<<(ostream&cout,Val a){cout<<string(a);return cout;}
#define H {\
    pass("var");\
    string name=getId();\
    Val v=0;\
    if(match("=")) pass("="),v=expr();\
    scope->define(name,v);\
    pass(";");\
}
struct Runner{
    string code;
    Scope*scope;
    bool hasThis=0;
    Runner(){}
    Runner(string c,Scope *s=new Scope(0)):code(c),scope(s){}
    void pre(){while(code[0]==' '||code[0]=='\n'||code[0]=='\t') pass();}
    void pass(int a=1){code.erase(code.begin(),code.begin()+a);}
    void pass(string a){pre(),code.erase(code.begin(),code.begin()+a.size());}
    bool match(string s){pre();return code.substr(0,s.size())==s;}
    bool matchId(string s){pre();return !isid(code[s.size()])&&code.substr(0,s.size())==s;}
    string getId(){pre();string ans="";while(isid(code[0])) ans+=code[0],pass();return ans;}
    string nextId(){pre();string w=code,ans=getId();code=w;return ans;}
    string getBlock(){
        string ans;
        int l=1,r=0;
        while(1){
            pass(),ans+=code[0];
            if(code[0]=='{') l++;
            if(code[0]=='}') r++;
            if(l&&r) l--,r--;
            if(!l){
                pass();
                return ans.substr(0,ans.size()-1);
            }
        }
        return "";
    }
    void program(){
        //cout<<expr();
        /*if(!match("It is a program.")) raise("It is not a program!");
        cout<<"It is a program.";*/
        pre();
        while(code.size()){
            H
            pre();
        }
        callFunc(scope->var["main"],vector<Val>());
    }
    Val block(Scope*s=0){
        if(s==0) s=new Scope(scope);
        pass("(");
        Scope*l=scope;
        scope=s;
        Val ans=stmts();
        pass(")");
        scope=l;
        return ans;
    }
    Val stmt(){
        if(matchId("if")){
            pass("if");
            pass("(");
            Val cond=expr();
            pass(")");
            if(cond){
                Val ans=block();
                if(match("else")){
                    pass("else");
                    while(match("if")){
                        pass("if");
                        while(!match("{")) pass();
                        getBlock();
                        if(match("else")) pass("else");
                    }
                    getBlock();
                }
                return ans;
            }
            else{
                Val ans=NoneType();
                getBlock();
                if(matchId("else")){
                    pass("else");
                    bool nd=0,f=0;
                    while(matchId("if")){
                        pass("if");
                        if(!nd){
                            pass("(");
                            Val v=expr();
                            pass(")");
                            if(v) nd=1,ans=block();
                            else getBlock();
                        }
                        else{
                            while(!match("{")) pass();
                            getBlock();
                        }
                        if(matchId("else")) pass("else");
                        else f=1;
                    }
                    if(!nd&&!f) ans=block();
                }
                return ans;
            }
        }
        else if(matchId("while")){
            pass("while");
            pass("(");
            string l=code;
            Val cond=expr();
            while(cond){
                pass(")");
                Val ans=block();
                code=l;
                cond=expr();
                if(ans.SCv){
                    if(ans.SCv->n==Break) break;
                    if(ans.SCv->n==Continue) continue;
                }
                if(!ans.Nv) return ans;
            }
            pass(")"),getBlock();
        }
        else if(matchId("for")){
            pass("for");
            string name=getId();
            pass("=");
            Val a=expr();
            pass("to");
            Val b=expr();
            Val c=1;
            if(match("skip")) pass("skip"),c=expr();
            string bl=getBlock();
            Scope*ns=new Scope(scope);
            for(ns->var[name]=a;ns->var[name]<b;ns->var[name]=ns->var[name]+c){
                Val ans=Runner(bl,ns).stmts();
                if(ans.SCv){
                    if(ans.SCv->n==Break) break;
                    if(ans.SCv->n==Continue) continue;
                }
                if(!ans.Nv) return ans;
            }
        }
        else if(matchId("return")){
            pass("return");
            Val ans=expr();
            pass(";");
            return ans;
        }
        else if(matchId("break")){
            pass("break");
            pass(";");
            return SC(Break);
        }
        else if(matchId("continue")){
            pass("continue");
            pass(";");
            return SC(Continue);
        }
        else if(matchId("var"))H
        else if(matchId("script")) getId(),Runner(getBlock(),new Scope(scope)).program();
        else{
            bool f1=0,f2=0;
            for(int i=0;i<code.size();i++){
                if(!f1&&(code[i]=='\"'||code[i]=='\'')) f1=1;
                if(f1&&(code[i]=='\"'||code[i]=='\'')) f1=0;
                if(!f1&&code[i]=='='){
                    f2=1;
                    break;
                }
                if(!f1&&code[i]==';') break;
            }
            if(f2) assign();
            else expr();
            pass(";");
        }
        return NoneType();
    }
    Val stmts(){
        pre();
        while(code.size()&&!match("}")){
            Val ans=stmt();
            pre();
            if(!ans.Nv) return ans;
        }
        return NoneType();
    }
    Val assign(){
        Val*n=ah();
        if(!match("=")) raise("Expected '='.");
        pass();
        *n=expr();
        return NoneType();
    }
    Val* ah(){
        Val*v=scope->find(getId());
        while(match("[")||match(".")){
            if(match(".")) pass("."),v=v->get(getId());
            else if(match("[")) pass("["),v=(*v)[expr()],pass("]");
        }
        return v;
    }
    #define F(f,w) if(match(#f)) pass(#f),v=v f w();
    Val expr(){
        Val v=expr0();
        while(match("||")||match("&&")){F(||,expr0)F(&&,expr0)}
        return v;
    }
    Val expr0(){
        Val v=expr1();
        while(match("==")||match("!=")||match(">=")||
            match("<=")||match(">")||match("<")){
            F(==,expr1)F(!=,expr1)F(>=,expr1)
            F(<=,expr1)F(>,expr1)F(<,expr1)}
        return v;
    }
    Val expr1(){
        Val v=expr2();
        while(match("|")||match("&")||match("^")){F(|,expr2)F(&,expr2)F(^,expr2)}
        return v;
    }
    Val expr2(){
        Val v=expr3();
        while(match("+")||match("-")){F(+,expr3)F(-,expr3)}
        return v;
    }
    Val expr3(){
        Val v=factor();
        while(match("*")||match("/")||match("%")){F(*,factor)F(/,factor)F(%,factor)}
        return v;
    }
    Val factor(){
        if(match("\"")){
            vector<Val> s;
            pass();
            while(!match("\"")&&!match("'")) s.push_back((char)code[0]),pass();
            pass();
            return fh(s).second;
        }
        if(match("'")){
            pass();
            char a=code[0];
            pass(2);
            return a;
        }
        if(match("[")){
            pass();
            if(match("]")) return vector<Val>();
            vector<Val> v;
            v.push_back(expr());
            while(match(",")) pass(),v.push_back(expr());
            pass();
            return fh(v).second;
        }
        if(match("(")){
            pass();
            Val v=expr();
            pass(")");
            return fh(v).second;
        }
        if(isdigit(code[0])){
            string s;
            while(isdigit(code[0])) s+=code[0],pass();
            return fh(stoi(s)).second;
        }
        if(nextId()=="type"){
            pass("type");
            vector<Val> p;
            if(match(":")){
                pass();
                p.push_back(expr());
                while(match(",")) pass(","),p.push_back(expr());
            }
            pass("{");
            map<string,Val> a;
            if(match("}")){
                pass();
                return Type(p,a);
            }
            string n=getId();
            pass(":");
            Val v=expr();
            a[n]=v;
            while(match(",")){
                pass();
                n=getId();
                pass(":");
                v=expr();
                a[n]=v;
            }
            pass("{");
            return Type(p,a);
        }
        if(nextId()=="length"){
            getId();
            return factor().length();
        }
        if(nextId()=="ord"){
            getId();
            return int(factor());
        }
        if(nextId()=="chr"){
            getId();
            return char(factor());
        }
        if(match("getChar!")){
            pass("getChar!");
            getId();
            return char(getchar());
        }
        if(match("getInt!")){
            pass("getInt!");
            int a;
            cin>>a;
            return a;
        }
        if(match("throw!")){
            pass("throw!");
            throw;
        }
        if(matchId("throw")){
            getId();
            throw expr();
        }
        if(match("isNone?")){
            pass("isNone?");
            return bool(factor().Nv);
        }
        if(match("isInt?")){
            pass("isInt?");
            return bool(factor().Iv);
        }
        if(match("isList?")){
            pass("isList?");
            return bool(factor().Lv);
        }
        if(match("isFunc?")){
            pass("isFunc?");
            return bool(factor().Fv);
        }
        if(match("isType?")){
            pass("isType?");
            return bool(factor().Tv);
        }
        if(match("isObject?")){
            pass("isObject?");
            return bool(factor().Ov);
        }
        if(match("isChar?")){
            pass("isChar?");
            return bool(factor().Cv);
        }
        if(matchId("print")){
            pass("print"),cout<<expr();
            return NoneType();
        }
        if(matchId("new")){
            pass("new");
            Val tp=*scope->find(getId());
            if(match("(")){
                vector<Val> args;
                pass();
                if(match(")")) pass();
                else{
                    args.push_back(expr());
                    while(match(",")) pass(),args.push_back(expr());
                    pass(")");
                }
                return tp._new(args);
            }
            return tp._new();
        }
        if(matchId("None")){
            pass("None");
            return NoneType();
        }
        if(nextId()=="func"){
            getId();
            pass("(");
            if(match(")")){
                pass();
                return fh(Func(vector<string>(),new Scope(),getBlock())).second;
            }
            Scope*p=new Scope();
            string name=getId();
            Val value=SC(NoInitValue);
            if(match("=")) pass(),value=expr();
            p->var.insert(make_pair(name,value));
            vector<string> wp;
            wp.push_back(name);
            while(match(",")){
                pass();
                name=getId();
                value=SC(NoInitValue);
                if(match("=")) pass(),value=expr();
                p->var.insert(make_pair(name,value));
                wp.push_back(name);
            }
            pass(")");
            return fh(Func(wp,p,getBlock())).second;
        }
        if(isidf(code[0])){
            string n=getId();
            pair<Val,Val> res=fh(*(scope->find(n)));
            if(hasThis) hasThis=0,*scope->find(n)=res.first;
            return res.second;
        }
        if(match("!")){pass();return !factor();}
        if(match("~")){pass();return ~factor();}
        if(match("+")){pass();return +factor();}
        if(match("-")){pass();return -factor();}
    }
    pair<Val,Val> fh(Val v){
        if(match("[")){
            pass();
            Val i=expr();
            pass("]");
            return fh(*v[i]);
        }
        if(match("(")){
            pass();
            vector<Val> args;
            if(match(")")) pass();
            else{
                args.push_back(expr());
                while(match(",")) pass(),args.push_back(expr());
                pass(")");
            }
            return fh(callFunc(v,args));
        }
        if(match(".")){
            pass();
            string n=getId();
            Val a=*v.get(n);
            if(a.Fv){
                a.Fv->scope->var["this"]=v;
                if(!match("(")) raise("Error:Member function must be called.");
                pass();
                vector<Val> args;
                if(match(")")) pass();
                else{
                    args.push_back(expr());
                    while(match(",")) pass(),args.push_back(expr());
                    pass(")");
                }
                v=callFunc(a,args,"this");
                Val res=callFunc(a,args);
                hasThis=1;
                return make_pair(v,fh(res).second);
            }
            auto res=fh(a);
            return make_pair(v,res.second);
        }
        return make_pair(v,v);
    }
    Val callFunc(Val w,vector<Val> args,string ret=""){
        if(!w.Fv) throw;
        Func f=*w.Fv;
        map<string,Val> m;
        int cnt=0;
        for(pair<string,Val> i:f.scope->var) cnt+=bool(i.second.SCv);
        for(int i=0,pos=0;i<f.params.size();i++){
            if(f.scope->var[f.params[i]].SCv) m[f.params[i]]=args[pos++];
            else if(args.size()-cnt>=(i-pos?i-pos:1)) m[f.params[i]]=args[pos++];
            else m[f.params[i]]=f.scope->var[f.params[i]];
        }
        Scope*ns=new Scope(scope);
        ns->var.insert(m.begin(),m.end());
        ns->var.insert(f.scope->var.begin(),f.scope->var.end());
        if(ret.size()){
            Runner(f.code,ns).stmts();
            return *ns->find(ret);
        }
        return Runner(f.code,ns).stmts();
    }
    #undef F
};
#undef H
bool test(string s){
    int l=0,r=0,inString=0;
    for(char i:s){
        if(i=='"'&&!inString) inString=1;
        else if(i=='"'&&inString) inString=0;
        else if(i=='{'&&!inString) l++;
        else if(i=='}'&&!inString){
            r++;
            if(l&&r) l--,r--;
        }
    }
    return l==r&&!l&&!inString;
}
void REPL(){
    Scope*MainScope=new Scope();
    while(1){
        cout<<">>>";
        string a;
        getline(cin,a);
        if(a=="exit") return;
        while(!test(a)){
            a+="\n";
            cout<<"...";
            string b;
            getline(cin,b);
            a+=b;
        }
        Val f=Runner(a,MainScope).stmt();
        cout<<"\n<- "<<f<<endl;
    }
}
Val Val::_new(vector<Val> args){
    if(!Tv) throw;
    Val f=*get("__constructor__");
    f.Fv->scope->var["this"]=_new();
    return Runner("").callFunc(f,args,"this");
}
Val Val::callFunc(Val w,vector<Val> args){
    return Runner("").callFunc(w,args);
}
int main(){
    //Runner(" \t\nIt is a program.").program();
    //Runner("[1,2,3][1]").program();
    /*Runner("\
    var puts=func(str){\
        for i=0 to length str{\
            print str[i];\
        }\
        return 0;\
    };\
    puts(\"Hello,world!\");\
    ").stmts();*/
    cout<<"这是我用C++做的一种自创语言的交互式解释器，名字还没想好，欢迎大家提出建议\n\
bug有很多，只不过我没有发现，也欢迎大家提出\n\
由于设计的问题，这个可能会占内存过多崩了\n\
正在更新\n";
    REPL();
}
/*
for i=0 to 10 skip 2{print i;}

if(0){print 1;}else if(1){print 2;}else{print 3;}

var f=func(){\
    print 1;\
    return 1;\
};\
print f();

var puts=func(str){\
    for i=0 to length str{\
        print str[i];\
    }\
    return 0;\
};\
puts("Hello,world!");

for i=0 to length'[1,2,3]'{\
    print "[1,2,3]"[i];\
}

script{
    var prime=func(a){
        if(a<2){
            return 0;
        }
        for i=2 to a{
            if(a%i==0){
                return 0;
            }
        }
        return 1;
    };
    var main=func(){
        print prime(11);
    };
}

script{
    var puts=func(s){
        for i=0 to length s{
            print s[i];
        }
        return None;
    };
    var main=func(){
        puts("Hello,world!");
    };
}

var T=type{
    a:10
};
var a=new T;
print a.a;
a.a=20;
print a.a;

var T1=type{
    a:10
};
var T2=type:T1{
    a=20
};
print (new T2).a;

var T1=type{
    a:10
};
var T2=type:T1{
    b:20
};
print (new T2).a;
print (new T2).b;

script{
    var T1=type{
        a:10,
        c:20
    };
    var T2=type:T1{
        a:0,
        b:10
    };
    var main=func(){
        var a=new T2;
        print a.a;
        print a.b;
        print a.c;
    };
}

var f=func(a=1){print a;};
f();

var f=func(a=1,b){print b;};
f(1);

script{
    var T=type{
        a:10,
        f:func(a){
            this.a=a;
        }
    };
    var main=func(){
        var a=new T;
        print a.a;
        a.f(20);
        print a.a;
    };
}

var T=type{a:10};
var a=new T;

script{
    var Str=type{
        l:"",
        __listAttr__:"l"
    };
    var main=func(){
        var a=new Str;
        a.l="123";
        print a[2];
    };
}

script{
    var T=type{
        a:10,
        __constructor__:func(a){
            this.a=a;
        }
    };
    var main=func(){
        var a=new T(20);
        print a.a;
    };
}

script{
    var T=type{
        a:10,
        __constructor__:func(a){
            this.a=a;
        },
        changeA:func(a){
            this.a=a;
        }
    };
    var main=func(){
        var a=new T(20);
        print a.a;
        a.changeA(30);
        print a.a;
    };
}

script{
    var puts=func(s){
        for i=0 to length s{
            print s[i];
        }
        return None;
    };
    var T=type{
        a:10,
        __constructor__:func(_a){
            this.a=_a;
        },
        _print:func(){
            puts("T object:a=");
            print this.a;
            return None;
        },
        operatorSub:func(this,_b){
            puts("call T.operatorSub");
            return new T(this.a-_b.a);
        }
    };
    var main=func(){
        (new T(20)-new T(10))._print();
    };
}
*/