#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
namespace BigInt{
    struct BigInt{
        int len,data[10000];
        BigInt(char number[10000]){
            len = strlen(number);
            for(int i=1;i<=len;i++){
                data[i] = number[len-i] - '0';
            }
        }
        BigInt(int number){
            for (len=1;number;len++){
                data[len] = number % 10;
                number /= 10;
            };
            len--;
        }
        void fix(int num){
            len = num;
            for(int i=1;i<len;i++){
                data[i+1] += data[i]/10;
                data[i] %= 10;
                if(data[i] < 0){
                    data[i] += 10;
                    data[i+1]--;
                };
            };
            while (!data[len] && len > 0){
                len--;
            };
        }
        int& operator[](int index){
            return data[index];
        }
    };
    // 高精小于高精
    bool operator<(BigInt left,BigInt right){
        if (left.len != right.len){
            return left.len < right.len;
        }else{
            for(int i=left.len;i;i--){
                if(left[i]!=right[i]){
                    return left[i] < right[i];
                }
            }
            return false;
        }
    }
    // 高精小于低精
    bool operator<(BigInt left,int right){
        BigInt res(right);
        return left<res;
    }
    // 高精大于高精
    bool operator>(BigInt left,BigInt right){
        return right<left;
    }
    // 高精大于低精
    bool operator>(BigInt left,int right){
        return right<left;
    }
    // 高精等于高精
    bool operator==(BigInt left,BigInt right){
        return (!(left>right) && !(left<right));
    }
    // 高精等于低精
    bool operator==(BigInt left,int right){
        return (!(left>right) && !(left<right));
    }
    // 高精大于等于高精
    bool operator>=(BigInt left,BigInt right){
        return (left>right||left==right);
    }
    // 高精大于等于低精
    bool operator>=(BigInt left,int right){
        return (left>right||left==right);
    }
    // 高精小于等于高精
    bool operator<=(BigInt left,BigInt right){
        return (left<right||left==right);
    }
    // 高精小于等于低精
    bool operator<=(BigInt left,int right){
        return (left<right||left==right);
    }
    // 高精不等于高精
    bool operator!=(BigInt left,BigInt right){
        return !(left==right);
    }
    // 高精不等于低精
    bool operator!=(BigInt left,int right){
        return !(left==right);
    }
    
    
    // 高精加高精
    BigInt operator+(BigInt left,BigInt right){
        BigInt result(0);
        int len = max(left.len,right.len);
        for (int i=1;i<=len;i++){
            result[i] = left[i] + right[i];
        };
        result.fix(len + 1);
        return result;
    };
    // 高精加低精
    BigInt operator+(BigInt left,int right){
        left[1] += right;
        left.fix(left.len+1);
        return left;
    };
    // 高精乘高精
    BigInt operator*(BigInt left,BigInt right){
        BigInt result(0);
        for(int i=1;i<=left.len;i++){
            for(int j=1;j<=right.len;j++){
                result.data[i+j-1] += left.data[i] * right.data[j];
            }
        }
        result.fix(left.len + right.len - 1);
        return result;
    };
    // 高精乘低精
    BigInt operator*(BigInt left,int right){
        BigInt result(0);
        for (int i=1;i<=left.len;i++){
            result[i] = left[i] * right;
        };
        result.fix(left.len + 10);
        return result;
    };
    // 高精减高精
    BigInt operator-(BigInt left,BigInt right){
        BigInt result(0);
        int len = max(left.len,right.len);
        for (int i=1;i<=len;i++){
            result[i] = left[i] - right[i];
        };
        result.fix(len + 1);
        return result;
    };
    // 高精减低精
    BigInt operator-(BigInt left,int right){
        left[1] -= right;
        left.fix(left.len + 1);
        return left;
    };
    // 高精除以高精
    BigInt operator/(BigInt left,BigInt right){
        BigInt result(0);
        while(left >= right){
            left = left - right;
            result = result + 1;
        };
        return result;

    };
    // 高精除以低精
    BigInt operator/(BigInt left,int right){
        int x = 0;
        BigInt result(0);
        for(int i = left.len;i>0;i--){
            result[i] = (x*10 + left[i]) / right;
            x = (x*10 + left[i]) % right;
        };
        result.fix(left.len);
        return result;
    };
    // 高精对高精取模
    BigInt operator%(BigInt left,BigInt right){
        int s = 0;
        while(left.len > right.len){
            right = right * 10;
            s++;
        };
        while(s >= 0){
            while(right <= left){
                left = left - right;
            };
            right = right / 10;
            s--;
        };
        left.fix(left.len);
        return left;
    };
    // 高精对低精取模
    BigInt operator%(BigInt left,int right){
        BigInt result = left / right;
        result = left - result*right;
        return result;
    };
    
    
    // cout输出
    ostream& operator<<(ostream& cout,BigInt number){
        if (!number.len){
            cout << 0;
        }else{
            for(int i=number.len;i>=1;i--){
                cout << number.data[i];
            }
        }
        return cout;
    }
}
int main()
{
    BigInt::BigInt a(10),b(3);
    cout << a/b;
    return 0;
}