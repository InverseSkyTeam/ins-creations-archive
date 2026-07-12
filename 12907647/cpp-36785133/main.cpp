#include<iostream>
using namespace std;

int main(){
    int L,is_prime,n=1,total=0,totalL=0;
    cin >> L;
    while (totalL+n<L){
        n++;
        is_prime = 1;
        for (int i=2;i<=n;i++){
            if (n%i==0 && i!=1 && i!=n){
                is_prime = 0;
                break;
            }
        }
        if (is_prime){
            totalL += n;
            total++;
            cout << n << endl;
        }
    }
    cout << total;
    return 0;
}