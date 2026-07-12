#include <bits/stdc++.h>
using namespace std;
enum{
    INT,
};
enum{
    ADD,SUB,MUL,DIV,LPAREN,RPAREN,
    NUM,
    EXIT,
};
int int_binary(int op,int a,int b){
    switch(op){
        case ADD:return a+b;
        case SUB:return a-b;
        case MUL:return a*b;
        case DIV:return a/b;
    }
    throw;
}
class Val{
public:
    int tp;
    int iv;
    Val(){}
    Val(int a):iv(a),tp(INT){}
    Val binary(int op,Val b){
        if(tp==INT&&b.tp==INT) return int_binary(op,iv,b.iv);
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
        if(match("(")) return p++,Token(LPAREN);
        if(match(")")) return p++,Token(RPAREN);
        #undef match
        if(isdigit(text[p])){
            string s;
            s+=text[p++];
            while(isdigit(text[p])) s+=text[p++];
            return Token(NUM,s);
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
        AST*res=term();
        while(tk.tp==ADD||tk.tp==SUB){
            int op=eat().tp;
            res=new BinOp(op,res,term());
        }
        return res;
    }
    AST*term(){
        AST*res=factor();
        while(tk.tp==MUL||tk.tp==DIV){
            int op=eat().tp;
            res=new BinOp(op,res,factor());
        }
        return res;
    }
    AST*factor(){
        if(tk.tp==NUM){
            int res=stoi(eat().v);
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
    cout<<Parser(Lexer("(1+1)*2")).expr()->eval().iv;
    return 0;
}