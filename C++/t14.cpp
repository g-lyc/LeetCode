#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

/**
 *  leetcode第14题
 *  寻找vector中最短元素，遍历，每次按照下标构建一个vector去重看长度是否等于1
 *  Author:lyc
*/


class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {

        int strs_size = strs.size();

        // 空vector直接返回
        if(strs.size() == 0){
            return "";
        };

        // 创建结果字符串
        string result = "";

        // 寻找最短元素下标及长度
        int minPosition = max_element(strs.begin(),strs.end()) - strs.begin();
        int minLength = strs[minPosition].length();

        for(int i=0; i < minLength; i++){

            // 构建临时vector
            vector<char> v {};
            for(int j = 0; j < strs.size(); j++){
                v.push_back(strs[j][i]);
            }

            // 去重
            set<char> s(v.begin(), v.end());
            v.assign(s.begin(), s.end());

            // 判断去重之后是否长度为1
            if(v.size() == 1){
                result += v[0];
            }else{
                break;
            }
        }

        return result;

    }
};

int main()
{
    Solution model;

    vector<string> x {"flower","flow","flight"};

    string res = model.longestCommonPrefix(x);
    cout << res << endl;

    system("pause");
    return 0;
}



