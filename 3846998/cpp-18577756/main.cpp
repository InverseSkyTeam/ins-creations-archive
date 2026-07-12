#include <iostream>
#include <string>
using namespace std;

int main()
{
    int a;
    string b;
    cout<<"大写转小写输入1，小写转大写输入2：";
    cin>>a;
    if(a==1){
        cout<<"请输入字符串：";
        cin>>b;
        for(int i=0;i<b.size();i++){
            if(b[i]<='Z' and b[i]>='A') b[i]=b[i]+32;
        }
    }
    else if(a==2){
        cout<<"请输入字符串：";
        cin>>b;
        for(int i=0;i<b.size();i++){
            if(b[i]<='z' and b[i]>='a') b[i]=b[i]-32;
        }
    }
    cout<<endl<<"结果是："<<b;
    return 0;
}