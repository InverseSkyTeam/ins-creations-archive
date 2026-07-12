#include <bits/stdc++.h>
#define sta stack<int>
using namespace std;
vector<string> split(string s){
    s+=" ";
    vector<string> ans;
    string ls;
    for(char i:s){
        if(i==' '||i=='\n'||i=='\t'||i==','){
            if(ls!="") ans.push_back(ls),ls="";
        }
        else ls+=i;
    }
    return ans;
}
enum{
    lbl,
    psh,phv,pop,ppv,
    pti,ptc,ptv,rds,rdi,rdc,
    var,
    add,sub,mul,dvi,mod,
    eq,ne,gt,lt,ge,le,
    lsh,rsh,
    lan,lor,ban,bor,bxr,
    lnt,bnt,
    ept,
    jmp,
    jif,jeq,jne,jgt,jlt,jge,jle,
    lft,rgt
};
struct exeRunner{
    sta st;
    int heap[65536],heapPos=0;
    map<int,pair<int,int> > varTable;
    vector<int> code;
    map<int,int> label;
    int pos=0;
    exeRunner(){}
    exeRunner(string s){
        vector<string> w=split(s);
        for(string i:w){
            code.push_back(stoi(i));
        }
    }
    exeRunner(vector<int> c):code(c){}
    void run(){
        for(int i=0;i<code.size();i++){
            if(code[i]==lbl) i++,label[code[i]]=i;
        }
        for(;pos<code.size();pos++){
            int i=code[pos];
            if(i==lbl) pos++;
            else if(i==psh) st.push(code[++pos]);
            else if(i==phv) st.push(heap[varTable[code[++pos]].first]);
            else if(i==pop) st.pop();
            else if(i==ppv) heap[varTable[code[++pos]].first]=st.top(),st.pop();
            else if(i==pti) cout<<st.top();
            else if(i==ptc) cout<<(char)st.top();
            else if(i==ptv) cout<<heap[varTable[code[++pos]].first];
            else if(i==rds){
                pos++;
                string s;
                cin>>s;
                for(int i=0;i<s.size();i--) st.push((int)s[i]);
                varTable[code[pos]]=make_pair(heapPos,heapPos+s.size());
                heapPos+=s.size();
            }
            else if(i==rdi){
                int s;
                cin>>s;
                st.push(s);
            }
            else if(i==rdc) st.push(getchar());
            else if(i==var){
                varTable[code[pos+1]]=make_pair(heapPos,heapPos+code[pos+2]);
                heapPos+=code[pos+2];
                pos+=2;
            }
            #define F(op) {int r=st.top();st.pop();int l=st.top();st.pop();st.push(l op r);}
            else if(i==add)F(+)
            else if(i==sub)F(-)
            else if(i==mul)F(*)
            else if(i==dvi)F(/)
            else if(i==mod)F(%)
            else if(i==eq)F(==)
            else if(i==ne)F(!=)
            else if(i==gt)F(>)
            else if(i==lt)F(<)
            else if(i==ge)F(>=)
            else if(i==le)F(<=)
            else if(i==lsh)F(<<)
            else if(i==rsh)F(>>)
            else if(i==lan)F(&&)
            else if(i==lor)F(||)
            else if(i==ban)F(&)
            else if(i==bor)F(|)
            else if(i==bxr)F(^)
            #undef F
            else if(i==lnt){int r=st.top();st.pop();st.push(!r);}
            else if(i==bnt){int r=st.top();st.pop();st.push(~r);}
            else if(i==ept) st.push(st.size()==0);
            else if(i==jmp) pos=label[code[pos+1]];
            #define F(op) {int r=st.top();st.pop();int l=st.top();st.pop();if(l op r) pos=label[code[pos+1]];else pos++;st.pop();}
            else if(i==jif){
                if(st.top()) pos=label[code[pos+1]];
                else pos++;
                st.pop();
            }
            else if(i==jeq)F(==)
            else if(i==jne)F(!=)
            else if(i==jgt)F(>)
            else if(i==jlt)F(<)
            else if(i==jge)F(>=)
            else if(i==jle)F(<=)
            #undef F
            else if(i==lft){
                varTable[code[pos+1]].first-=st.top();
                pos+=1;
            }
            else if(i==rgt){
                varTable[code[pos+1]].first+=st.top();
                pos+=1;
            }
        }
    }
};
struct asmCompiler{
    string s;
    int p=100;
    map<string,int> code;
    asmCompiler(){}
    asmCompiler(string _s):s(_s){}
    int getCode(string s){
        if(code[s]>=100) return code[s];
        return code[s]=++p;
    }
    exeRunner compile(){
        vector<int> res;
        vector<string> c=split(s);
        #define f res.push_back
        for(int x=0;x<c.size();x++){
            string i=c[x];
            if(i=="label") f(lbl),f(getCode(c[++x]));
            else if(i=="push") f(psh),f(stoi(c[++x]));
            else if(i=="pushv") f(phv),f(getCode(c[++x]));
            else if(i=="pop") f(pop);
            else if(i=="popv") f(ppv),f(getCode(c[++x]));
            else if(i=="puti") f(pti);
            else if(i=="putchar") f(ptc);
            else if(i=="putv") f(ptv),f(getCode(c[++x]));
            else if(i=="readstr") f(rds);
            else if(i=="readint") f(rdi);
            else if(i=="readchar") f(rdc);
            else if(i=="var") f(var),f(getCode(c[++x])),f(stoi(c[++x]));
            else if(i=="add") f(add);
            else if(i=="sub") f(sub);
            else if(i=="mul") f(mul);
            else if(i=="div") f(dvi);
            else if(i=="mod") f(mod);
            else if(i=="eq") f(eq);
            else if(i=="ne") f(ne);
            else if(i=="gt") f(gt);
            else if(i=="lt") f(lt);
            else if(i=="ge") f(ge);
            else if(i=="le") f(le);
            else if(i=="lshift") f(lsh);
            else if(i=="rshift") f(rsh);
            else if(i=="l_and") f(lan);
            else if(i=="l_or") f(lor);
            else if(i=="b_and") f(ban);
            else if(i=="b_or") f(bor);
            else if(i=="xor") f(bxr);
            else if(i=="l_not") f(lnt);
            else if(i=="b_not") f(bnt);
            else if(i=="empty") f(ept);
            else if(i=="jmp") f(jmp),f(getCode(c[++x]));
            else if(i=="jif") f(jif),f(getCode(c[++x]));
            else if(i=="jeq") f(jeq),f(getCode(c[++x]));
            else if(i=="jne") f(jne),f(getCode(c[++x]));
            else if(i=="jgt") f(jgt),f(getCode(c[++x]));
            else if(i=="jlt") f(jlt),f(getCode(c[++x]));
            else if(i=="jge") f(jge),f(getCode(c[++x]));
            else if(i=="jle") f(jle),f(getCode(c[++x]));
            else if(i=="left") f(lft),f(getCode(c[++x]));
            else if(i=="right") f(rgt),f(getCode(c[++x]));
        }
        return exeRunner(res);
        #undef f
    }
};
struct Calculator{
    string s;
    Calculator(){}
    Calculator(string _s):s(_s){}
    int calculate(){
        return expr();
    }
    #define pre while(s[0]==' '||s[0]=='\t'||s[0]=='\n') s.erase(s.begin());
    int expr(){
        pre;
        int res=term();
        pre;
        while(s[0]=='+'||s[0]=='-'){
            char op=s[0];
            s.erase(s.begin());
            if(op=='+') res+=term();
            else res-=term();
            pre;
        }
        return res;
    }
    int term(){
        pre;
        int res=factor();
        pre;
        while(s[0]=='*'||s[0]=='/'||s[0]=='%'){
            char op=s[0];
            s.erase(s.begin());
            if(op=='*') res*=factor();
            else if(op=='/') res/=factor();
            else res%=factor();
            pre;
        }
        return res;
    }
    int factor(){
        pre;
        if(s[0]=='('){
            s.erase(s.begin());
            int res=expr();
            s.erase(s.begin());
            return res;
        }
        if(s[0]=='-'){
            s.erase(s.begin());
            return -factor();
        }
        if(s[0]=='+'){
            s.erase(s.begin());
            return +factor();
        }
        string w;
        while(isdigit(s[0])) w+=s[0],s.erase(s.begin());
        return stoi(w);
    }
    #undef pre
};
map<string,string> op_to_string{
    {"+","add"},
    {"-","sub"},
    {"*","mul"},
    {"/","div"},
    {"%","mod"},
    {"==","eq"},
    {"!=","ne"},
    {">","gt"},
    {"<","lt"},
    {">=","ge"},
    {"<=","le"},
    {"<<","lshift"},
    {">>","rshift"},
    {"&&","lan"},
    {"||","lor"},
    {"&","ban"},
    {"|","bor"},
    {"^","bxr"},
};
struct easylCompiler{
    int ifAndWhileCode=0;
    string s;
    easylCompiler(){}
    easylCompiler(string _s):s(_s){}
    exeRunner compile(){
        return asmCompiler(stmts()).compile();
    }
    #define pre while(s[0]==' '||s[0]=='\t'||s[0]=='\n') s.erase(s.begin());
    void pass(int n){s.erase(s.begin(),s.begin()+n);}
    string peek(int n){pre;return s.substr(0,n);}
    string nextId(){pre;string r,_s=s;while(isalnum(s[0])||s[0]=='_') r+=s[0],pass(1);s=_s;return r;}
    string getId(){string r=nextId();pass(r.size());return r;}
    string getInt(){pre;string r;while(isdigit(s[0])) r+=s[0],pass(1);return r;}
    bool match(string w){pre;return w==peek(w.size());}
    string stmts(){
        string res;
        while(s.size()&&peek(3)!="end"&&peek(4)!="else"&&peek(4)!="elif"){
            res+=stmt();
            pre;
        }
        return res;
    }
    string stmt(){
        pre;
        if(peek(6)=="jumpif") return _jumpif();
        if(peek(4)=="jump") return _jump();
        if(peek(3)=="var") return _var();
        if(peek(3)=="set") return _set();
        if(peek(4)=="puts") return _puts();
        if(peek(4)=="puti") return _puti();
        if(peek(4)=="putc") return _putc();
        if(peek(5)=="label") return _label();
        if(peek(4)=="left") return _left();
        if(peek(5)=="right") return _right();
        if(peek(2)=="if") return _if();
        if(peek(5)=="while") return _while();
        if(peek(3)=="asm") return _asm();
        throw "Unknown statement name.";
    }
    string _jumpif(){
        pass(6);
        string res=expr()+"jif "+getId()+" ";
        return res;
    }
    string _jump(){
        pass(4);
        return "jmp "+getId()+" ";
    }
    string _var(){
        pass(3);
        return "var "+getId()+" "+getInt()+" ";
    }
    string _set(){
        pass(3);
        string id=getId();
        return expr()+"popv "+id+" ";
    }
    string _puts(){
        pass(4);
        while(s[0]!='[') pass(1);
        pass(1);
        string w,res;
        while(s[0]!=']') w+=s[0],pass(1);
        for(char i:w) res+="push "+to_string((int)i)+" putchar pop ";
        pass(1);
        return res;
    }
    string _puti(){
        pass(4);
        return expr()+"puti pop ";
    }
    string _putc(){
        pass(4);
        return expr()+"putchar pop ";
    }
    string _label(){
        pass(5);
        return "label "+getId()+" ";
    }
    string _left(){
        pass(4);
        string s=getId();
        return expr()+"left "+s+" "+"pop ";
    }
    string _right(){
        pass(5);
        string s=getId();
        return expr()+"right "+s+" "+"pop ";
    }
    string _if(){
        pass(2);
        /*int _code=ifAndWhileCode;
        string res=expr()+"l_not jif iflabel"+to_string(ifAndWhileCode)+" ";
        ifAndWhileCode++;
        res+=stmts()+"jmp endif"+to_string(_code)+" "+"label iflabel"+to_string(ifAndWhileCode-1)+" ";
        while(peek(4)=="elif"){
            pass(4);
            res+=expr()+"l_not jif iflabel"+to_string(ifAndWhileCode)+" ";
            ifAndWhileCode++;
            res+=stmts()+"jmp endif"+to_string(_code)+" "+"label iflabel"+to_string(ifAndWhileCode-1)+" ";
        }
        if(peek(4)=="else"){
            pass(4);
            res+=stmts()+"label iflabel"+to_string(ifAndWhileCode)+" label endif"+to_string(_code)+" ";
            res+="label endif"+to_string(_code)+" ";
        }
        else res+="label endif"+to_string(_code)+" ";
        ++ifAndWhileCode;*/
        //easylCompiler之精髓
        /*
        代码生成方案
        
        if ...
            ...
        elif ...
            ...
        else
            ...
        end
        
        ... l_not jif elif0_0
            ...
        jmp endif0
        label elif0_0
        ... l_not jif elif0_1
            ...
        jmp endif0
        label elif0_1
            ...
        label endif0
        */
        vector<string> blocks,conds;
        conds.push_back(expr());
        blocks.push_back(stmts());
        while(peek(4)=="elif"){
            pass(4);
            conds.push_back(expr());
            blocks.push_back(stmts());
        }
        if(peek(4)=="else"){
            pass(4);
            blocks.push_back(stmts());
        }
        else blocks.push_back("");
        pass(3);
        string res;
        int ic=ifAndWhileCode;
        for(int i=0;i<conds.size();i++){
            res+=conds[i];
            res+="l_not jif elif"+to_string(ic)+"_"+to_string(i)+" ";
            res+=blocks[i];
            res+="jmp endif"+to_string(ic)+" ";
            res+="label elif"+to_string(ic)+"_"+to_string(i)+" ";
        }
        res+=*(blocks.end()-1);
        res+="label endif"+to_string(ic)+" ";
        ifAndWhileCode++;
        return res;
    }
    string _while(){
        pass(5);
        string _expr=expr(),_res=stmts();
        string res=
            "label whilelabel"+to_string(ifAndWhileCode)+" "+
            _expr+
            "l_not jif whilelabel"+to_string(ifAndWhileCode+1)+" ";
        ++ifAndWhileCode;
        res+=
            _res+
            "jmp whilelabel"+to_string(ifAndWhileCode-1)+" "+
            "label whilelabel"+to_string(ifAndWhileCode)+" ";
        ++ifAndWhileCode;
        pass(3);
        cout<<res;
        return res;
    }
    string _asm(){
        pass(3);
        while(s[0]!='[') pass(1);
        pass(1);
        string w;
        while(s[0]!=']') w+=s[0],pass(1);
        pass(1);
        return w+" ";
    }
    #define F(f,w) if(match(#f)) pass(string(#f).size()),v=v+w()+op_to_string[#f]+" ";
    string expr(){
        string v=expr0();
        while(match("||")||match("&&")){F(||,expr0)F(&&,expr0)}
        return v;
    }
    string expr0(){
        string v=expr1();
        while(match("==")||match("!=")||match(">=")||
            match("<=")||match(">")||match("<")){
            F(==,expr1)F(!=,expr1)F(>=,expr1)
            F(<=,expr1)F(>,expr1)F(<,expr1)}
        return v;
    }
    string expr1(){
        string v=expr2();
        while(match("|")||match("&")||match("^")){F(|,expr2)F(&,expr2)F(^,expr2)}
        return v;
    }
    string expr2(){
        string v=expr3();
        while(match("+")||match("-")){F(+,expr3)F(-,expr3)}
        return v;
    }
    string expr3(){
        string v=factor();
        while(match("*")||match("/")||match("%")){F(*,factor)F(/,factor)F(%,factor)}
        return v;
    }
    string factor(){
        if(match("(")){
            pass(1);
            string res=expr();
            pass(1);
            return res;
        }
        else if(isdigit(s[0])) return "push "+getInt()+" ";
        else if(isalpha(s[0])||s[0]=='_') return "pushv "+getId()+" ";
        throw;
    }
    #undef F
    #undef pre
};
void lower(string &a){
    for(int i=0;i<a.size();i++) if('A'<=a[i]&&'Z'>=a[i]) a[i]=a[i]-'A'+'a';
}
map<string,bool> form;
map<string,string> fileType,file;
int main()
{
    form["txt"]=form["ci"]=form["exe"]=form["asm"]=form["easyl"]=1;
    cout<<"这次更新包括改变和新增两部分"<<endl;
    cout<<"改变："<<endl;
    cout<<"exe、asm、easyl里的变量全部定义在堆里而不是栈里"<<endl;
    cout<<"避免了变量的值被栈中的值覆盖"<<endl;
    cout<<"变量声明只接受两个参数（名称和大小）"<<endl;
    cout<<"新增："<<endl;
    cout<<"easyl新增if（已支持else和elif）、while（暂不支持break和continue）"<<endl;
    cout<<"Flat OS 0.0.2\n\"exit\" to close.\n";
    while(1){
        string name;
        cout<<">";
        cin>>name;
        lower(name);
        if(name=="exit") break;
        else if(name=="newform"){
            string fn;
            cin>>fn;
            form[fn]=1;
        }
        else if(name=="newfile"){
            string fn,nm;
            cin>>fn>>nm;
            fileType[nm]=fn,file[nm]="";
        }
        else if(name=="cls") system("clear");
        else if(name=="files") for(pair<string,string> i:fileType) cout<<i.first<<"("<<i.second<<")\n";
        else if(name=="write"){
            string nm;
            cin>>nm;
            getchar();
            int i=0;
            if(file.find(nm)==file.end()) cout<<"Can't find file\""<<nm<<"\".\n";
            else{
                file[nm]="";
                cout<<"\"EOF\" to stop.\n";
                while(++i){
                    printf("%3d | ",i);
                    string s;
                    getline(cin,s);
                    if(s=="EOF") break;
                    file[nm]+=s+"\n";
                }
            }
        }
        else if(name=="append"){
            string nm;
            cin>>nm;
            getchar();
            int i=0;
            if(file.find(nm)==file.end()) cout<<"Can't find file\""<<nm<<"\".\n";
            else{
                cout<<"\"EOF\" to stop.\n";
                while(++i){
                    printf("%3d | ",i);
                    string s;
                    getline(cin,s);
                    if(s=="EOF") break;
                    file[nm]+=s+"\n";
                }
            }
        }
        else if(name=="content"){
            string nm;
            cin>>nm;
            if(file.find(nm)==file.end()) cout<<"Can't find file\""<<nm<<"\".\n";
            else cout<<file[nm];
        }
        else if(name=="echo"){
            char i=getchar();
            string s,t;
            while(i!='[') i=getchar();
            i=getchar();
            while(i!=']') s+=i,i=getchar();
            getline(cin,t);
            cout<<s<<endl;
        }
        else if(name=="runexe"){
            string nm;
            cin>>nm;
            if(fileType[nm]!="exe") cout<<"Command \"runexe\" must run a exe,not a "<<fileType[nm];
            exeRunner(file[nm]).run();
            cout<<endl;
        }
        else if(name=="runasm"){
            string nm;
            cin>>nm;
            if(fileType[nm]!="asm") cout<<"Command \"runasm\" must run a asm,not a "<<fileType[nm];
            asmCompiler(file[nm]).compile().run();
            cout<<endl;
        }
        else if(name=="runeasyl"){
            string nm;
            cin>>nm;
            if(fileType[nm]!="easyl") cout<<"Command \"runeasyl\" must run a easyl,not a "<<fileType[nm];
            easylCompiler(file[nm]).compile().run();
            cout<<endl;
        }
        else if(name=="calculator"){
            getchar();
            cout<<"\"EOF\" to close.\n";
            while(1){
                cout<<"calculator>";
                string s;
                getline(cin,s);
                if(s=="EOF") break;
                try{
                    cout<<s<<"="<<Calculator(s).calculate()<<endl;
                }catch(invalid_argument){
                    cout<<"Can't calculate your input \""<<s<<"\"\n";
                }
            }
        }
        else if(name=="help"){
            cout<<"Flat OS是一个扁平的模拟操作系统"<<endl;
            cout<<"允许创建文件，但不允许创建文件夹"<<endl;
            cout<<"\n以下是目前有用的全部文件格式"<<endl;
            cout<<"txt：文本文件"<<endl;
            cout<<"exe：可执行文件（显然跟电脑自带的不一样）"<<endl;
            cout<<"asm：汇编（显然跟电脑自带的汇编不一样）"<<endl;
            cout<<"easyl：极其简单的编译性语言，会编译成可执行文件（当然是指这里的）后运行（编译得到的文件不会保存）"<<endl;
            cout<<""<<endl;
            cout<<"以下是目前的全部指令"<<endl;
            cout<<"help获取帮助"<<endl;
            cout<<"newform [格式名]创建新的文件格式（没啥用）"<<endl;
            cout<<"newfile [格式名] [文件名]创建新文件"<<endl;
            cout<<"cls清屏"<<endl;
            cout<<"files展示全部文件及其类型"<<endl;
            cout<<"write [文件名]写入文件（会覆盖原内容）"<<endl;
            cout<<"append [文件名]写入文件（不会覆盖原内容）"<<endl;
            cout<<"content [文件名]展示文件内容"<<endl;
            cout<<"echo[内容]打印内容到屏幕上（内容的左右要有方括号）"<<endl;
            cout<<"runexe [文件名]运行可执行文件"<<endl;
            cout<<"runasm [文件名]先把汇编转成可执行文件，然后运行"<<endl;
            cout<<"runeasyl [文件名]先把easyl文件转成可执行文件，然后运行"<<endl;
            cout<<"calculator打开计算器"<<endl;
            cout<<"exit退出"<<endl;
            cout<<"\neasyl代码示例："<<endl;
            cout<<"puts[Hello!]"<<endl;
            cout<<"会被转成下面的汇编代码："<<endl;
            cout<<"push 72 putchar pop push 101 putchar pop push 108 putchar pop push 108 putcharpop push 111 putchar pop push 33 putchar pop"<<endl;
            cout<<"再转成这样的可执行文件："<<endl;
            cout<<"1,72,6,3,1,101,6,3,1,108,6,3,1,108,6,3,1,111,6,3,1,33,6,3,"<<endl;
        }
        else cout<<"Unknown command \""<<name<<"\"\n";
    }
    return 0;
}
/*
newfile easyl f
write f
var isbreak 1
var i 1
set i 0
set isbreak 0
while isbreak==0
    puts[inloop]
    puti i
    puts[ ]
    puti isbreak
    if i>10
        puts[hhh;;;;;;;;;;;;]
        set isbreak 1
    end
    set i i+1
    putc 10
end
EOF
runeasyl f
*/