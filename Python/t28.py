# -*- conding:utf-8 -*-
#Author:lyc
import os, sys

# 题目：
# 实现 strStr() 函数。
# 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串
# 出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
#
# 示例 1:
# 输入: haystack = "hello", needle = "ll"
# 输出: 2

# 示例 2:
# 输入: haystack = "aaaaa", needle = "bba"
# 输出: -1

# 说明:
# 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
# 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # 如果输入匹配字符为空直接返回
        if not needle:return 0

        # 设置结果标志
        result = -1
        # 当匹配字符长度大于查询的字符时直接返回
        if len(haystack) < len(needle): return result

        # 遍历查询的字符串，遍历长度需要减去匹配的字符串长度再加1
        for i in range(len(haystack)-len(needle)+1):
            # 首个字符相同时开始遍历匹配字符串
            if haystack[i] == needle[0]:
                flag = True
                for j in range(len(needle)):
                    # 一旦出现不相同的字符更改flag状态并退出本次循环，退出是关键
                    if needle[j] != haystack[i+j]:
                        flag = False
                        break
                if flag:
                    return i

        return result


result = Solution()
haystack = "a"
needle = "a"
print(result.strStr(haystack, needle))
