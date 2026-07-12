#include <iostream>
#include <string>
#include <cmath>
using namespace std;
string reverse(string a);
int turnint(string a){
    int ans=0;
    a=reverse(a);
    for(int i=0;i<a.size();i++){
        if(a[i]<='9'&&a[i]>='0') ans+=(a[i]-'0')*pow(10,i);
        else return 0;
    }
    return ans;
}
string turnstr(int a){
    if(a==0) return "0";
    string ans="",sign="";
    if(a<0){
        a=-a;
        sign="-";
    }
    while(a){
        ans+=char(a%10+'0');
        a/=10;
    }
    return sign+reverse(ans);
}
string reverse(string a){
    for(int i=0;i<a.size()/2;i++) swap(a[i],a[a.size()-i-1]);
    return a;
}
char xplus(char a,char b){
    return a-'0'+b;
}
char xsub(char a,char b){
    return a+'0'-b;
}
string r0(string a){
    while(a[0]=='0') a=a.substr(1,a.length()-1);
    return a;
}
class big{
    bool sign=0;
    string value="0";
    public:
    big(){};
    big abs(){
        big a=(*this);
        a.sign=0;
        return a;
    }
    big(int a){
        string x=turnstr(a);
        if(x[0]=='-'){
            sign=1;
            value=x.substr(1,x.length()-1);
        }else value=x;
    }
    big(string a){
        if(a[0]=='-'){
            sign=1;
            value=a.substr(1,a.length()-1);
        }
        else if(a[0]=='+') value=a.substr(1,a.length()-1);
        else value=a;
    }
    friend ostream&operator<<(ostream&cout,big a){
        if(a.sign) cout<<"-";
        cout<<a.value;
        return cout;
    }
    friend istream&operator>>(istream&cin,big&a){
        string x;
        cin>>x;
        if(x[0]=='-'){
            a.sign=1;
            a.value=x.substr(1,x.length()-1);
        }else if(x[0]=='+') a.value=x.substr(1,x.length()-1);
        else a.value=x;
        return cin;
    }
    bool operator==(big b){
        return sign==b.sign&&value==b.value;
    }
    bool operator!=(big b){
        return !((*this)==b);
    }
    bool operator>(big b){
        if(sign&&(!b.sign)) return 0;
        if((!sign)&&b.sign) return 1;
        if(value.size()>b.value.size()) return 1;
        if(value.size()<b.value.size()) return 0;
        if((*this)==b) return 0;
        string n=value,m=b.value;
        for(int i=0;i<n.size();i++){
            if(n[i]>m[i]) return 1;
            if(n[i]<m[i]) return 0;
        }
        return 0;
    }
    bool operator<(big b){
        return ((*this)!=b)&&(!((*this)>b));
    }
    bool operator<=(big b){
        return ((*this)==b)||((*this)<b);
    }
    bool operator>=(big b){
        return ((*this)==b)||((*this)>b);
    }
    big operator+(big b){
        if(value=="0"&&b.value=="0") return 0;
        if(sign==b.sign){
            string ans,xa=reverse(value),xb=reverse(b.value);
            bool j=0;
            while(1){
                if(xa.size()<xb.size()) xa+="0";
                else if(xa.size()>xb.size()) xb+="0";
                else break;
            }
            for(int i=0;i<xa.size();i++){
                char ls=xplus(xa[i],xb[i])+j;
                if(ls>'9'){
                    j=1;
                    ans+=ls-10;
                    //cout<<xa[i]<<";"<<xb[i]<<";"<<char(ls-10)<<";"<<j<<endl;
                }
                else{
                    j=0;
                    ans+=ls;
                    //cout<<xa[i]<<";"<<xb[i]<<";"<<ls<<";"<<j<<endl;
                }
            }
            if(sign){
                if(j) return r0("-1"+reverse(ans));
                return r0("-"+reverse(ans));
            }else{
                if(j) return r0("1"+reverse(ans));
                return r0(reverse(ans));
            }
        }
        if((!sign)&&b.sign){
            if(value==b.value) return 0;
            if((*this)>b.abs()){
                string ans,xa=reverse(value),xb=reverse(b.value);
                bool j=0;
                while(1){
                    if(xa.size()<xb.size()) xa+="0";
                    else if(xa.size()>xb.size()) xb+="0";
                    else break;
                }
                for(int i=0;i<xa.size();i++){
                    char ls=xsub(xa[i],xb[i])-j;
                    if(ls<'0'){
                        j=1;
                        ans+=ls+10;
                        //cout<<xa[i]<<";"<<xb[i]<<";"<<char(ls+10)<<";"<<j<<endl;
                    }else{
                        j=0;
                        ans+=ls;
                        //cout<<xa[i]<<";"<<xb[i]<<";"<<ls<<";"<<j<<endl;
                    }
                }
                return r0(reverse(ans));
            }
            else{
                string ans,xa=reverse(value),xb=reverse(b.value);
                bool j=0;
                while(1){
                    if(xa.size()<xb.size()) xa+="0";
                    else if(xa.size()>xb.size()) xb+="0";
                    else break;
                }
                for(int i=0;i<xa.size();i++){
                    char ls=xsub(xb[i],xa[i])-j;
                    if(ls<'0'){
                        j=1;
                        ans+=ls+10;
                        //cout<<xa[i]<<";"<<xb[i]<<";"<<ls<<";"<<j<<endl;
                    }else{
                        j=0;
                        ans+=ls;
                        //cout<<xa[i]<<";"<<xb[i]<<";"<<ls<<";"<<j<<endl;
                    }
                }
                return "-"+r0(reverse(ans));
            }
        }
        if(sign&&(!b.sign)){
            if(value==b.value) return 0;
            if(b>(*this).abs()){
                string ans,xa=reverse(b.value),xb=reverse(value);
                bool j=0;
                while(1){
                    if(xa.size()<xb.size()) xa+="0";
                    else if(xa.size()>xb.size()) xb+="0";
                    else break;
                }
                for(int i=0;i<xa.size();i++){
                    char ls=xsub(xa[i],xb[i])-j;
                    if(ls<'0'){
                        j=1;
                        ans+=ls+10;
                    }else{
                        j=0;
                        ans+=ls;
                        //cout<<xa[i]<<";"<<xb[i]<<";"<<ls<<";"<<j<<endl;
                    }
                }
                return r0(reverse(ans));
            }
            else{
                string ans,xa=reverse(b.value),xb=reverse(value);
                bool j=0;
                while(1){
                    if(xa.size()<xb.size()) xa+="0";
                    else if(xa.size()>xb.size()) xb+="0";
                    else break;
                }
                for(int i=0;i<xa.size();i++){
                    char ls=xsub(xb[i],xa[i])-j;
                    if(ls<'0'){
                        j=1;
                        ans+=ls+10;
                        //cout<<xa[i]<<";"<<xb[i]<<";"<<ls<<";"<<j<<endl;
                    }else{
                        j=0;
                        ans+=ls;
                        //cout<<xa[i]<<";"<<xb[i]<<";"<<ls<<";"<<j<<endl;
                    }
                }
                return "-"+r0(reverse(ans));
            }
        }
        return 0;
    }
    big operator-(big b){
        b.sign=!b.sign;
        return (*this)+b;
    }
    big operator*(big b){//非常临时的高精乘，速度超慢
        bool xsign=(sign!=b.sign);
        big xans(0);
        (*this)=abs(),b=b.abs();
        for(;b>0;b=b-1) xans=xans+(*this);
        xans.sign=xsign;
        return xans;
    }
    big operator/(big b){//非常临时的高精除，速度超慢
        bool xsign=(sign!=b.sign);
        big xans(0);
        (*this)=abs(),b=b.abs();
        while((*this)>=b){
            (*this)=(*this)-b;
            xans=xans+1;
        }
        xans.sign=xsign;
        return xans;
    }
    big operator%(big b){//非常临时的高精模，速度超慢
        bool xsign=sign;
        big t=(*this);
        t=t.abs(),b=b.abs();
        while(t>=b) t=t-b;
        t.sign=xsign;
        return t;
    }
};
int main()
{
    big a,b;
    cin>>a>>b;
    cout<<a%b;
    return 0;
}