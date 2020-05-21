# -*- conding:utf-8 -*-
#Author:lyc
import os, sys

# 题目：
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
#
# 示例:
# 输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# 说明:
# 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。

# 递归解法
class Solution:
    def letterCombinations(self, digits: str) -> [str]:

        str_dic = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        result = []
        if not digits:
            return []
        for i in str_dic[digits[0]]:
            if len(digits) == 1:
                result.append(i)
                if i == str_dic[digits[0]][-1]:
                    return result
            else:
                for j in self.letterCombinations(digits[1:]):
                    result.append(i+j)
                    if i == str_dic[digits[0]][-1] and j == self.letterCombinations(digits[1:])[-1]:
                        return result


# 快速递归法
class Solution:
    def letterCombinations(self, digits: str) -> [str]:

        str_dic = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        result = []
        if not digits:
            return result
        elif len(digits) == 1:
            return list(str_dic[digits[0]])
        else:
            res = self.letterCombinations(digits[:-1])
            for i in res:
                for j in str_dic[digits[-1]]:
                    result.append(i+j)

        return result


result = Solution()
x = '234'
print(result.letterCombinations(x))



