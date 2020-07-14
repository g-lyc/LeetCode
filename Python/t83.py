# -*- conding:utf-8 -*-
#Author:lyc
import os, sys

# 题目：
# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

# 示例 1:
# 输入: 1->1->2
# 输出: 1->2

# 示例 2:
# 输入: 1->1->2->3->3
# 输出: 1->2->3




# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 解法1，将链表转成list，去重，再转成链表
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        if not head : return 0

        lnode = self.showNode(head)
        uni_lnode = []
        for i in lnode:
            if i not in uni_lnode:
                uni_lnode.append(i)
        lnode = uni_lnode
        res = ListNode(lnode[0])
        result = res
        for i in lnode[1:]:
            res.next = ListNode(i)
            res = res.next

        return result



    def showNode(self, node : ListNode) -> list:
        """
        show all value of ListNode
        :param node:
        :return:
        """
        nodeValue = []
        head = node
        while head:
            nodeValue.append(head.val)
            head = head.next
        return nodeValue



# 解法2，判断当前节点的值和下一个节点的值是否相等
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        res = head
        temp = res
        while temp and temp.next:
            if temp.val == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return res
        
    def showNode(self, node : ListNode) -> list:
        """
        show all value of ListNode
        :param node:
        :return:
        """
        nodeValue = []
        head = node
        while head:
            nodeValue.append(head.val)
            head = head.next
        return nodeValue


node = ListNode(1)
node.next = ListNode(1)
node.next.next = ListNode(2)


result = Solution()

new_node = result.deleteDuplicates(node)
print(result.showNode(new_node))
