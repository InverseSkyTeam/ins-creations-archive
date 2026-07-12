#include<iostream>
using namespace std;

int main(){
    int k;
    double sum=0,times=1;
    cin >> k;
    while (sum<=k){
        sum += 1/times;
        times++;
    }
    cout << times-1;
    return 0;
}