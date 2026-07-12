#include <iostream>
using namespace std;

// string code="++++++++[>+++++++++<-]>.>>++++++++++[<++++++++++>-]<+.+++++++..+++.>>++++[<+++++++++++>-]<.------------.<<<+++[>+++++<-]>.>.+++.------.--------.>+. ";
char arr[1000]={0};
char *p = arr;
 
void run(string s)
{
    int pcode=0;
    while(pcode<s.length())
    {
        switch(s[pcode])
        {        
            case '>':
                p++;
                break;
            case '<':
                p--;
                break;
            case '+':
                *p = *p + 1;
                break;
            case '-':
                *p = *p - 1;
                break;
            case '.':
                cout<<char(*p);
                break;
            case ',':
                *p=getchar();
                break;
            case '[':
                {
                    int num=1, pend=pcode;
                    while(num)
                    {
                        pend++;
                        if(s[pend]=='[')num++;
                        if(s[pend]==']')num--;
                    }
                    string ss=s.substr(pcode+1,pend-pcode-1);
                    while(*p)run(ss);
                    pcode=pend;
                    break;
                }
            case ']':
                break;
        }
        pcode++;
    }
    
}
 
int main()
{
    string code;
    cin >> code;
    run(code);
    return 0;
}