#include<bits/stdc++.h>
bool panduan(int z){
    bool r = true;
    for(int i=2;i<=sqrt(z);i++){
        if(z%i == 0)
            r = false;
    }
    if(z == 1)
        r = false;
    return r;
}
int take_of_head(int num){
    int c = -1;
    int a = 0;
    int num1 = num;
    while(num > 0){
        a = num%10;
        num/=10;
        c+=1;
    }
    for(int i=0;i<c;i++){
        a*=10;
    }
    num = num1 - a;
    return num;
}
int main() {
    for(int a=1000;a<=3000;a++){
        bool flag = true;
        int i = a;
        if(panduan(i) == true){
        while(i>0){
            i = take_of_head(i);
            if(panduan(i) == false)
                flag = false;
        }
        if(flag == true)
            printf("%d\n",a);}
    }
    return 0;
}