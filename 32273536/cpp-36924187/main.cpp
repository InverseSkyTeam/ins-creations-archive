//README--------必读-------------------
// 原本准备用python计算，结果发现速度太慢，于是转战c++
// 常量number指定运算次数，越大精度越高，可自行更改尝试，但是，number最好不要超过2147483646，以免for循环成为死循环
// 计算公式 pi/4=1-1/3+1/5-1/7+1/9.........
//为计算速度，已牺牲部分精度，故pi值不完全准确


#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;
double fl(long total)
{
    double res=1;
    for(long i = 0;i < total;i++)
        res *= 0.1;
    return res;
}
int main()
{
    double pi = 1, sum, s, t;
    long num;
    cout<<"输入计算精度(小数点后精确位数)，推荐为7：";
    scanf("%ld",&num);
    long double dem = fl(num+1);
    cout <<"\n-----------------必读-------------------------\n原本准备用python计算，结果发现速度太慢，于是转战c++\n计算公式 pi/4=1-1/3+1/5-1/7+1/9.........\n为计算速度，已牺牲部分精度，故pi值不完全准确\n(后台已在计算中，请稍候...)"<<endl;
    
    s = -1.0;
    t = 3.0;
    sum = s / t;
    pi += sum;
    
    while(fabs(sum)>dem)
    {
        
        s = -s;
        t += 2;
        sum = s / t;
        pi += sum;
        //cout << "s" << fixed << setprecision(2) << s << endl;
        //cout << "pi" << fixed << setprecision(5) << pi << endl;
        //cout << "sum" << fixed << setprecision(5) << sum << endl;
     }
    cout<<"\n\n\n";
    cout<<"pi=";
    cout << fixed << setprecision(num) << pi*4<< endl;
    return 0;

}
