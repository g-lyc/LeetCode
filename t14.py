# -*- conding:utf-8 -*-
#Author:lyc
import os, sys

# 题目：
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 如果不存在公共前缀，返回空字符串 ""。

# 示例 1:
# 输入: ["flower","flow","flight"]
# 输出: "fl"

# 示例 2:
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。

# 说明:
# 所有输入只包含小写字母 a-z 。



class Solution:
    def longestCommonPrefix(self, strs: str) -> str:
        """
        遍历每一个列表元素取出对应的下标元素去重处理
        :param strs:
        :return:
        """

        if len(strs) == 0:
            return ""

        min_s = len(min(strs))

        result = ""

        for i in range(min_s):
            i_list = []
            for j in strs:
                i_list.append(j[i])
            if len(set(i_list)) == 1:
                result += i_list[0]
            else:
                break
        return result


result = Solution()
#x = ["flower","flow","flight"]
x = []
print(result.longestCommonPrefix(x))






