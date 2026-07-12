#include <bits/stdc++.h>
using
    std::cin,
    std::cout,
    std::endl;
enum{
    left,right,up,down
};
char code[1000][1000]{
    "25*'!dlrow,olleH':v",
    "               v:,_@",
    "               >  ^"
};
int x=0,y=0;
#define ch (code[x][y])
int dir=right;
std::stack<int> s;
int pop(){
    if(s.empty()) return 0;
    int v=s.top();
    s.pop();
    return v;
}
int top(){
    if(s.empty()) return 0;
    return s.top();
}
void go(){
    switch(dir){
        case right:y++;break;
        case left:y--;break;
        case up:x--;break;
        case down:x++;break;
    }
}
void run(){
    for(;;go()){
        if(ch=='@') break;
        if(ch=='>') dir=right;
        if(ch=='<') dir=left;
        if(ch=='v') dir=down;
        if(ch=='^') dir=up;
        if(ch=='?') dir=rand()%4;
        if(ch=='_') dir=pop()==0?right:left;
        if(ch=='|') dir=pop()==0?down:up;
        #define f(op) if(ch==(#op)[0]){\
            int r=pop();\
            int l=pop();\
            s.push(l op r);\
        }
        f(+)f(-)f(*)f(/)f(%)
        #undef f
        if(ch=='!') top()==bool(top());
        if(ch=='`'){
            int r=pop(),l=pop();
            s.push(l>r);
        }
        if(ch==':') s.push(top());
        if(ch=='\\'){
            int l=pop(),r=pop();
            s.push(l);
            s.push(r);
        }
        if(ch=='$') pop();
        if(isdigit(ch)) s.push(ch-'0');
        if(ch=='.') cout<<pop();
        if(ch==',') cout<<(char)pop();
        if(ch=='&') s.push(0),cin>>s.top();
        if(ch=='~') s.push(getchar());
        if(ch=='"'||ch=='\''){
            go();
            while(ch!='"'&&ch!='\'') s.push(ch),go();
        }
        if(ch=='#') go();
        if(ch=='p'){
            int y=pop(),x=pop(),v=pop();
            code[x][y]=v;
        }
        if(ch=='g'){
            int y=pop(),x=pop();
            s.push(code[x][y]);
        }
    }
}
int main()
{
    srand(time(0));
    run();
    cout<<"\nEXIT\n";
    return 0;
}