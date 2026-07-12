#include <iostream>
#include <iomanip>
using namespace std;

void safe_flush(FILE *fp)
{
int ch;
while( (ch = fgetc(fp)) != EOF && ch != '\n' );
}
int run()
{
    long double sum=1; 
    unsigned long int total;
    short su;
    cout<<"输入阶乘次数：";
    su=scanf("%ld",&total);
    if(su==1)
    {
        for(long i=1;i<=total;i++)
        {
            sum*=i;
        }
    }
    else
    {
        cout<<"键入的值无效"<<endl;
        return 1;
    }
    
    cout<<fixed<<sum<<endl;
    return 0;
}
int main()
{
    run();
    safe_flush(stdin);
    main();
    return 0;
}