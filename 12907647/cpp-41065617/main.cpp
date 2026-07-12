#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;

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

integer operator*(integer a, int b) {
    integer result(0);
    int len = a.len;
    for (int i=1;i<=len;i++) result[i] = a[i]*b;
    result.up(len+10);
    return result;
}

int t,n,c;

int main(){
    cin >> t;
    for (int i=1;i<=t;i++){
        int total = 0;
        cin >> n >> c;
        integer fact(1);
        for (int i=1;i<=n;i++) fact = fact * i;
        for (int i=1;i<=fact.len;i++){
            if (fact[i] == c) total++;
        }
        cout << total << endl;
    }
    return 0;
}