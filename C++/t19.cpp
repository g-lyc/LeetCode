#include <cstddef>


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
    ListNode* removeNthFromEnd(ListNode* head, int n) {

        ListNode* newNode = new ListNode(0);

        newNode->next = head;

        ListNode* first = newNode;
        ListNode* second = newNode;

        for(int i=0; i <= n ; i++)
        {
            first = first->next;
        }

        while (first != NULL)
        {
            first = first->next;
            second = second->next;
        }

        second->next = second->next->next;

        return newNode->next;
        
    };
};


int main()
{
    ListNode* node;
    
    Solution result;

}
