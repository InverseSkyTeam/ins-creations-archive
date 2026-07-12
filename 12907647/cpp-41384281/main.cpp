#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

int up,step,a[1005],b[1005],c[1005];
string A;

void r(int a[],int b[],int l) {
    for (int i=1;i<=l;i++) b[i] = a[l-i+1];
}

void plusn(int a[],int b[],int c[],int &l) {
    for (int i=1;i<=l;i++){
        c[i] += a[i] + b[i];
        c[i+1] += c[i] / up;
        c[i] %= up;
    }
    if (c[l+1]) l++;
    for (int i=1;i<=l;i++) a[i] = c[i], c[i] = 0;
}

bool issame(int a[],int b[],int l) {
    for (int i=1;i<=l;i++) {
        if (b[i]!=a[i]) return false;
    }
    return true;
}

int main(){
    cin >> up >> A;
    int l = A.length();
    for (int i=1;i<=l;i++){
        a[i] = A[i-1];
        if ('0'<=a[i]&&a[i]<='9') a[i] -= '0';
        else a[i] -= 'A'-10;
    }
    r(a,b,l);
    while (!issame(a,b,l)&&step<=30) {
        plusn(a,b,c,l);
        r(a,b,l);
        step++;
    }
    if (step<=30) cout << "STEP=" << step;
    else cout << "Impossible!";
    return 0;
}