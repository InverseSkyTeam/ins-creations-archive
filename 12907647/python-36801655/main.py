print('''https://www.luogu.com.cn/problem/T259133
《由于你没有高斯聪明，所以你不被允许使用等差数列求和公式直接求出答案。》
《数据保证，1<=n<=100》
侮辱智商/doge

#include<iostream>
using namespace std;

int main(){
    int n,s;
    cin >> n;
    for (int i=1;i<=n;++i){
        s += i;
    }
    cout << s;
    return 0;
}
''')