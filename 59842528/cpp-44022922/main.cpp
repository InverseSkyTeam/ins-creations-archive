#include <ctime>
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string convert(string s, int numRows) {
        vector<string> ans(numRows + 1,"");
        int i = 0;
        while(i < s.size()){
            for(int j = 1;j <= numRows && i < s.size(); j++, i++)
                ans[j] += s[i];
                
            for(int j = numRows - 1; j >= 2 && i < s.size(); j--, i++)
                ans[j] += s[i];
        }
        string answer = "";
        for(int i = 1;i < ans.size(); i++)
            answer += ans[i];
            
        return answer;
    }
};

int main()
{
    
    srand(time(0));
    Solution S = Solution();
    cout << S.convert("Stay Foolish Stay hungry", rand() % 4 + 2) << endl << endl;
    cout << S.convert("Actually, there is no road on the ground, and with more people walking, it becomes a road", rand() % 25 + 2);
    return 0;
}