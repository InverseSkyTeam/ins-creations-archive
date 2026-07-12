#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;

// 直呼其名，很礼貌。
struct integer {
    int len, a[100000];
    integer(int x){
        memset(a, 0, sizeof(a));
        for (len=1;x;len++){
            a[len] = x % 10;
            x /= 10;
        } len--;
    }
    int &operator[](int i){
        return a[i];
    }
    void up(int newlen){
        len = newlen;
        for (int i=1;i<=len;i++){
            a[i+1] += a[i] / 10;
            a[i] %= 10;
        }
        while (!a[len]) len--;
    }
    void output(){
        if (!len){
            cout << 0;
        } else {
            for (int i=len;i>=1;i--) cout << a[i];
        }
    }
};

// plus
integer operator+(integer a, integer b) {
    integer result(0);
    int len = max(a.len,b.len);
    for (int i=1;i<=len;i++) result[i] = a[i]+b[i];
    result.up(len+1);
    return result;
}

// mul
integer operator*(integer a, int b) {
    integer result(0);
    int len = a.len;
    for (int i=1;i<=len;i++) result[i] = a[i]*b;
    result.up(len+10);
    return result;
}

int n;

int main(){
    cin >> n;
    if (!n){
        cout << 0;
        return 0;
    }
    if (n > 1000){
        cout << "这么大的数据我怎么算";
        return 0;
    }
    // 正片开始
    integer total(0), fact(1);
    for (int i=1;i<=n;i++){
        fact = fact * i;
        total = total + fact;
    }
    total.output();
    return 0;
}