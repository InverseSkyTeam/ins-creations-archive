#include<iostream>
#include<cstdio>
using namespace std;

int main(){
    int data[1000050],n,start,end,yes=0,no=0,maxyes=0,maxno=0,tmp=0,maxnum=0;
    cin >> n;
    for (int i=1;i<=n;i++)
        data[i] = 0;
    for (int i=1;i<=n;i++){
        cin >> start >> end;
        if (end>maxnum) maxnum=end;
        for (int j=start+1;j<=end;j++)
            data[j] = 1;
    }
    for (int i=1;i<=maxnum;i++)
        if (data[i] == 1){
            tmp = 0;
            yes++;
            if (no>0){
                if (no>maxno) maxno = no;
                no = 0;
            }
        }
        else {
            if (i==1 || tmp){
                tmp = 1;
                continue;
            }
            no++;
            if (yes>0){
                if (yes>maxyes) maxyes = yes;
                yes = 0;
            }
        }
    if (yes>maxyes) maxyes=yes;
    cout << maxyes << " " << maxno;
    return 0;
}