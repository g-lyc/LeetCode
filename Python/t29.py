# -*- conding:utf-8 -*-
#Author:lyc
import os, sys

# 题目：
# 给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
# 返回被除数 dividend 除以除数 divisor 得到的商。
# 整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2
#
# 示例 1:
# 输入: dividend = 10, divisor = 3
# 输出: 3
# 解释: 10/3 = truncate(3.33333..) = truncate(3) = 3

# 示例 2:
# 输入: dividend = 7, divisor = -3
# 输出: -2
# 解释: 7/-3 = truncate(-2.33333..) = -2
#
# 提示：
# 被除数和除数均为 32 位有符号整数。
# 除数不为 0。
# 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。



class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """
        采用位运算代替乘法，不断用被除数减去除数的左移位运算结果，直到位运算结果大于被除数，开始新一轮
        :param dividend:
        :param divisor:
        :return:
        """
        # 定义边界值
        MIN_INT = -(2**31)
        MAX_INT = (2**31)-1
        # 取绝对值，方便运算
        f,r = abs(dividend), abs(divisor)
        # 初始化结果值
        count = 0

        while f >= r:
            flag = 0
            tmp = r
            # 迭代被除数减去除数的位运算
            while f >= tmp:
                f -= tmp
                count += 1 << flag
                tmp <<= 1
                flag += 1

        # 判断异号及边界
        if dividend < 0 and divisor > 0:
            count = -count
            if count < MIN_INT:
                return MIN_INT
        if dividend > 0 and divisor < 0:
            count = -count
            if count < MIN_INT:
                return MIN_INT

        if count > MAX_INT:
            return MAX_INT

        return count



dividend = 234589788
divisor = 3
result = Solution()
print(result.divide(dividend, divisor))


