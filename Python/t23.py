# -*- conding:utf-8 -*-
#Author:lyc
import os, sys

# 题目：
# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
#
# 示例:
# 输入:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 输出: 1->1->2->3->4->4->5->6



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: [ListNode]) -> ListNode:
        """
        将所有元素取出来放在列表中排序再逐个添加至新链表
        :param lists:
        :return:
        """

        # 当传入的链表list为空或者只有一个时直接返回
        if len(lists) == 0:return []
        if len(lists) == 1:return lists[0]

        # 定义最终返回的链表，带有保护节点
        merge_node = ListNode(0)
        result = merge_node

        # 将所有链表的元素取出放入列表
        node_list = []
        for node in lists:
            while node:
                node_list.append(node.val)
                node = node.next

        # 排序
        node_list.sort()

        # 将列表中每一个元素添加至新链表
        while node_list:
            merge_node.next = ListNode(node_list.pop(0))
            merge_node = merge_node.next

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


class Solution:
    def mergeKLists(self, lists: [ListNode]) -> ListNode:
        """
        官网解法，使用基于堆的优先级队列
        :param lists:
        :return:
        """
        import heapq
        dummy = ListNode(0)
        p = dummy
        head = []
        for i in range(len(lists)):
            if lists[i] :
                heapq.heappush(head, (lists[i].val, i))
                lists[i] = lists[i].next
        while head:
            val, idx = heapq.heappop(head)
            p.next = ListNode(val)
            p = p.next
            if lists[idx]:
                heapq.heappush(head, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return dummy.next

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


# 创建三个测试链表
node1 = ListNode(1)
node1.next = ListNode(4)
node1.next.next = ListNode(5)

node2 = ListNode(1)
node2.next = ListNode(3)
node2.next.next = ListNode(4)

node3 = ListNode(2)
node3.next = ListNode(6)

lists = [node1, node2, node3]

result = Solution()
new_node = result.mergeKLists(lists)
print(result.showNode(new_node))












