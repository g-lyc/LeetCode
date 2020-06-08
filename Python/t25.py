# -*- conding:utf-8 -*-
#Author:lyc
import os, sys

# 题目：
# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
# k 是一个正整数，它的值小于或等于链表的长度。
# 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
#
# 示例：
# 给你这个链表：1->2->3->4->5
# 当 k = 2 时，应当返回: 2->1->4->3->5
# 当 k = 3 时，应当返回: 3->2->1->4->5
#
# 说明：
# 你的算法只能使用常数的额外空间。
# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        # 传入链表为空或只有一个元素时返回
        if not head:return None
        if not head.next:return head

        # 创建带有保护节点的链表
        result = ListNode(0)
        result.next = head

        # 创建两个指针
        pre,end = result,result

        while end:
            # end指针先跑k步，如果不够k步直接返回
            for i in range(k):
                end = end.next
                if not end:
                    return result.next

            # 截取k长度子链表，保留首尾节点
            startNode = pre.next
            endNode = end.next
            end.next = None

            # 截取的子链表反转，返回的结果中startNode节点已经到了第k个位置
            pre.next = self.reverse(startNode)

            # 将原来截取剩余的两边添加至尾部
            startNode.next = endNode

            # 更新pre和end节点的位置，进行下一轮迭代
            pre = startNode
            end = pre

        return result.next

    def reverse(self, head):
        """
        反转链表
        :param head:
        :return:
        """
        pre = None
        pnext = None
        while head:
            # 截取当前节点之后的链表
            pnext = head.next
            # 将当前节点的下个节点设置为pre链表
            head.next = pre
            # pre赋值为当前节点
            pre = head
            # head赋值为当前节点的下一个节点，用于迭代
            head = pnext

        return pre


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
new_node = result.reverseKGroup(node,2)
print(result.showNode(new_node))






