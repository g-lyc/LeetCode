# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# -> 函数注释信息
class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        add two NodeList value
        """
        sum_num = l1.val + l2.val
        l3 = ListNode(sum_num % 10)
        l3.next = ListNode(sum_num // 10)
        p1 , p2 , p3 = l1.next , l2.next , l3

        while True:

            if p1 and p2:
                sum = p1.val + p2.val + p3.next.val
                p3.next.val = sum % 10
                p3.next.next = ListNode(sum // 10)
                p1 , p2 , p3 = p1.next , p2.next , p3.next

            elif p1 and not p2:
                sum = p1.val + p3.next.val
                p3.next.val = sum % 10
                p3.next.next = ListNode(sum // 10)
                p1, p3 = p1.next, p3.next

            elif not p1 and p2:
                sum = p2.val + p3.next.val
                p3.next.val = sum % 10
                p3.next.next = ListNode(sum // 10)
                p2, p3 = p2.next, p3.next

            else:
                if p3.next.val == 0:
                    p3.next = None
                break
        return l3


    def printListNode(self, listNode):
        """
        print value of NodeList
        """
        v_list = []
        head = listNode
        while head:
            v_list.append(head.val)
            head = head.next
        return v_list[::-1]

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

model = Solution()
result = model.addTwoNumbers(l1,l2)
#print(result)
print(model.printListNode(result))


