#include <bits/stdc++.h>
using namespace std;
enum{
    INT,FLOAT,
};
enum{
    ADD,SUB,MUL,DIV,MOD,
    EQ,NE,GT,LT,GE,LE,
    SHL,SHR,
    AND,OR,
    BAND,BOR,XOR,
    LPAREN,RPAREN,
    INUM,FNUM,
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
    throw;
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
    throw;
}
class Val{
public:
    int tp;
    int iv;
    float fv;
    Val(){}
    Val(int a):iv(a),tp(INT){}
    Val(float a):fv(a),tp(FLOAT){}
    Val binary(int op,Val b){
        Val a=*this;
        if(a.tp==INT&&b.tp==INT) return int_binary(op,a.iv,b.iv);
        if(a.tp==FLOAT&&b.tp==FLOAT) return float_binary(op,a.fv,b.fv);
        if(a.is_float()||b.is_float()) return float_binary(op,a.convert(FLOAT).fv,b.convert(FLOAT).fv);
        throw;
    }
    Val convert(int to){
        switch(tp){
            case INT:
            switch(to){
                case INT:return *this;
                case FLOAT:return Val(float(iv));
                default:throw;
            }
            case FLOAT:
            switch(to){
                case INT:return Val(int(fv));
                case FLOAT:return *this;
                default:throw;
            }
        }
        throw;
    }
    bool is_int(){
        return tp==INT;
    }
    bool is_float(){
        return tp==FLOAT;
    }
    string tostr(){
        switch(tp){
            case INT:return to_string(iv);
            case FLOAT:return to_string(fv);
        }
        throw;
    }
    Val unary(int op){
        throw;
    }
};
class AST{
public:
    virtual Val eval()=0;
};
class Const:public AST{
public:
    Val v;
    Const(Val a):v(a){}
    Val eval(){
        return v;
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
        if(match("(")) return p++,Token(LPAREN);
        if(match(")")) return p++,Token(RPAREN);
        #undef match
        if(isdigit(text[p])){
            string s;
            s+=text[p++];
            while(isdigit(text[p])||text[p]=='.') s+=text[p++];
            if(s.find(".")!=string::npos) return Token(FNUM,s);
            return Token(INUM,s);
        }
        throw;
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
        throw;
    }
    AST*expr(){
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
        if(tk.tp==INUM){
            int res=stoi(eat().v);
            return new Const(Val(res));
        }
        if(tk.tp==FNUM){
            float res=stof(eat().v);
            return new Const(Val(res));
        }
        if(tk.tp==LPAREN){
            eat();
            AST*v=expr();
            eat(RPAREN);
            return v;
        }
        throw;
    }
};
int main()
{
    cout<<Parser(Lexer("1.0==2.0-1.0")).expr()->eval().tostr();
    return 0;
}