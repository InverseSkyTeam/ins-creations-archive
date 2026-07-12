#include <iostream>
#include <stack>
#include <vector>
#include <cmath>
#include <string>
#include <map>
using namespace std;
stack<int> StackA;
int Main[100000];
int pos=50000,i=0;
vector<string> code;
map<string,vector<string> > func,module;
string reverse(string a){
    for(int i=0;i<a.size()/2;i++) swap(a[i],a[a.size()-i-1]);
    return a;
}
int turnint(string a){
    int ans=0;
    a=reverse(a);
    for(int i=0;i<a.size();i++){
        if(a[i]<='9'&&a[i]>='0') ans+=(a[i]-'0')*pow(10,i);
        else return 0;
    }
    return ans;
}
void run(){
    for(;i<code.size();i++){
        if(code[i]=="VALUE") StackA.push(turnint(code[++i]));
        else if(code[i]=="COPY") StackA.push(StackA.top());
        else if(code[i]=="OUTPUT") cout<<(int)StackA.top();
        else if(code[i]=="INPUT"){
            int a;
            cin>>a;
            StackA.push(a);
        }
        else if(code[i]=="PUTCHAR") cout<<(char)StackA.top();
        else if(code[i]=="GETCHAR") StackA.push(getchar());
        else if(code[i]=="OUTPUT-STR") cout<<code[++i];
        else if(code[i]=="LEFT") pos--;
        else if(code[i]=="RIGHT") pos++;
        else if(code[i]=="STORE") Main[pos]=StackA.top();
        else if(code[i]=="POP") StackA.pop();
        else if(code[i]=="PUSH") StackA.push(Main[pos]);
        else if(code[i]=="LABEL") i++;
        else if(code[i]=="GOTO"){
            string label=code[i+1];
            for(i=0;i<code.size();i++) if(code[i]=="LABEL"&&code[++i]==label) break;
        }
        else if(code[i]=="AND"){
            int ls=StackA.top();
            StackA.pop();
            int rs=StackA.top();
            StackA.pop();
            StackA.push(rs&ls);
        }
        else if(code[i]=="OR"){
            int ls=StackA.top();
            StackA.pop();
            int rs=StackA.top();
            StackA.pop();
            StackA.push(rs|ls);
        }
        else if(code[i]=="XOR"){
            int ls=StackA.top();
            StackA.pop();
            int rs=StackA.top();
            StackA.pop();
            StackA.push(rs^ls);
        }
        else if(code[i]=="NOT"){
            int ls=StackA.top();
            StackA.pop();
            StackA.push(!ls);
        }
        else if(code[i]=="ADD"){
            int ls=StackA.top();
            StackA.pop();
            int rs=StackA.top();
            StackA.pop();
            StackA.push(rs+ls);
        }
        else if(code[i]=="SUB"){
            int ls=StackA.top();
            StackA.pop();
            int rs=StackA.top();
            StackA.pop();
            StackA.push(rs-ls);
        }
        else if(code[i]=="MUL"){
            int ls=StackA.top();
            StackA.pop();
            int rs=StackA.top();
            StackA.pop();
            StackA.push(rs*ls);
        }
        else if(code[i]=="DIV"){
            int ls=StackA.top();
            StackA.pop();
            int rs=StackA.top();
            StackA.pop();
            StackA.push(rs/ls);
        }
        else if(code[i]=="MOD"){
            int ls=StackA.top();
            StackA.pop();
            int rs=StackA.top();
            StackA.pop();
            StackA.push(rs%ls);
        }
        else if(code[i]=="EQ"){
            int ls=StackA.top();
            StackA.pop();
            int rs=StackA.top();
            StackA.pop();
            StackA.push(rs==ls);
        }
        else if(code[i]=="NEQ"){
            int ls=StackA.top();
            StackA.pop();
            int rs=StackA.top();
            StackA.pop();
            StackA.push(rs!=ls);
        }
        else if(code[i]=="BIG"){
            int ls=StackA.top();
            StackA.pop();
            int rs=StackA.top();
            StackA.pop();
            StackA.push(rs>ls);
        }
        else if(code[i]=="SMALL"){
            int ls=StackA.top();
            StackA.pop();
            int rs=StackA.top();
            StackA.pop();
            StackA.push(rs<ls);
        }
        else if(code[i]=="BEQ"){
            int ls=StackA.top();
            StackA.pop();
            int rs=StackA.top();
            StackA.pop();
            StackA.push(rs>=ls);
        }
        else if(code[i]=="SEQ"){
            int ls=StackA.top();
            StackA.pop();
            int rs=StackA.top();
            StackA.pop();
            StackA.push(rs<=ls);
        }
        else if(code[i]=="FUNC"){
            vector<string> f;
            i++;
            string name=code[i];
            i++;
            int l=1,r=0;
            for(;;i++){
                if(code[i]=="IF"||code[i]=="WHILE"||code[i]=="FUNC") l++;
                if(code[i]=="END"){
                    r++;
                    if(l){
                        r--;
                        l--;
                    }
                }
                if(l==0&&r==0) break;
                f.push_back(code[i]);
            }
            func[name]=f;
            //cout<<"Your function \""+name+"\":";
            //for(string i:func[name]) cout<<i<<" ";
            //cout<<endl;
        }
        else if(code[i]=="IF"){
            if(StackA.top()){
                i++;
                run();
            }
            else{
                int l=1,r=0;
                for(;;i++){
                    if(code[i]=="IF"||code[i]=="WHILE"||code[i]=="FUNC") l++;
                    if(code[i]=="END"){
                        r++;
                        if(l){
                            r--;
                            l--;
                        }
                    }
                    if(l==0&&r==0) break;
                }
            }
            i++;
        }
        else if(code[i]=="WHILE"){
            int ls=i;
            i++;
            while(StackA.top()){
                run();
                i=ls+1;
            }
            int l=1,r=0;
            for(;;i++){
                if(code[i]=="IF"||code[i]=="WHILE"||code[i]=="FUNC") l++;
                if(code[i]=="END"){
                    r++;
                    if(l){
                        r--;
                        l--;
                    }
                }
                if(l==0&&r==0) break;
            }
            i++;
        }
        else if(code[i]=="END") return;
        else if(code[i]=="IMPORT"){
            //cout<<"Import module \""+code[i+1]+"\"\nModule \""+code[i+1]+"\":";
            //for(string i:module[code[i+1]]) cout<<i<<" ";
            //cout<<endl;
            i++;
            vector<string> lc=code;
            int li=i;
            i=0;
            code=module[code[li]];
            run();
            code=lc;
            i=li;
        }
        else{
            //cout<<"Using function \""+code[i]+"\""<<endl;
            vector<string> lc=code;
            int li=i;
            i=0;
            code=func[code[li]];
            run();
            code=lc;
            i=li;
        }
    }
}
vector<string> split(string a){
    a+=" ";
    vector<string> ans;
    string ls;
    for(char i:a){
        if(i==' '){
            if(ls!="") ans.push_back(ls);
            ls="";
        }
        ls+=i;
    }
    return ans;
}
int main()
{
    module["BOOL"]=split("FUNC BOOL NOT NOT END");
    cout<<"所有关键字：\nLEFT指针左移\nRIGHT指针右移\nVALUE数字入栈\nCOPY复制栈顶数字\nINPUT输入数字\nOUTPUT输出栈顶数字\nPUTCHAR\nGETCHAR\nOUTPUT-STR原样输出后面的内容\nSTORE把栈顶数字存入Array\nPUSH把Array指针位置的数字入栈\nPOP弹出\nADD弹出两个数，求它们的和\nSUB弹出两个数，求它们的差\nMUL弹出两个数，求它们的积\nDIV弹出两个数，求它们的商\nMOD弹出两个数，求它们的余数\nAND弹出两个数，进行按位与\nOR弹出两个数，进行按位或\nXOR弹出两个数，进行按位异或\nNOT弹出一个数，进行逻辑取反\nEQ即==\nNEQ即!=\nBIG即>\nSMALL即<\nBEQ即>=\nSEQ即<=\nFUNC定义操作\nWHILE即BrainF***中的[\nIF\nELSE\nEND即BrainF***中的]\nGOTO\nLABEL\nIMPORT倒库，有bug暂不能用\n注：FUNC关键字定义的不是真正的函数，只是一个操作，不能传参\n可以写代码了，EOF结束\n";
    while(1){
        string a;
        cin>>a;
        if(a=="EOF") break;
        if(a=="ELSE"){
            code.push_back("END");
            code.push_back("COPY");
            code.push_back("NOT");
            code.push_back("IF");
            code.push_back("POP");
            continue;
        }
        code.push_back(a);
    }
    cout<<"输入任意键运行：";
    getchar();getchar();
    cout<<"\033[1;33m代码运行开始\033[1;0m\n";
    run();
    getchar();
    cout<<"\n\033[1;33m代码运行结束\033[1;0m\n";
    return 0;
}
/*
Main:
    LEFT
    RIGHT
StackA:
    VALUE
    INPUT
    OUTPUT
    PUTCHAR
    GETCHAR
    OUTPUT-STR
    STORE
    PUSH
    POP
    ADD
    SUB
    MUL
    DIV
    MOD
    AND
    OR
    XOR
    EQ
    NEQ
    BIG
    SMALL
    BEQ
    SEQ
Code:
    WHILE
    IF
    END

INPUT OUTPUT EOF

INPUT INPUT ADD OUTPUT EOF

VALUE 127
WHILE
 OUTPUT
 VALUE 1
 SUB
END
EOF

VALUE 70
IF
 OUTPUT
END
EOF

VALUE 65
IF
 OUTPUT
 VALUE 66
 IF
  OUTPUT
 END
END
EOF

INPUT
STORE
PUSH
OUTPUT
POP
OUTPUT
EOF

VALUE 65
LABEL MAIN
OUTPUT
GOTO MAIN
EOF

GOTO MAIN
LABEL MAIN
VALUE 65
OUTPUT
POP
EOF

FUNC F
 OUTPUT
END
VALUE 65
F
EOF

FUNC F
 VALUE 100000
 OUTPUT
END
F
EOF

FUNC BOOL
 NOT NOT
END
VALUE 10
BOOL
OUTPUT
EOF

IMPORT BOOL
VALUE 10
BOOL
OUTPUT
EOF

VALUE 1
IF
 OUTPUT-STR True
ELSE
 OUTPUT-STR False
END
EOF
*/