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
        first,second = result,result

        while second:
            # first指针先跑k步，如果不够k步直接返回
            for i in range(k):
                first = first.next
                if not first:
                    return result.next


            cur = second.next
            for i in range(k):
                x = cur.next
                cur.next = x.next
                x.next = second.next
                second.next = x

            second = cur
            first = second


        return result.next

    def reverse(self, head):

        pre = None
        pnext = None
        while head:
            pnext = head.next
            head.next = pre
            pre = head
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






