/*
这个作品的一部分是我在iPad上写的
*/
#include <bits/stdc++.h>
using namespace std;
struct File{
    map<string,File>*dir;
    string*text;
    File(){}
    File(string s){text=new string(s);}
    File(map<string,File> s){dir=new map<string,File>(s);}
} maindir;
File&get_route(string s,File f){
    int p=s.find("/");
    if(p==string::npos) return (*f.dir)[s];
    if(f.dir->find(s.substr(0,p))==f.dir->end()) throw;
    return get_route(s.substr(p+1),(*f.dir)[s.substr(0,p)]);
}
int main()
{
    maindir.dir=new map<string,File>;
    (*maindir.dir)["bin"]=map<string,File>();
    cout<<"FKJ-OS 0.0.1\nInput \"exit\" to close.\n";
    while(1){
        cout<<">>>";
        string op;
        cin>>op;
        if(op=="exit") break;
        if(op=="newfile"){
            string route;
            cin>>route;
            get_route(route,maindir).text=new string;
        }
        if(op=="newdir"){
            string route;
            cin>>route;
            get_route(route,maindir).dir=new map<string,File>;
        }
        if(op=="writefile"){
            string route;
            cin>>route;
            cout<<"EOF to close.\n";
            string s,tmp;
            while(1){
                cin>>tmp;
                if(tmp=="EOF") break;
                s+=tmp+"\n";
            }
            *get_route(route,maindir).text=string(s);
        }
        if(op=="print"){
            string route;
            cin>>route;
            cout<<route<<":\n"<<*get_route(route,maindir).text<<"\n";
        }
        if(op=="echo"){
            string s;
            getchar();
            getline(cin,s);
            cout<<s<<endl;
        }
        if(op=="help"){
            cout<<
            "以下是FKJ-OS 0.0.1的全部命令\n"
            "help 获取帮助\n"
            "exit 退出\n"
            "newfile [完整路径] 创建文件\n"
            "newdir [完整路径] 创建文件夹\n"
            "writefile [完整路径] 写入文件\n"
            "print [完整路径] 输出文件的内容\n"
            "echo [内容] 把内容原封不动输出一遍\n";
        }
    }
    return 0;
}