# -*- conding:utf-8 -*-
#Author:lyc
import os, sys


# 将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
#
# 比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
#
# L   C   I   R
# E T O E S I I G
# E   D   H   N
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
#
# 请你实现这个将字符串进行指定行数变换的函数：
#
# string convert(string s, int numRows);
# 示例 1:
#
# 输入: s = "LEETCODEISHIRING", numRows = 3
# 输出: "LCIRETOESIIGEDHN"
# 示例 2:
#
# 输入: s = "LEETCODEISHIRING", numRows = 4
# 输出: "LDREOEIIECIHNTSG"
# 解释:
#
# L     D     R
# E   O E   I I
# E C   I H   N
# T     S     G



class Solution:

    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1 or numRows >= len(s):
            return s

        # 定义总行数大小的字符串列表
        result = ['']*numRows
        # 定义当前行的位置和移动步长(正向、反向)
        cur_position, step = 0, 1

        for item in s:
            # 按照步长依次赋值给每一行
            result[cur_position] += item
            cur_position += step
            # 当到达每行的临界点时，步长改变方向
            if cur_position == 0 or cur_position == numRows-1:
                step = -step

        result = ''.join(result)
        return result


result = Solution()
s = "LEETCODEISHIRING"
n = 3
print(result.convert(s,n))




