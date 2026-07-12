#include<bits/stdc++.h>
using namespace std;
string in(string s,string t){
	int c=t.length();
	if(c>s.size()){
		return "no";
	}
	else{
		for(int i=0;i<s.size();i++){
			if(s.substr(i,t.length())==t){
				return "yes";
			}
		}
	return "no";
	}
}
int main()
{
    string s,t;
    cin>>s>>t;
    cout<<in(s,t);
	return 0;
}