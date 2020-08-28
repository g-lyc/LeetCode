# -*- conding:utf-8 -*-
#Author:lyc
import os, sys

# 题目：
# 给定一个二叉树，检查它是否是镜像对称的。

# 示例：
# 输入：[1,2,2,3,4,4,3]
# 输出: true
# 输入：[1,2,2,null,3,null,3]
# 输出: false

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        else:
            return self.checkSame(root.left, root.right)

    def checkSame(self, left:TreeNode, right:TreeNode):

        if left != None and right != None and left.val == right.val:
            return self.checkSame(left.right, right.left) and \
                   self.checkSame(left.left, right.right)
        elif left == None and right == None:
            return True
        else:
            return False


p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(2)
p.left.left = TreeNode(3)
p.left.right = TreeNode(4)
p.right.left = TreeNode(4)
p.right.right = TreeNode(3)


result = Solution()
print(result.isSymmetric(p))
