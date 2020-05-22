#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>

using namespace std;

/**
 *  leetcode第17题
 *  递归
 *  Author:lyc
*/

// 解法一：递归
class Solution {
public:
    vector<string> letterCombinations(string digits) 
    {

        // 定义电话键盘对应map
        map<char,vector<string>> str_dic = {
                {'2',{"a","b","c"}},
                {'3',{"d","e","f"}},
                {'4',{"g","h","i"}},
                {'5',{"j","k","l"}},
                {'6',{"m","n","o"}},
                {'7',{"p","q","r","s"}},
                {'8',{"t","u","v"}},
                {'9',{"w","x","y","z"}}
        };
        
        // 声明结果vector
        vector<string> result;

        // 判断输入字符为空时直接返回空vector
        if(digits.size() < 1){
            return result;
        };

        // 输入字符串长度
        int digOflens = digits.size();

        for(auto s:str_dic[digits[0]])
        {
            // 当输入字符只有一个时，逐个添加至result并返回
            if(digits.size() == 1)
            {
                result.push_back(s);
                if(s == str_dic[digits[0]].back())
                {
                    return result;
                }
            }else{
                // 截取输入字符串并递归调用
                string tail = digits.substr(1,digits.size());
                for(auto n:letterCombinations(tail))
                {
                    result.push_back(s+n);
                    // 判断输入字符串到最后一位及对应的str_dic中也为最后一个时函数返回
                    if(s == str_dic[digits[0]].back() & n == letterCombinations(tail).back())
                    {
                        return result;
                    };
                };
            };
        };
        // 函数必须有返回值
        return result;
    };
};


// 解法二：快速递归
class Solution {
public:
    vector<string> letterCombinations(string digits) 
    {

        // 定义电话键盘对应map
        map<char,vector<string>> str_dic = {
                {'2',{"a","b","c"}},
                {'3',{"d","e","f"}},
                {'4',{"g","h","i"}},
                {'5',{"j","k","l"}},
                {'6',{"m","n","o"}},
                {'7',{"p","q","r","s"}},
                {'8',{"t","u","v"}},
                {'9',{"w","x","y","z"}}
        };
        
        // 声明结果vector
        vector<string> result;

        // 判断输入字符为空时直接返回空vector
        if(digits.size() < 1)
        {
            return result;
        }
        else if(digits.size() == 1)
        {
            return str_dic[digits[0]];
        }
        else
        {
            vector<string> res = letterCombinations(digits.substr(0,digits.size()-1));
            for(auto i:res)
            {
                for(auto j:str_dic[digits.back()])
                {
                    result.push_back(i+j);
                }
            }
        }
        return result;
    };
};




int main()
{
    Solution model;

    string x = "234";

    vector<string> res = model.letterCombinations(x);

    // 打印结果
    for(auto i:res){
        cout << i << ',';
    };
    cout << endl;

    system("pause");
    return 0;
}