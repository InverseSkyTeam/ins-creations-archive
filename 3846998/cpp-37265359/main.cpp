#include <bits/stdc++.h>
using namespace std;
struct EVM{//Easyl Virtual Machine
    struct Array{
        int level,start,move;
        vector<int> num;
        Array(){}
        Array(int l,int s,vector<int> n):level(l),start(s),num(n){
            move=1;
            for(int i=1;i<num.size();i++) move*=num[i];
        }
        Array operator[](int n){
            Array a=*this;
            a.start+=move*n;
            a.level--;
            a.move/=a.num[0];
            a.num.erase(a.num.begin());
            return a;
        }
    };
    struct Val{
        int*v=0;
        Array*a=0;
        Val(){}
        Val(int _v):v(new int(_v)){}
        Val(Array v):a(new Array(v)){}
        #define F(op)\
        Val operator op(Val b){\
            if(v&&b.v) return *v op *b.v;\
            throw;\
        }
        F(+)F(-)F(*)F(/)F(%)
        F(==)F(!=)F(>)F(<)F(>=)F(<=)
        F(&&)F(||)
        F(<<)F(>>)
        F(&)F(|)F(^)
        #undef F
        Val operator!(){
            if(v) return !(*v);
            throw;
        }
        Val operator~(){
            if(v) return ~(*v);
            throw;
        }
        Val operator[](Val b){
            if(a&&b.v) return (*a)[*b.v];
            throw;
        }
    };
    struct Scope{
        map<string,Val> var;
        Scope*parent;
        Scope(Scope*p):parent(p){}
        Val&find(string name){
            if(var.find(name)!=var.end()) return var[name];
            if(parent) return parent->find(name);
            throw "Name \""+name+"\" is undefined.";
        }
    } *scope=new Scope(0);
    stack<Val> st;
    int gettop(){
        st.top();
        if(st.top().v) return *st.top().v;
        else if(st.top().a->level!=0) throw;
        return memory[st.top().a->start];
    }
    stack<int> callst;
    vector<string> code;
    map<int,int>
        begin_condmp,
        cond_nextmp,
        next_whilemp,
        while_endmp,
        end_beginmp;
    map<int,int>
        cond_ifmp,
        if_elsemp,
        else_endmp,
        end_condmp;
    stack<pair<int,bool> > ifst;
    stack<pair<int,pair<bool,bool> > >whilest;
    map<string,int> labelmp;
    int memory[65536],pc=0;
    stack<int> mp;
    EVM(){}
    EVM(vector<string> c,Scope*s=new Scope(0)):code(c),scope(s){}
    vector<string> split(string s){
        s+=" ";
        vector<string> ans;
        string ls;
        for(char i:s){
            if(i==' '||i=='\n'||i=='\t'){
                if(ls!="") ans.push_back(ls),ls="";
            }
            else ls+=i;
        }
        return ans;
    }
    bool inifflag=0;
    void getpair(){//放弃不递归的想法了。但并没有完全放弃
        for(;pc<code.size();pc++){
            auto a=split(code[pc])[0];
            if((inifflag==0&&a=="cond")||a=="if"||a=="else"||a=="end"||a=="next"||a=="while") return;
            if(a=="expr") getpair();
            if(split(code[pc])[0]=="cond"){
                inifflag=1;
                //cout<<"cond\n";
                const int w=pc;
                //printf("store_cond(%d)\n",pc);
                int &t=cond_ifmp[pc];
                pc++;
                getpair();
                inifflag=0;
                t=pc;
                //printf("store_if(%d)\n",pc);
                pc++;
                getpair();
                if_elsemp[t]=pc;
                int&_t=if_elsemp[t];
                //printf("store_else(%d)\n",pc);
                pc++;
                getpair();
                //printf("store_end(%d)\n",pc);
                else_endmp[if_elsemp[t]]=pc;
                end_condmp[pc]=t;
            }
            else if(split(code[pc])[0]=="begin"){
                inifflag=0;
                const int w=pc;
                int&t=begin_condmp[pc];
                pc++;
                getpair();
                t=pc;
                pc++;
                getpair();
                cond_nextmp[t]=pc;
                int&_t=cond_nextmp[t];
                pc++;
                getpair();
                next_whilemp[_t]=pc;
                int&__t=next_whilemp[_t];
                pc++;
                getpair();
                while_endmp[__t]=pc;
                end_beginmp[pc]=w;
            }
        }
    }
    vector<string> getpair(int &p){
        int l=1,r=0;
        p++;
        vector<string> res;
        while(p<code.size()){
            res.push_back(code[p]);
            if(code[p]=="expr") l++;
            if(code[p]=="end"){
                if(l) l--;
                else r++;
            }
            if(!l&&!r){
                res.pop_back();
                return res;
            }
            p++;
        }
        throw;
    }
    void run(int ismain=1){//不能递归！不能递归！（算了暂时放弃不递归的想法了）
        mp.push(0);
        int _pos=0;
        getpair();
        for(pc=ismain;pc<code.size();pc++){
            auto v=split(code[pc]);
            if(v[0]=="func") labelmp[v[1]]=pc;
        }
        if(ismain){
            callst.push(code.size()-1);
            string name=split(code[0])[1];
            _pos=labelmp[name]+1;
        }
        for(pc=/*labelmp[name]*/_pos;pc<code.size();pc++){
            string i=code[pc];
            if(i[0]=='#') continue;
            //printf("do %s\n",i.data());
            if(i.find("puts ")!=string::npos){
                cout<<i.data()+i.find("puts ")+5;
                continue;
            }
            vector<string> v=split(i);
            if(!v.size()) continue;
            if(isdigit(v[0][0])) v.erase(v.begin());
            //虚拟机主体
            if(v[0]=="ret") pc=callst.top(),callst.pop(),scope=scope->parent;
            else if(v[0]=="push") st.push(stoi(v[1]));
            else if(v[0]=="pop") st.pop();
            else if(v[0]=="puti"){
                if(st.top().v) cout<<*st.top().v;
                else if(st.top().a->level==0) cout<<(int)memory[st.top().a->start];
                else throw;
            }
            else if(v[0]=="putc"){
                if(st.top().v) cout<<char(*st.top().v);
                else if(st.top().a->level==0) cout<<(char)memory[st.top().a->start];
                else throw;
            }
            #define f(name,op) else if(v[0]==#name){int r=gettop();st.pop();int l=gettop();st.pop();st.push(l op r);}
            f(add,+)f(sub,-)f(mul,*)f(div,/)f(mod,%)
            f(eq,==)f(ne,!=)f(gt,>)f(lt,<)f(ge,>=)f(le,<=)
            f(l_and,&&)f(l_or,||)
            f(lshift,<<)f(rshift,>>)
            f(b_and,&)f(b_or,|)f(b_xor,^)
            #undef f
            else if(v[0]=="get"){
                Val r=st.top();
                st.pop();
                Val l=st.top();
                st.pop();
                st.push(l[r]);
            }
            else if(v[0]=="l_not"){Val r=st.top();st.pop();st.push(!r);}
            else if(v[0]=="b_not"){Val r=st.top();st.pop();st.push(~r);}
            else if(v[0]=="value") scope->var[v[1]]=Val(rand());
            else if(v[0]=="pushv"||v[0]=="pusharr") st.push(scope->find(v[1]));
            else if(v[0]=="popv") scope->find(v[1])=st.top(),st.pop();
            else if(v[0]=="readint"){
                int a;
                cin>>a;
                st.push(a);
            }
            else if(v[0]=="readchar") st.push(int(getchar()));
            else if(v[0]=="args"){
                pc++;
                scope=new Scope(scope);
                mp.push(mp.top());
                v=split(code[pc]);
                while(v[0]=="array"||v[0]=="value"){
                    pc++;
                    auto _v=getpair(pc);
                    pc++;
                    auto w=code;
                    int _pc=pc;
                    code=_v;
                    run(0);
                    code=w;
                    pc=_pc;
                    scope->var[v[1]]=st.top();
                    v=split(code[pc]);
                }
                pc=labelmp[v[1]];
            }
            else if(v[0]=="array"){
                int level=stoi(v[2]);
                vector<int> num;
                for(int i=3;i<v.size();i++) num.push_back(stoi(v[i]));
                scope->var[v[1]].a=new Array(level,mp.top(),num);
                mp.top()+=scope->var[v[1]].a->move*num[0];
            }
            else if(v[0]=="popaddr"){
                Val v=st.top();
                st.pop();
                Val addr=st.top();
                st.pop();
                if(addr.a->level!=0) throw;
                memory[addr.a->start]=*v.v;
            }
            else if(v[0]=="cond"){
                //printf("cond(%d,%d)\n",pc,cond_nextmp[pc]);
                //printf("cond(%d,%d)\n",pc,cond_ifmp[pc]);
                if(cond_nextmp.find(pc)==cond_nextmp.end()) ifst.push(make_pair(pc,0)),scope=new Scope(scope);//选择结构之开始
                else if(whilest.top().second.second==0) scope=new Scope(scope);
            }
            else if(v[0]=="if"){
                //printf("if(%d,%d)\n",pc,if_elsemp[pc]);
                ifst.top().second=gettop();
                if(!gettop()) pc=if_elsemp[pc]-1;
                st.pop();
            }
            else if(v[0]=="else"){
                //printf("else(%d,%d)\n",pc,else_endmp[pc]);
                if(ifst.top().second) pc=else_endmp[pc]-1;
            }
            else if(v[0]=="end"){
                scope=scope->parent;
                if(end_beginmp.find(pc)!=end_beginmp.end()) pc=cond_nextmp[begin_condmp[end_beginmp[pc]]],scope=new Scope(scope);
                else ifst.pop();
            }
            else if(v[0]=="begin"){
                //printf("begin(%d,%d)\n",pc,begin_condmp[pc]);
                whilest.push(make_pair(pc,make_pair(0,0)));
                scope=new Scope(scope);
            }
            else if(v[0]=="next"){
                //printf("next(%d,%d)\n",pc,next_whilemp[pc]);
                whilest.top().second.first=gettop();
                st.pop();
                if(whilest.top().second.second==0&&whilest.top().second.first) pc=next_whilemp[pc],whilest.top().second.second=1;
                else if(whilest.top().second.first) pc=next_whilemp[pc];
                else{
                    pc=while_endmp[next_whilemp[pc]];
                    scope=scope->parent->parent;
                    whilest.pop();
                }
                //pc=next_whilemp[pc]-1;
            }
            else if(v[0]=="while"){
                /*printf("while(%d,%d)\n",pc,while_endmp[pc]);
                whilest.top().second.first=gettop(),st.pop();
                if(whilest.top().second.first==0) scope=scope->parent->parent,pc=while_endmp[pc];*/
                /*whilest.top().second.first=gettop();
                st.pop();*/
                /*if(whilest.top().second.first) */pc=begin_condmp[end_beginmp[while_endmp[pc]]];
                /*else{
                    cout<<"jump to end\n";
                    pc=while_endmp[pc];
                    scope=scope->parent->parent;
                    whilest.pop();
                }*/
            }
        }
    }
};
int main()
{
    EVM(vector<string>{
        "start main",
        "func main",
            "puts 这个Easyl Bytecode程序由我编写，由Easyl Virtual Machine解释执行\n",
            "puts \nProgram start.\n",
            "begin",
                "#puts do begin\n",
                "value i",
                "push 0",
                "popv i",
            "cond",
                "#puts do cond\n",
                "push 10",
                "pushv i",
                "ne",
            "next",
                "#puts do next\n",
                "push 1",
                "pushv i",
                "add",
                "popv i",
            "while",
                "#puts do while\n",
                "pushv i",
                "puts i=",
                "puti",
                "pop",
                "puts \n",
            "end",
            "ret",
    }).run();
    cout<<"\nRunning successed.\n";
    return 0;
}
/*
"start main",
"func main",
    "ret"

"start main",
"func f",
    "pushv arg0",
    "puti",
    "pop",
    "ret",
"func main",
    "args",
        "value arg0",
        "expr",
            "push 10",
        "end",
    "call f",
    "ret"

"start main",
"func f",
    "puts Hello\n",
    "args",
    "call f",
    "ret",
"func main",
    "args",
    "call f",
    "ret"
    
"start main",
"func main",
    "array arr 1 100",
    "pusharr arr",
    "push 0",
    "get",
    "push 10",
    "popaddr",
    "pusharr arr",
    "push 0",
    "get",
    "puti",
    "ret"
    
"start main",
"func main",
    "cond",
        "push 0",
    "if",
        "puts 0==true\n",
    "else",
        "puts 0!=true\n",
    "end",
    "ret"
*/