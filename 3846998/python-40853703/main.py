'''
{
    var
        EOF=0,
        CONST="const",
        ADD="+",
        SUB="-",
        MUL="*",
        DIV="/",
        LPAREN="(",
        RPAREN=")"
    ;
    func stoi(s){
        var res=0;
        for(var i=0;i<len(s);i++){
            res=res*10;
            res=res+ord(s[i])-48;
        }
        return res;
    }
    func isdigit(ch){
        return ord(ch)<=ord("9")&&ord(ch)>=ord("0");
    }
    class Lexer
    cons(text){
        this.text=text;
    }
    {
        var text,p=0;
        func get(){
            if(this.p==len(this.text)) return EOF,;
            while(this.text[this.p]==" "||this.text[this.p]=="\n"||this.text[this.p]=="\t") this.p++;
            if(this.p==len(this.text)) return EOF,;
            if(isdigit(this.text[this.p])){
                var s="";
                while(this.p<len(this.text)){
                    if(!isdigit(this.text[this.p])) break;
                    s=s+this.text[this.p];
                    this.p++;
                }
                return CONST,stoi(s);
            }
            if(this.text[this.p]=="+"){
                this.p++;
                return ADD,;
            }
            if(this.text[this.p]=="-"){
                this.p++;
                return SUB,;
            }
            if(this.text[this.p]=="*"){
                this.p++;
                return MUL,;
            }
            if(this.text[this.p]=="/"){
                this.p++;
                return DIV,;
            }
            if(this.text[this.p]=="("){
                this.p++;
                return LPAREN,;
            }
            if(this.text[this.p]==")"){
                this.p++;
                return RPAREN,;
            }
        }
    }
    var
        Const="Const",
        Binary="Binary"
    ;
    class Parser
    cons(lexer){
        this.lexer=lexer;
        this.tk=this.lexer.get();
        //println(this.tk);
    }
    {
        var lexer,tk;
        func eat(ex=-1){
            if(ex==-1||this.tk[0]==ex){
                var _tk=this.tk;
                this.tk=this.lexer.get();
                //println(this.tk);
                return _tk;
            }
        }
        func expr(){
            //println(1);
            var res=this.term();
            while(this.tk[0]==ADD||this.tk[0]==SUB){
                var op=this.eat()[0];
                res=(Binary,op,res,this.expr());
            }
            return res;
        }
        func term(){
            //println(2);
            var res=this.factor();
            while(this.tk[0]==MUL||this.tk[0]==DIV){
                var op=this.eat()[0];
                res=(Binary,op,res,this.factor());
            }
            return res;
        }
        func factor(){
            //println(3);
            if(this.tk[0]==CONST) return (Const,eat()[1]);
            if(this.tk[0]==LPAREN){
                this.eat();
                var e=this.expr();
                this.eat(RPAREN);
                return e;
            }
            //println("!!!",this.tk);
        }
    }
    func run(tree){
        //println(__scope__);
        println("run ",tree);
        //var tp=tree[0];
        //println(tp);
        if(tree[0]==Const){
            println("Const ",tree[0],tree);
            return tree[1];
        }
        if(tree[0]==Binary){
            var op=tree[1];
            println("Binary ",tree[0],tree);
            var l=run(tree[2]),r=run(tree[3]);
            if(op==ADD) return l+r;
            if(op==SUB) return l-r;
            if(op==MUL) return l*r;
            if(op==DIV) return l/r;
            println("op!!! ",op);
        }
        println("tp!!! ",tp);
    }
    var tree=Parser(Lexer("1+1+1")).expr();
    println(tree);
    println(run(tree));
}

'''