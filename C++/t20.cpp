#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

/**
 *  leetcode第20题
 *  利用栈结构后进先出的特性依次比对字符
 *  Author:lyc
*/



class Solution {
public:
    bool isValid(string s) {

        // 定义结果布尔变量，如果输入字符串为空直接返回true
        bool result = true;
        if(s == ""){
            return result;
        };

        // 定义括号类型map
        map<char,char> str_dic = {
            {'(',')'},
            {'[',']'},
            {'{','}'},
            {'a','a'}
        };

        // 定义栈结构
        vector<char> stack = {'a'};

        for(auto i:s){
            if(i == ' ')
            {
                // 如果该字符为空直接跳过
                continue;
            }else if(str_dic.count(stack.back()) == 1 & i == str_dic[stack.back()])
            {
                // 如果与栈中第一个元素匹配成功，则删除栈中该元素
                stack.pop_back();
            }
            else
            {
                // 如果与栈中第一个元素不匹配，则将该元素添加至栈中
                stack.push_back(i);
            }
        };

        if(stack.size() != 1){
            result = false;
        };

        return result;
        
    };
};

int main()
{
    string x = "()[]{}"; 
    Solution result;
    bool res = result.isValid(x);

    cout << res << endl;
    system("pause");
}





