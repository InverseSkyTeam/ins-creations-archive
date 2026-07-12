#include <iostream>
using namespace std;
int pow(int a,int b){
    if(b==1) return a;
    return a*pow(a,b-1);
}
string reverse(string a){
    if(a.length()==1) return a;
    if(a.length()==0) return "";
    return a[a.length()-1]+reverse(a.substr(1,a.length()-2))+a[0];
}
int to_int(string a){
    if(a.length()==1) return a[0]-'0';
    return pow(10,a.length()-1)*(a[0]-'0')+to_int(a.substr(1,a.length()-1));
}
string to_str(int a){
    if(a==0) return "0";
    return reverse(char(a%10+'0')+reverse(to_string(a/10)));
}
int main()
{
    cout<<"看代码";
    return 0;
}