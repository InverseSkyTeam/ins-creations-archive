#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;

#define ll long long

ll height,width,total,square;

int main() {
    cin >> height >> width;
    if (height>width) swap(width,height);
    total = (width+width*width)*(height+height*height)/4;
    //  (1+2+3+...+width)*(1+2+3+...+height)
    // =(1+width)*width/2*(1+height)*height/2
    // =(width+width^2)*(height+height^2)/4
    for (int i=width,j=height;j>=1;i--,j--) square += i*j;
    cout << square << " " << total-square;
    //  ((width-0)*(height-0))+((width-1)*(height-1))+((width-2)*(height-2))*...
    return 0;
}