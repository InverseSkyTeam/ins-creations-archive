#include<iostream>
using namespace std;

int main(){
    long long n,score=0;
    cin >> n;
    while (n!=1){
        score++;
        if (n%2==0) n /= 2;
        else n = n*3+1;
    }
    cout << score;
    return 0;
}