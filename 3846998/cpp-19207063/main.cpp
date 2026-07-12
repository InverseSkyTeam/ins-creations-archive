#include <bits/stdc++.h>
using namespace std;
int dcsl(int a1,int a2,int c){
    int ans,a;
    a=(a2-a1)/c+1;
    ans=(a1+a2)*a/2;
    return ans;
}
int main()
{
    int a1,a2,c;
    cout<<"首项：";
    cin>>a1;
    cout<<"末项：";
    cin>>a2;
    cout<<"公差：";
    cin>>c;
    cout<<"等差数列的总和是："<<dcsl(a1,a2,c);
    return 0;
}