#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

string A[10],B[10];
char tmp;
int a[10],b[10],c[10],indexa=1,indexb=1,type=0,len;
int go[8] = {0,2,3,5,7,11,13};

int to_int(string x){
    int total;
    if (x.length()==1) total = x[0]-'0';
    else total = (x[0]-'0')*10+(x[1]-'0');
    return total;
}

int main(){
    while (cin>>tmp){
        if (tmp == ','){
            if (type==0) indexa++;
            else indexb++;
            continue;
        }
        if (tmp == '+'){
            type = 1;
            continue;
        }
        if (type==0) A[indexa] += tmp;
        if (type==1) B[indexb] += tmp;
    }
    for (int i=1;i<=indexa;i++) a[i] = to_int(A[indexa+1-i]);
    for (int i=1;i<=indexb;i++) b[i] = to_int(B[indexb+1-i]);
    len = max(indexa,indexb);
    for (int i=1;i<=len;i++){
        c[i] += a[i]+b[i];
        c[i+1] += c[i] / go[i];
        c[i] %= go[i];
    }
    len++;
    while (!c[len]) len--;
    for (int i=len;i>=1;i--){
        cout << c[i];
        if (i!=1) cout << ",";
    }
    return 0;
}
