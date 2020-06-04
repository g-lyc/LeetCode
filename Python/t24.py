# -*- conding:utf-8 -*-
#Author:lyc
import os, sys

# 题目：
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
# 示例:
# 给定 1->2->3->4, 你应该返回 2->1->4->3.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        设置三个指针移动
        :param head:
        :return:
        """
        # 链表为空或只有一个元素时返回
        if not head:return None
        if not head.next:return head

        result = ListNode(0)
        result.next = head

        first = result
        mid = head
        second = head.next

        while mid and second:
            # 交换节点
            mid.next = second.next
            second.next = mid
            first.next = second

            # 移动节点
            first = mid
            mid = first.next
            if mid:second=mid.next

        return result.next


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
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)

result = Solution()
new_node = result.swapPairs(node)
print(result.showNode(new_node))





