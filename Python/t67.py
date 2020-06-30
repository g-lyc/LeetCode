# -*- conding:utf-8 -*-
#Author:lyc
import os, sys

# 题目：
# 给你两个二进制字符串，返回它们的和（用二进制表示）。
# 输入为 非空 字符串且只包含数字 1 和 0。
#
# 示例 1:
# 输入: a = "11", b = "1"
# 输出: "100"
#
# 示例 2:
# 输入: a = "1010", b = "1011"
# 输出: "10101"
#
# 提示：
# 每个字符串仅由字符 '0' 或 '1' 组成。
# 1 <= a.length, b.length <= 10^4
# 字符串如果不是 "0" ，就都不含前导零。

class Solution:
    def addBinary(self, a: str, b: str) -> str:

        a,b = a[::-1],b[::-1]
        short,large = b,a if len(a) > len(b) else a,b
        result = []
        r = 0
        for i in range(len(short)):
            if a[i] + b[i] + r == 2:
                result.append(0)
                r = 1
            else:
                result.append(a[i] + b[i] + r)
                r = 0

        for i in range(len(short),len(large))

result = Solution()
a = "1010"
b = "1011"
print(result.addBinary(a,b))


