#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int main()
{
    cout<<"本计算器支持加（+）、减（-）、乘（*或x）、取余（%）、次方计算（^）和整除（/,会保留整数）,且需要输入英文字符"<<endl;
    cout<<"请直接输入一个只有一个运算符号的算式：";
    int a,b;
    char c;
    cin>>a>>c>>b;
    if(c=='+') cout<<a+b;
	else if(c=='-') cout<<a-b;
	else if(c=='*') cout<<a*b;
	else if(c=='/') cout<<a/b;
	else if(c=='%') cout<<a%b;
	else if(c=='^') cout<<pow(a,b);
	else cout<<"输入错误";
    return 0;
}