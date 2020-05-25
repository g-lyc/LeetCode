#include <cstddef>
#include <iostream>

using namespace std;

/**
 *  leetcode第19题
 *  利用双指针移动步长差求解
 *  Author:lyc
*/


// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {

        // 创建一个保护节点，不用对边界进行特殊处理
        ListNode* newNode = new ListNode(0);

        // 保护节点与head连接
        newNode->next = head;

        // 创建两个指针用于移动
        ListNode* first = newNode;
        ListNode* second = newNode;

        // 先移动第一个指针，移动n个步长
        for(int i=0; i <= n ; i++)
        {
            first = first->next;
        }

        // 两个指针同时移动，直到第一个指针为NULL
        while (first != NULL)
        {
            first = first->next;
            second = second->next;
        }

        // 此时两个指针相差n步，第二个指针的下一个元素即为要删除的元素，跳过此元素
        second->next = second->next->next;

        // 返回链表时跳过保护节点
        return newNode->next;
        
    };
};


int main()
{
    /**
     * 利用定义好的链表结构体创建一个链表
    */
    ListNode* node1 = new ListNode(1);
    ListNode* node2 = new ListNode(2);
    ListNode* node3 = new ListNode(3);
    ListNode* node4 = new ListNode(4);
    ListNode* node5 = new ListNode(5);

    node1->next = node2;
    node2->next = node3;
    node3->next = node4;
    node4->next = node5;
    
    // 声明需要删除倒数第几个元素
    int n = 2;

    Solution result;

    ListNode *res = result.removeNthFromEnd(node1, n);

    // 循环打印删除对应元素之后的链表
    while(res != NULL)
    {
        cout << res->val << endl;
        res = res->next;
    }

    system("pause");
    return 0;

}
