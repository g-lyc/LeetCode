# -*- conding:utf-8 -*-
#Author:lyc
import os, sys

# 题目：
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
#
# 示例：
# 输入：n = 3
# 输出：[
#        "((()))",
#        "(()())",
#        "(())()",
#        "()(())",
#        "()()()"
#      ]


class Solution:
    def generateParenthesis(self, n: int) -> [str]:
        """
        回溯算法
        :param n:
        :return:
        """
        # 输入数字为0时直接返回空列表
        if n == 0:
            return []

        # 存放最终结果的列表
        result = []

        def backtrack(left:int, right:int, track) -> list:

            """
            定义回溯算法函数，关键是判断track中左括号不能比右括号少
            :param left: 左括号的初始个数
            :param right: 右括号的初始个数
            :param track: 括号组合的记录
            :return:
            """
            # 退出条件：
            # 1、左括号剩余的比右括号多时
            # 2、如果左括号或右括号的个数小于0时
            # 3、左右括号同时遍历完时说明该track符合要求，添加至结果并返回
            if left > right : return
            if left < 0 or right < 0 : return
            if left == 0 and right == 0:
                result.append(track)
                return

            # 每次都需要尝试添加左括号和右括号，添加之后对应的一边减去1，递归调用
            track += '('
            backtrack(left-1, right, track)
            track = track[:-1]

            track += ')'
            backtrack(left, right-1, track)
            track = track[:-1]


        track = ''
        backtrack(n, n, track)
        return result



result = Solution()
n = 3
print(result.generateParenthesis(n))




