#include <iostream>
using namespace std;
bool bin[2000000001]={};
int main()
{
    system("clear");
    cout<<"桶排序，支持20亿以内整数，自动去重（输出时需要一些时间，请耐心等待）\n";
    cout<<"请输入需要排序的数列长度：";
    int a;
    cin>>a;
    cout<<"请输入这个数列：";
    for(int i=0;i<a;i++){int ls;cin>>ls;bin[ls]=1;}
    cout<<"结果是：";
    for(int i=0;i<2000000001;i++) if(bin[i]) cout<<i<<' ';
    return 0;
}