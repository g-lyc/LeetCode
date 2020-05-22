# -*- conding:utf-8 -*-
#Author:lyc
import os, sys


# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
#
# 示例 1:
#
# 输入: 123
# 输出: 321
#  示例 2:
#
# 输入: -123
# 输出: -321
# 示例 3:
#
# 输入: 120
# 输出: 21
# 注意:
#
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

class Solution:
    def reverse(self, x: int) -> int:
        import math
        if x <= math.pow(-2,31) or x > math.pow(2,31)-1 or x==0:
            return 0

        if x < 0:
            x = str(-x)
            while x[-1] == '0':
                x = x[:-1]
            x = -int(x[::-1])

        else:
            x = str(x)
            while x[-1] == '0':
                x = x[:-1]
            x = int(x[::-1])

        if x <= math.pow(-2,31) or x > math.pow(2,31)-1 or x==0:
            return 0

        return x

result = Solution()
#x = -123
x = 1534236469
print(result.reverse(x))



