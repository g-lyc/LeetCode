# -*- conding:utf-8 -*-
#Author:lyc
import os, sys, copy

# 题目：
# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
# 给定一个整数 n，返回 n 皇后不同的解决方案的数量。
#
# 示例:
# 输入: 4
# 输出: 2
# 解释: 4 皇后问题存在如下两个不同的解法。
# [
#  [".Q..",  // 解法 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // 解法 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]


# 采用回溯算法
class Solution:
    def totalNQueens(self, n: int) -> int:
        res = []
        num = n
        board = [['.'] * num for i in range(num)]
        backtrack(board, 0, res)

        # 相比51题，这里只需要返回数量即可
        return len(res)


def backtrack(board: list, row: int, res):

    if len(board) == row:
        res.append(copy.deepcopy(board))
        return
    n = len(board[row])
    for col in range(n):
        if not isValid(board, row, col):
            continue
        board[row][col] = 'Q'
        backtrack(board, row + 1, res)
        board[row][col] = '.'

def isValid(board: list, row: int, col: int):

    # 检查列是否有冲突
    n = len(board)
    for i in range(n):
        if board[i][col] == 'Q':
            return False

    # 检查右上方是否有冲突
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    # 检查左上方是否有冲突
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    return True

n = 8
result = Solution()
print(result.totalNQueens(n))








