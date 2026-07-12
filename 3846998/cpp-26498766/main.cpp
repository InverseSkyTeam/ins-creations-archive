#include <iostream>
using namespace std;
struct fs{
    int fz=0,fm=1;
    char fsx='/';
};
void fsout(fs a){
    cout<<a.fz<<a.fsx<<a.fm;
}
void fsin(fs &a){
    cin>>a.fz>>a.fsx>>a.fm;
}
void yf(fs &a){
    int b=a.fm,c=a.fz;
    for(int i=2;i<min(b,c);i++){
        while(a.fm%i==0&&a.fz%i==0){
            a.fm=a.fm/i;
            a.fz=a.fz/i;
        }
    }
}
void tf(fs &a,fs &b){
    yf(a);
    yf(b);
    int fm=a.fm*b.fm;
    int fz1=a.fz*b.fm;
    int fz2=b.fz*a.fm;
    a.fm=fm;
    a.fz=fz1;
    b.fm=fm;
    b.fz=fz2;
}
fs operator+(fs a,fs b){
    yf(a);
    yf(b);
    tf(a,b);
    fs c;
    c.fm=a.fm;
    c.fz=a.fz+b.fz;
    yf(c);
    return c;
}
fs operator-(fs a,fs b){
    yf(a);
    yf(b);
    tf(a,b);
    fs c;
    c.fm=a.fm;
    c.fz=a.fz-b.fz;
    yf(c);
    return c;
}
fs operator*(fs a,fs b){
    fs c;
    c.fm=a.fm*b.fm;
    c.fz=a.fz*b.fz;
    yf(c);
    return c;
}
fs operator/(fs a,fs b){
    fs c;
    c.fm=a.fm*b.fz;
    c.fz=a.fz*b.fm;
    yf(c);
    return c;
}
bool operator>(fs a,fs b){
    tf(a,b);
    return a.fz>b.fz;
}
bool operator<(fs a,fs b){
    tf(a,b);
    return a.fz<b.fz;
}
bool operator==(fs a,fs b){
    tf(a,b);
    return a.fz==b.fz;
}
bool operator>=(fs a,fs b){
    tf(a,b);
    return a.fz>=b.fz;
}
bool operator<=(fs a,fs b){
    tf(a,b);
    return a.fz<=b.fz;
}
fs build(int a_=0,int b=1){
    fs a;
    a.fz=a_;
    a.fm=b;
    return a;
}
fs fsget(){
    fs a;
    fsin(a);
    return a;
}
float turnfloat(fs a){
    return float(a.fz/a.fm);
}
int main()
{
    fs a=fsget(),b=fsget();
    fsout(a+b);
    cout<<endl<<turnfloat(a+b);
    return 0;
}