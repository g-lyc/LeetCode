# -*- conding:utf-8 -*-
#Author:lyc
import os, sys

# 题目：
# 实现 int sqrt(int x) 函数。
# 计算并返回 x 的平方根，其中 x 是非负整数。
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
#
# 示例 1:
# 输入: 4
# 输出: 2
#
# 示例 2:
# 输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842...,
#      由于返回类型是整数，小数部分将被舍去。

class Solution:
    def mySqrt(self, x: int) -> int:
        """
        暴力解法
        :param x:
        :return:
        """
        if x == 0: return 0

        result = 0
        # 先每次平方增长
        for i in range(1,x+2):
            result = i*2
            if pow(result,2) > x:
                break

        # 一旦超过，每次减一迭代
        while pow(result,2) > x:
            result -= 1

        return result


class Solution:
    def mySqrt(self, x: int) -> int:
        """
        二分法
        :param x:
        :return:
        """
        l,r,res = 0,x,-1
        while l <= r:
            mid = (l+r) // 2
            if pow(mid,2) <= x:
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res


class Solution:
    def mySqrt(self, x: int) -> int:
        """
        牛顿迭代法
        :param x:
        :return:
        """
        if x == 0:return 0
        C, res = float(x),float(x)
        while True:
            tmp = 0.5*(res + C/res)
            if res - tmp < 0.00000001:
                break
            res = tmp
        return int(res)


result = Solution()
n = 8
print(result.mySqrt(n))


