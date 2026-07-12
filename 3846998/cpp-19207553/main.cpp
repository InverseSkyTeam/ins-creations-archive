#include <iostream>
using namespace std;
int prime(int a){
    int b=1;
    if(a==1||a==0) return 0;
    for(int i=2;i<a;i++){
        if(a%i==0&&a/i!=1){
            b=0;
            return b;
        }
    }
    return b;
}
int main()
{
    int a;
    cout<<"请输入要判断是不是质数的数";
    cin>>a;
    cout<<prime(a);
}