# -*- conding:utf-8 -*-
#Author:lyc
import os, sys

# 题目：
# 将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
#
# 示例：
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        同时遍历两个链表，小的值直接链向新创建的链表，直到短的
        一个遍历完之后，将另一个链表剩余的元素直接链向新链表
        :param l1:
        :param l2:
        :return:
        """
        l3 = ListNode(0)
        result = l3
        # 同时遍历，头结点往后移动
        while l1 and l2:
            if l1.val >= l2.val:
                l3.next = l2
                l2 = l2.next
            else:
                l3.next = l1
                l1 = l1.next
            l3 = l3.next

        # 判断哪个链表不为空，将剩余元素加在l3之后
        l3.next = l1 if not l2 else l2
        return result.next

    def showNode(self, head:ListNode) -> list:
        """
        打印节点元素
        :param head:
        :return:
        """
        s = []
        while head:
            s.append(head.val)
            head = head.next
        return s



node1 = ListNode(1)
node1.next = ListNode(2)
node1.next.next = ListNode(4)

node2 = ListNode(1)
node2.next = ListNode(3)
node2.next.next = ListNode(4)

result = Solution()
new_node = result.mergeTwoLists(node1, node2)
print(result.showNode(new_node))
