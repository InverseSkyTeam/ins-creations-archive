#include <iostream>
#include <string>
#include <cmath>
using namespace std;
string reverse(string a);
int turnint(string a){
    int ans=0;
    a=reverse(a);
    for(int i=0;i<a.size();i++){
        if(a[i]<='9'&&a[i]>='0') ans+=(a[i]-'0')*pow(10,i);
        else return 0;
    }
    return ans;
}
string turnstr(int a){
    string ans="";
    while(a){
        ans+=char(a%10+'0');
        a/=10;
    }
    return reverse(ans);
}
string reverse(string a){
    for(int i=0;i<a.size()/2;i++) swap(a[i],a[a.size()-i-1]);
    return a;
}
int getint(string b=""){
    int a;
    cout<<b;
    cin>>a;
    return a;
}
string getstr(string b=""){
    string a;
    cout<<b;
    getline(cin,a);
    return a;
}
string getstr2(string b=""){
    string a;
    cout<<b;
    cin>>a;
    return a;
}
int main()
{
    cout<<"请分两行输入两个数\n"<<turnint(getstr("请输入第一个数："))+turnint(getstr("请输入第二个数："))<<endl<<"输入类型是string，不信看代码";
    return 0;
}