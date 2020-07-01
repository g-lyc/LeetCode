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

        # 补齐短的字符串
        while len(a) > len(b):
            b = '0'+b
        while len(b) > len(a):
            a = '0'+a

        result = [0]*len(a)
        r = 0

        # 反向遍历
        for i in range(len(a)-1,-1,-1):
            sum = int(a[i])+int(b[i])+r
            if sum >= 2:
                r = 1
                result[i] = sum - 2
            else:
                r = 0
                result[i] = sum

        result = ''.join([str(i) for i in result])

        return '1'+result if r != 0 else result

result = Solution()
a = "1111"
b = "1111"
print(result.addBinary(a,b))


