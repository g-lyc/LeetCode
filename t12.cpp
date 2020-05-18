#include <iostream>
#include <string>

using namespace std;

/**
 *  leetcode第12题
 *  定义两个列表存储罗马字符和数字，遍历寻找
 *  Author:lyc
*/

class Solution {
public:
    string intToRoman(int num) {

        if(num > 3999 | num < 0){
            return 0;
        }

        // 定义数组
        string romastr[] {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        int nums[] {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};

        // 计算数组长度
        int num_of_array = sizeof(nums) / sizeof(int);

        // 定义存放结果的字符串
        string result = "";

        for(int i = 0;i < num_of_array; i++){
            while(num >= nums[i]){
                num -= nums[i];
                result += romastr[i];
            }
        }

        return result;
    }
};

int main()
{
    Solution s;
    int a = 1994;
    string res = s.intToRoman(a);
    cout << res << endl;
    system("pause");
    return 0;
}