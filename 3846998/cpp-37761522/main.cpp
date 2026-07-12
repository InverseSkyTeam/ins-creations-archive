#include <iostream>
using namespace std;

int main()
{
    long long a;
    *((double*)(&a))=1.1;
    cout<<*(double*)&a;
    return 0;
}