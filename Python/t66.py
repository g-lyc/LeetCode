# -*- conding:utf-8 -*-
#Author:lyc
import os, sys

# 题目：
# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
#
# 示例 1:
# 输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
#
# 示例 2:
# 输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。

class Solution:
    def plusOne(self, digits: [int]) -> [int]:
        if digits[0] == 0:return [1]
        result = []
        r = 1
        for i in digits[::-1]:
            if i+r >= 10:
                result.append(i+r-10)
                r = 1 if i + r == 10 else i + r - 10

            else:
                result.append(i+r)
                r = 0
        if r != 0:
            result.append(r)
        return result[::-1]




result = Solution()
digits = [9]
print(result.plusOne(digits))




