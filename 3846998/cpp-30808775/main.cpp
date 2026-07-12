#include <iostream>
#include <vector>
#include <string>
using namespace std;
string cut(string a,int begin,int end){
    return a.substr(begin,end-begin);
}
vector<string> split(string a,char cha=' '){
    a=" "+a+" ";
    vector<string> ans;
    int last=0;
    for(int i=0;i<a.length();i++){
        if(a[i]==cha){
            ans.push_back(cut(a,last,i));
            last=i+1;
        }
    }ans.erase(ans.begin());
    return ans;
}
int main()
{
    string a;
    getline(cin,a);
    vector<string> ans(split(a));
    for(auto i:ans) cout<<i+";";
    return 0;
}