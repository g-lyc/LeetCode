# -*- conding:utf-8 -*-
#Author:lyc
import os, sys

# 题目：
# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
#
# 示例：
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
#
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
# 说明：
# 给定的 n 保证是有效的。
#
# 进阶：
# 你能尝试使用一趟扫描实现吗？



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 解法一：双循环
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        # 创建一个新的头节点用于后续删除节点后返回
        new_head = ListNode(0)
        new_head.next = head

        # 计算链表的长度
        nodeLens = 0
        while head:
            nodeLens += 1
            head = head.next

        # 计算从头到删除节点的长度
        subLens = nodeLens - n

        # 创建新的头节点p用于删除对应节点
        p = new_head

        while subLens > 0:
            subLens -= 1
            p = p.next

        # 遍历到删除的节点后将next指针指向下下个元素的next
        p.next = p.next.next

        return new_head.next



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




# 解法二：双指针
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        # 创建一个新的头节点用于后续删除节点后返回
        new_head = ListNode(0)
        new_head.next = head

        # 设置双指针
        first = new_head
        second = new_head

        # 第一个指针先走n步
        for i in range(n+1):
            first = first.next

        # 接着上一步，两个指针同时走，直到第一个指针到了尾部
        while first != None:
            first = first.next
            second = second.next
        # 第二个指针与第一个指针相差n步，这时跳过下一个元素即可
        second.next = second.next.next

        return new_head.next



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
node.next.next.next.next = ListNode(5)

result = Solution()
n = 2

new_node = result.removeNthFromEnd(node, n)
print(result.showNode(new_node))
