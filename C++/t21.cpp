#include <cstddef>
#include <iostream>

using namespace std;

/**
 *  leetcode第21题
 *  遍历移动头结点
 *  Author:lyc
*/

/**
 * Definition for singly-linked list.
 */
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {

        // 创建一个保护节点，不用对边界进行特殊处理
        ListNode* newNode = new ListNode(0);

        // 创建一个头节点用于返回
        ListNode* result = newNode;

        while (l1 != NULL & l2 != NULL)
        {
            if(l1->val >= l2->val)
            {
                newNode->next = l2;
                l2 = l2->next;
            }
            else
            {
                newNode->next = l1;
                l1 = l1->next;
            }

            newNode = newNode->next;
        };

        if(l1 == NULL)
        {
            newNode->next = l2;
        }
        else
        {
            newNode->next = l1;
        };

        return result->next;
        
    };
};



int main()
{

    // 创建第一个节点
    ListNode* node1 = new ListNode(1);
    ListNode* node2 = new ListNode(2);
    ListNode* node3 = new ListNode(4);
    node1->next = node2;
    node2->next = node3;

    // 创建第二个节点
    ListNode* node4 = new ListNode(1);
    ListNode* node5 = new ListNode(3);
    ListNode* node6 = new ListNode(4);
    node4->next = node5;
    node5->next = node6;

    Solution result;

    ListNode *res = result.mergeTwoLists(node1,node4);

    // 循环打印合并元素之后的链表
    while(res != NULL)
    {
        cout << res->val << endl;
        res = res->next;
    }

    system("pause");
    return 0;

}