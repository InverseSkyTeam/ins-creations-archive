#include<bits/stdc++.h>
bool panduan(int z){
    bool r = false;
    for(int i=2;i<=sqrt(z);i++){
        if(z%i == 0)
            r = true;
    }
    if(z == 1)
        r = false;
    return r;
}
int main() {
    for(int a=100;a<=999;a++){
        int i = a;
        if(panduan(i) == true&&panduan(i/100) == true&&panduan(i/10) == true){
            printf("%d\n",a);}
    }
    return 0;
}