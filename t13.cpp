#include <iostream>
#include <string>
#include <map>

using namespace std;

/**
 *  leetcode第13题
 *  定义map数据结构
 *  Author:lyc
*/

class Solution {
public:
    int romanToInt(string s) {

        // 定义map
        map<char, int> romadic={
            {'I',1},
            {'V',5},
            {'X',10},
            {'L',50},
            {'C',100},
            {'D', 500},
            {'M', 1000}
        };

        // 计算传入的字符串长度
        int num_of_s = s.length();

        // 定义存放结果的数值
        int result = 0;


        for(int i = 0;i < s.length()-1; i++){
            if(romadic[s[i]] < romadic[s[i+1]]){
                result -= romadic[s[i]];
            }else{
                result += romadic[s[i]];
            }
        }

        result += romadic[s[s.length()-1]];

        return result;
    }
};


int main()
{
    Solution roma2int;
    string a = "MCMXCIV";
    int res = roma2int.romanToInt(a);

    cout << res << endl;
    system("pause");
    return 0;
}