# -*- conding:utf-8 -*-
#Author:lyc
import copy

# **回溯算法框架**

# Example1：列表全排列问题
res = []
def backtrack(nums:list, track:list):

    # 结束条件
    if len(nums) == len(track):
        # track是变动的，因此需要拷贝
        res.append(track.copy())
        return

    for i in range(len(nums)):
        # 跳过重复的元素
        if nums[i] in track:
            continue
        # 做选择阶段
        track.append(nums[i])
        # 递归阶段
        backtrack(nums, track)
        # 撤销选择
        track.pop()

nums, track = [1,2,3], []
backtrack(nums, track)
print(res)


# Example2：利用回溯算法解决八皇后问题
# 使用模板
res = []
def backtrack(board:list, row:int):

    if len(board) == row:
        res.append(copy.deepcopy(board))
        return
    n = len(board[row])
    for col in range(n):
        if not isValid(board, row, col):
            continue
        board[row][col] = 'Q'
        backtrack(board, row+1)
        board[row][col] = '.'


def isValid(board:list, row:int, col:int):

    # 检查列是否有冲突
    n = len(board)
    for i in range(n):
        if board[i][col] == 'Q':
            return False

    # 检查右上方是否有冲突
    i, j = row-1, col+1
    while i>=0 and j<n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    # 检查左上方是否有冲突
    i, j = row-1, col-1
    while i>=0 and j>=0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    return True



num = 8
board = [['.']*num for i in range(num)]
backtrack(board, 0)

# 输出结果
count = 1
for i in res:
    print('result {}:'.format(count))
    for j in i:
        print(j)
    count += 1