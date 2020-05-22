# -*- conding:utf-8 -*-
#Author:lyc
import os, sys

# 题目：罗马数字转整数
# 穷举列表法
class Solution:
    def romanToInt(self, s: str) -> int:
        """
        遍历列表方式查找
        :param str:
        :return:
        """
        # 建立映射字典
        dic={'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}

        result_num = 0
        for i in range(len(s[:-1])):
            if dic[s[i]] < dic[s[i+1]]:
                result_num -= dic[s[i]]
            else:
                result_num += dic[s[i]]

        result_num += dic[s[-1]]

        if result_num > 3999 or result_num < 1:
            return 0

        return result_num


result = Solution()
x = "MCMXCIV"
print(result.romanToInt(x))


